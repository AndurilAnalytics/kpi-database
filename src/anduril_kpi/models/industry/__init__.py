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
        ,'folder': 'company'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'])

    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def industries(self, display=False, return_type='df'):
        
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns

        data = self._load(columns=columns, display=display)
        return dataframes.drop_duplicates(df=data)

def industries(display=False, return_type='df'):
    i = Industry()
    return i.industries(return_type=return_type)