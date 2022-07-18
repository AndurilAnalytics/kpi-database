# Standard Imports
from pathlib import Path
PATH = Path(__file__).parent

# Module Imports
from anduril_kpi.modules import dataframes

# Application Imports
from anduril_kpi.models.base import ModelBase



class Industry(ModelBase):
    CONFIG = {
        'columns': [
            {
                'name': 'industry',
                'display_name':'Industry'
            }
        ]
        ,'folder': 'industry'
        ,'index': 'industry_id'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'], index=self.CONFIG['index'])

    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def industries(self, display=False, return_type='df', reindex_column=None, include_index=False):
        
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns

        data = self._load(columns=columns, display=display)
        data = dataframes.drop_duplicates(df=data)

        if reindex_column:
            columns.append(reindex_column)
        data = self._load(columns=columns, display=display)
        
        if include_index:
            data = self._add_index(data)
        return data

def industries(display=False, return_type='df', reindex_column=None, include_index=False):
    i = Industry()
    return i.industries(display=display, return_type=return_type, reindex_column=reindex_column, include_index=include_index)