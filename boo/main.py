# TODO: pip install boo

import pandas as pd

from .year import YEARS, make_url
from .file import curl, yield_rows, save_rows
from .path import raw, processed, canonic
from .columns import CONVERTER_FUNC as shorten, SHORT_COLUMNS
from .dataframe import canonic_df, canonic_dtypes


def preclean(path, force: bool):
    """Delete an exisiting file if *force* flag is set to True"""
    if force is True and path.exists():
       path.unlink()

def download(year: int, force=False):
    """Download file from Rosstat."""
    path, url = raw(year), make_url(year), 
    preclean(path, force)
    print("Downloading", url, f"for {year}")
    curl(path, url)
    print("Saved as", path)
    # MAYBE: show line count  
    # TODO: download must fail on small fail on small file or HTML file

     
def cut_columns(year, worker=shorten, column_names=SHORT_COLUMNS.all, 
                force=False):
    """Create smaller local file with fewer columns. 
       Columns will be named with *COLUMNS_SHORT*.
       Rows will be modified by *worker* function.
    """    
    src, dst = raw(year), processed(year)
    preclean(dst, force)
    print("Reading from", src)    
    print("Saving to", dst)    
    save_rows(path=dst, 
              stream=map(worker, yield_rows(src)), 
              column_names=column_names)
    print("Done")  


def read_df(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)  

def write_df(df, path):
    df.to_csv(path, index=False 
                  , header=True         
                  , chunksize=100_000
                  , encoding='utf-8')    
    
def read_intermediate_df(year: int):
    src = processed(year)    
    return read_df(src, SHORT_COLUMNS.dtypes)


def make_canonic_df(year: int, force=False):
    dst = canonic(year)
    preclean(dst, force)
    print (f"Reading intermediate dataframe for {year}...")
    df = canonic_df(read_intermediate_df(year))
    print (f"Created final dataframe for {year}")
    print(f"Saving to {dst}...")
    write_df(df, dst)
    print ("Done")
    

def read_canonic_df(year):
    src = canonic(year)
    return read_df(src, dtypes=canonic_dtypes())
    # MAYBE: save dtypes as json, use them if available to speed up df import  

# Shorthand functions
    
def cut(year: int):
    cut_columns(year, force=False)


def cutf(year: int):
    cut_columns(year, force=True)


def put(year: int):
    make_canonic_df(year, force=False)


def putf(year: int):
    make_canonic_df(year, force=True)


def read_dataframe(year):
    return read_canonic_df(year)    
    

def frame(year: int):
    return read_canonic_df(year)


def prepare(year: int):
    if not raw(year).exists():
        download(year)
    if not processed(year).exists():
        cut(year)
    if not canonic(year).exists():        
        put(year)   


def erase(year):
    for f in raw(year), processed(year), canonic(year):
        f.unlink()
        

def prepare_all():
    for year in YEARS:
        prepare(year)  

# TODO: acquire all at Google Colab
    
if __name__ == "__main__":
    dfs = {}
    #for year in range(2015, 2018):        
    #    print(year)
    #    putf(year)
    #    dfs[year] = frame(year)      
        
# ERROR: trimmed_2016.csv is an anomaly        