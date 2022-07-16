from anduril_kpi.models import LOADED_FILE

class ModelBase:
    def __init__(self, columns, folder) -> None:
        self._data = self._file_load()
        self._columns = columns
        self._folder = folder


    def _file_load(self):
        return LOADED_FILE

    @property
    def columns(self):
        return self._columns

    @property
    def file_columns(self):
        return [column['name'] for column in self._columns]

    @property
    def display_columns(self):
        return [column['display'] for column in self._columns]