# Analyze .csv files from bank statements in Python
Neither Revolut, nor Cedit Suisse offer APIs for non-business customers. As an engineer I am annoyed and therefore chose to write this python library that helps me manage my expanses. Revolut `csv` exports are straightforward but Credit Suisse statements are terrible :). 

Therefore Revolut statements can be anything (monthly, yearly, etc.) and are processed one-by-one using the directory structure described below.

Credit Suisse statements are single file `.csv` exports of the account history (I use yearly). 

`lib.py` exposes all logic required to process the Revolut statements but `cs.py` is an extension for those chunky Credit Suisse statements.

> [!WARNING]
> Salty Engineer!


## Source venv
```bash
source env/bin/activate 
```

## Input structure (.csv)
### Revolut
For `Revolut`, it is recommened to place the input files in `./banks/revolut/MONTH_YEAR.csv`:
```
./banks/revolut/october_2024.csv
./banks/revolut/september_2024.csv
...
```
See examples of how to use this data in `/tests/revolut.py`. 

> [!NOTE]
> Using yearly, quarterly or other data should work fine, adjust higher-level logic accordingly when building on top of `lib.py`.
> `lib.py` is designed to account for possible API changes. The examples in `/tests/` show more clearly how it works.


### Credit Suisse