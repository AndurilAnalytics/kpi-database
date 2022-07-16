# Standard Imports
from pathlib import Path

# Module Imports
from anduril_kpi.modules import dataframes

# Application Imports
from anduril_kpi.models.base import ModelBase



CURRENT_PATH = Path(__file__).parent

COMPANY_HANDLERS = {
    'df': None,
    'list': None,
}

class Company(ModelBase):
    CONFIG = {
        'columns': [
            {
                'name': 'ticker',
                'display_name':'Ticker'
            },
            {
                'name': 'company',
                'display_name': 'Company Name'
            }
        ],
        'folder': 'company'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'])
        
    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def companies(self, display=False, return_type='df'):
        
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns

        data = self._load(columns=columns, display=display)
        return dataframes.drop_duplicates(df=data)  

    def create_db():
        pass

def companies():
    c = Company()
    return c.companies()
    

