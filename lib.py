import pandas as pd
import os
from constants import REVOLUT_REL_PATH, DEFAULT_FLOAT_PRECISION

class Parser:
    def __init__(self, master_key, expected_value):
        self.master_key = master_key
        self.expected_value = expected_value
        self.file_cache = {}

    def parse_file(self, file_path):
        self.file_cache = pd.read_csv(file_path).to_dict()

    def solve_expanses(self):
        data = self.file_cache
        keys = data.keys()
        out = []
        for index in range(0, len(data[list(keys)[0]])):
            obj = {}
            for key in keys:
                obj[key] = data[key][index]
            out.append(obj)
        return out

    def solve_directory(self, directory_path):
        file_list = [file for file in os.listdir(directory_path) if file.endswith('.csv') and os.path.isfile(os.path.join(directory_path, file))]
        out = []
        for file_name in file_list:
            self.parse_file(os.path.join(directory_path, file_name))
            self.solve_expanses()
            out.append(self.solve_expanses())
        return out
    
    def solve_for_master_key(self):
        data = self.file_cache
        keys = data.keys()
        check_for_master_key(self.master_key, keys)
        master_key = self.master_key
        indices = []
        for index in range (0, len(data[master_key])):
            if data[master_key][index] != self.expected_value:
                continue
            indices.append(index)
        
        out = []
        for idx in indices:
            obj = {}
            for key in keys:
                obj[key] = data[key][idx]
            out.append(obj)
        return out
    
    def solve_directory_for_master_key(self, directory_path):
        file_list = [file for file in os.listdir(directory_path) if file.endswith('.csv') and os.path.isfile(os.path.join(directory_path, file))]
        out = []
        for file_name in file_list:
            self.parse_file(os.path.join(directory_path, file_name))
            self.solve_for_master_key()
            out.append(self.solve_for_master_key())
        return out
    
    def sort_expanses(self, expanses):
        master_key = self.master_key
        out = {}
        for expanse in expanses:
            if expanse[master_key] in out:
                out[expanse[master_key]].append(expanse)
            else:
                out[expanse[master_key]] = [expanse]
        return out

    def sum_sorted_expanses(self, expanses, identifying_key, value_key):
        out = {}
        for expanse in expanses:
            if expanse[identifying_key] not in out:
                out[expanse[identifying_key]] = float(expanse[value_key])
            else:
                out[expanse[identifying_key]] += float(expanse[value_key])
        return out

def round_sorted_expanses(sorted_expanses):
    out = {}
    for key, value in sorted_expanses.items():
        out[key] = round(value, DEFAULT_FLOAT_PRECISION)
    return out

def calculate_sum(output, value_key):
    out = 0.0
    for obj in output:
        out += float(obj[value_key])
    return round(out, DEFAULT_FLOAT_PRECISION)

def check_for_master_key(master_key, keys):
    if master_key not in keys:
        raise RuntimeError("Master Key does not exist in .csv")