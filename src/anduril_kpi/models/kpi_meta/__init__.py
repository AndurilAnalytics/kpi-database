# Standard Imports
from pathlib import Path
PATH = Path(__file__).parent

# Module Imports
from anduril_kpi.modules import dataframes

# Application Imports
from anduril_kpi.models.base import ModelBase

class KPIMeta(ModelBase):
    CONFIG = {
        'columns': [
            {
                'name': 'kpi_unit',
                'display_name':'KPI Unit'
            },
            {
                'name': 'kpi_output_type',
                'display_name':'KPI Output Type'
            },
            {
                'name': 'kpi_source',
                'display_name':'KPI Source'
            },

        ]
        ,'folder': 'kpi_meta'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'])

    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def meta(self, display=False, return_type='df'):
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns

        data = self._load(columns=columns, display=display)
        return dataframes.drop_duplicates(df=data)


def kpis_meta(display=False, return_type='df'):
    i = KPIMeta()
    return i.meta(display=display, return_type=return_type)