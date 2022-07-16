from ..folders import files_in_folder
from .. import dataframes

class Collector:
    def __init__(self, path, options=None) -> None:
        self._path = path
        self._extension = None
        self._options = None
        self._handle_options(options)
        self._data = None

    def _handle_options(self, options):
        if options:
            self._extension = options.pop('extension', None)
            self._options = options

    def collect(self):
        return self._collect()

    def _collect(self):
        files = files_in_folder(self._path, extension=self._extension)
        return dataframes.append(files)

def collect(path, options=None):
    l = Collector(path=path, options=options)
    return l.collect()