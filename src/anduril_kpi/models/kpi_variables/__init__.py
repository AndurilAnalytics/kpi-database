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
                'name': 'var_a_type',
                'display_name':'Variable A Type'
            },
            {
                'name': 'var_a_name',
                'display_name':'Variable A Name'
            },
            {
                'name': 'var_b_type',
                'display_name':'Variable B Type'
            },
            {
                'name': 'var_b_name',
                'display_name':'Variable B Name'
            }
        ]
        ,'folder': 'kpi_variables'
        ,'index': 'kpi_vairables_id'
    }
    def __init__(self) -> None:
        super().__init__(columns=self.CONFIG['columns'], folder=self.CONFIG['folder'], index=self.CONFIG['index'])

    def _load(self, columns, display=False):
        if display:
            return self._data[columns]    
        return self._data[columns]

    def variables(self, display=False, return_type='df', reindex_column=None, include_index=False):
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


def kpis_variables(display=False, return_type='df', reindex_column=None, include_index=False):
    k = KPIVariables()
    return k.variables(display=display, return_type=return_type, reindex_column=reindex_column, include_index=include_index)