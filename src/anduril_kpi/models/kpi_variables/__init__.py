# Standard Imports
from pathlib import Path
PATH = Path(__file__).parent

# Module Imports
from anduril_kpi.modules import dataframes

# Application Imports
from anduril_kpi.models.base import ModelBase

class KPIVariables(ModelBase):
    CONFIG = {
        'columns': [
            {
                'name': 'kpi_tags',
                'display_name':'KPI Variables'
            }
        ]
        ,'folder': 'kpi_variables'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'])

    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def variables(self, display=False, return_type='df'):
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns

        data = self._load(columns=columns, display=display)
        data = dataframes.drop_duplicates(df=data)
        # data = dataframes.series_unstack(series=data, column='kpi_tags')
        return data


def kpis_variables(display=False, return_type='df'):
    k = KPIVariables()
    return k.tags(display=display, return_type=return_type)