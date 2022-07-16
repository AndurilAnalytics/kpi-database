# Standard Imports
from pathlib import Path
PATH = Path(__file__).parent

# Module Imports
from anduril_kpi.modules import dataframes

# Application Imports
from anduril_kpi.models.base import ModelBase
from anduril_kpi.models.handlers import df_handler

def kpi_tag_list_handler(df):
    df = df_handler(df)['kpi_tags']
    tags = list({value.strip() for row in df.values for value in row.split(",")})
    tags.sort()
    return tags



HANDLERS = {
    'df': df_handler,
    'list': kpi_tag_list_handler 
}

class KPITag(ModelBase):
    CONFIG = {
        'columns': [
            {
                'name': 'kpi_tags',
                'display_name':'KPI Tags'
            }
        ]
        ,'folder': 'kpi_tag'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'])

    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def tags(self, display=False, return_type='df'):
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns

        data = self._load(columns=columns, display=display)

        handler = HANDLERS[return_type]
        data = handler(data)
        return data


def kpis_tags(display=False, return_type='df'):
    k = KPITag()
    return k.tags(display=display, return_type=return_type)