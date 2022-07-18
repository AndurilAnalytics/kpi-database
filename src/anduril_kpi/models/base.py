from anduril_kpi.models import KPI_DATA

class ModelBase:
    def __init__(self, columns, folder, index) -> None:
        self._data = self._file_load()
        self._columns = columns
        self._folder = folder
        self._index = index

    def _add_index(self, df):
        columns = [self._index]
        columns.extend(df.columns)
        df[self._index] = df.index
        df = df[columns]
        return df


    def _file_load(self):
        return KPI_DATA

    @property
    def columns(self):
        return self._columns

    @property
    def file_columns(self):
        return [column['name'] for column in self._columns]

    @property
    def display_columns(self):
        return [column['display'] for column in self._columns]