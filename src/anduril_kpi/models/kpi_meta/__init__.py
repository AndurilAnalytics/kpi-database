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
                'name': 'kpi_formula',
                'display_name':'KPI Formula'
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
        ,'index': 'kpi_meta_id'

    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'], index=self.CONFIG['index'])

    def _load(self, columns, display=False):
        if display:
            print(self._data.columns)
            return self._data[columns]    
        return self._data[columns]

    def meta(self, display=False, return_type='df', reindex_column=None, include_index=False):
        columns = None
        if display:
            columns=self.display_columns
        else:
            columns = self.file_columns


        if reindex_column:
            columns.append(reindex_column)
        data = self._load(columns=columns, display=display)
        data = dataframes.drop_duplicates(df=data)
        
        if include_index:
            data = self._add_index(data)

        return data


def kpis_meta(display=False, return_type='df', reindex_column=None, include_index=False):
    i = KPIMeta()
    return i.meta(display=display, return_type=return_type, reindex_column=reindex_column, include_index=include_index)