import pandas as pd
import numpy as np

class ResultBuilder:
    def __init__(self) -> None:
        pass

def melt(df, id_vars, value_vars, var_name, value_name):
    return df.melt(id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)

def columns(df):
    return list(df.columns)

def unique_list(df, column):
    """
        Purpose: Return the unique columns of a series
        TODO: Side effect even if a list is submitted it will only return the unique
            values from the first item in the list. Can't use a list comprehension 
            because there likely wouldn't be a need for the unique from multiple
            columns to be contained in a single list 
    """
    if isinstance(column, list):
        return list(df[column[0]].unique())
    return list(df[column].unique())

def unique_dict(df, columns):
    return {column: unique_list(df, column)  for column in columns}

def column_unique(df, columns, return_type='list'):
    """
        Purpose: Return the unique column values
        Parameters:
            df(pd.DataFrame) - data
            columns()
    """
    HANDLERS = {
        'list': unique_list,
        'dict': unique_dict
    }
    handler = HANDLERS[return_type]
    return handler(df, columns)

def dtypes(df):
    return df.dtypes

DATA_TYPES = {
    'int': 'int64',
    'small_int': 'int32',
    'float': 'float64',
    'small_float': 'float32',
    'datetime': 'datetime',
    'bool': 'bool'
}

DATA_TYPE_SELECTIONS = {
    'number': 'number',
    'datetime': 'datetime',
    'category': 'category',
    'object': 'object',
    'bool': 'bool'

}

def select_dtypes(df, dtypes):
    """
        Purpose: Returns a datatype of the requested type or types
        Parameters: 
            df(pd.DataFrame) - pandas dataframe
            dtypes(list of str) - list of strings for dtypes needed
        Returns
            pd.DataFrame - Dataframe with only the columns with dtypes filtered for 
    """
    return df.select_dtypes(include=dtypes)

def set_dtype(df, settings):
    """
        Purpose: Set the dtypes for a dataframe
        Parameters:
            df(pd.DataFrame) - data to be type casted
            settings(dict) - {'column': 'dtype'}
    """
    return df.astype(settings)


def fill_nan(df, values):
    return df.fillna(value=values)

def drop_nan(df, axis):
    """
        Purpose: Drop nans from an axis
        Parameters:
            axis(str)
    """
    AXIS_OPTIONS = {
        'rows': 0,
        'columns': 1
    }
    return df.dropna(axis=AXIS_OPTIONS[axis])

def append(dfs):
    """
        Purpose: Append a list of dataframes or series
        Parameters:
            dfs(list of pd.DataFrame or pd.Series) - a list of dataframes or series to append 
    """
    return pd.concat(dfs)

def group_by(df, columns, aggregator=None):
    if aggregator:
        return df.groupby(columns).agg(aggregator).reset_index()
    return df.groupby(columns)

def drop_duplicates(df, subset=None, reset_index=True):
    return df.drop_duplicates(subset=subset, ignore_index=reset_index)

def series_unstack(series, column):
    """
        TODO: Finish series unstack
    """
    values = series.values
    return values

def column_unstack(df, column):
    return pd.DataFrame({
        col:np.repeat(df[col].values, df[column].str.len())
        for col in df.columns.difference([column])
        }).assign(**{column:np.concatenate(df[column].values)})[df.columns.tolist()]

def reindex(df, columns):
    return df.set_index(columns)
    
def merge(df, other_df, fields, join_type):
    return pd.merge(df, other_df, on=fields, how=join_type)