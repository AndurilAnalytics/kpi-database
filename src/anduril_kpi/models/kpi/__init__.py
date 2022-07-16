# Standard Imports
from pathlib import Path

from src.anduril_kpi.models.kpi_tags import HANDLERS
PATH = Path(__file__).parent

# Module Imports
from anduril_kpi.modules import dataframes

# Application Imports
from anduril_kpi.models.base import ModelBase
from anduril_kpi.models.handlers import df_handler

def kpi_list_handler(df, column):
    df = df_handler(df)[column]
    tags = list({value.strip() for row in df.values for value in row.split(",")})
    tags.sort()
    return tags



KPITAG_HANDLERS = {
   'df': df_handler,
   'list': kpi_list_handler 
}


class KPI(ModelBase):
    CONFIG = {
        'columns': [
            {
                'name': 'kpi_name',
                'display_name':'KPI Name'
            },
            {
                'name': 'kpi_category',
                'display_name':'KPI Category'
            }
        ]
        ,'folder': 'kpi'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'])

    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def kpis(self, display=False, return_type='df'):
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns

        data = self._load(columns=columns, display=display)
        return dataframes.drop_duplicates(df=data)

    def categories(self, display=False, return_type='df'):
        columns = None
        if display:
            columns=['KPI Category']
        else:
            columns = self.file_columns['kpi_category']

        data = self._load(columns=columns, display=display)
        handler = HANDLERS[return_type]
        return handler(data, column=columns[0])
        


def kpis(display=False, return_type='df'):
    k = KPI()
    return k.kpis(display=display, return_type=return_type)