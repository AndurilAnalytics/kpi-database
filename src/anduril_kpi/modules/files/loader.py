import pandas as pd


class Loader:
    def __init__(self, path, xlsx_options=None) -> None:
        self._path = path
        self._xlsx_options = xlsx_options
        self._data = None

    def load(self):
        file_extension = self._path.suffix[1:]
        with open(self._path, 'rb') as f:
            handler = getattr(self, f'_read_{file_extension}')
            self._data = handler(f)
        return self._data

    def _read_csv(self, open_file):
        csv_data = pd.read_csv(open_file, converters=self._converter)
        return csv_data

    def _read_xlsx(self, open_file):

        xlsx_data = pd.read_excel(open_file)
        return xlsx_data


def load(path, xlsx_options=None):
    l = Loader(path=path, xlsx_options=xlsx_options)
    return l.load()