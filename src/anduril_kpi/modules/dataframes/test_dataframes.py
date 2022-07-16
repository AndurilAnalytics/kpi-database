# Package Imports
import pandas as pd
from numpy import nan

# Application Module Imports
from ..dataframes import (
    melt, column_unique, columns, unique_dict, unique_list, dtypes, 
    select_dtypes, set_dtype, fill_nan, drop_nan, append
)

DF1_DATA = {
    'letters': ['A', 'B'],
    'numbers': [1,2]
}

DF2_DATA = {
    'letters': ['C', 'D'],
    'numbers': [3,4]
}

DF3_DATA = {
    'letters': ['A', 'B'],
    'numbers': [1,2.0]
}

DF4_DATA = {
    'letters': ['A', 'B'],
    'numbers': [1,2.0],
    'Q1': [0, 0],
    'Q2': [1,1],
    'Q3': [2,2],
}

DF1 = pd.DataFrame(DF1_DATA)
DF2 = pd.DataFrame(DF2_DATA)
DF3 = pd.DataFrame(DF3_DATA)
DF4 = pd.DataFrame(DF4_DATA)

def test_append_dataframes():
    test_df = append([DF1, DF2]) 
    
    assert test_df['letters'].iat[3] == 'D'

NAN_DATA = {
    'letters': ['A', 'B'],
    'numbers': [1,nan]
}

NAN_PDF = pd.DataFrame(NAN_DATA)

def test_drop_nan_rows():
    test_df = drop_nan(df=NAN_PDF, axis='rows')
    
    assert len(test_df) == 1

def test_drop_nan_columns():
    test_df = drop_nan(df=NAN_PDF, axis='columns')
    
    assert list(test_df.columns) == ['letters']

def test_fill_nan_columns():
    test_df = NAN_PDF.copy()
    test_df = fill_nan(df=test_df, values={'numbers': 0})
    
    assert test_df['numbers'].iat[1] == 0

def test_set_type():
    test_df = DF3.copy()

    test_df = set_dtype(test_df, settings={ 'numbers': 'int64'})
    assert test_df['numbers'].dtype == 'int64'

def test_melt():
    test_value_vars = ['Q1', 'Q2', 'Q3']
    test_var_name = 'quarter'
    test_df = melt(df=DF4, id_vars=['letters', 'numbers'], value_vars=test_value_vars, var_name=test_var_name, value_name='quantity')

    assert len(test_df) == len(DF4)*len(test_value_vars)
    assert test_var_name in columns(test_df)
    
def test_column_unique_list():
    test_list = column_unique(df=DF1, columns=['numbers'])

    assert isinstance(test_list, list)
    assert len(test_list) == 2

def test_column_unique_dict():
    test_dict = column_unique(df=DF1, columns=['numbers'], return_type='dict')

    assert isinstance(test_dict, dict)
    assert len(test_dict['numbers']) == 2

def test_columns():
    test_list = columns(df=DF1)

    assert test_list == ['letters', 'numbers']
    assert isinstance(test_list, list)

def test_unique_dict():
    test_dict = unique_dict(df=DF1, columns=['numbers'])

    assert len(test_dict['numbers']) == 2
    assert isinstance(test_dict, dict)

def test_unique_list():
    test_list = unique_list(df=DF1, column='numbers')

    assert len(test_list) == 2
    assert isinstance(test_list, list)

def test_dtypes():
    test_df = dtypes(df=DF1)
    assert test_df.iat[0] == 'object'


def test_select_dtypes():
    test_df = select_dtypes(DF1, dtypes=['number'])

    assert list(test_df.columns) == ['numbers']