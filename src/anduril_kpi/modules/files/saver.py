#Standard Imports
import json

# Application Imports
import pandas as pd

class AndurilErrors(Exception):
    def __init__(self):
        self._message = None

    def __str__(self) -> str:
        return f'{self._message}'

class AndurilModuleErrors(AndurilErrors):
    def __init__(self, module_name, message):
        super().__init__()

class Saver:
    TEXT_OPTIONS = {
        'read': 'r',
        'read_binary': 'rb',
        'read_write': 'r+',
        'write': 'w',
        'write_binary': 'wb',
        'append': 'a',
        'append_read': 'a+',
    }
    ENABLED_HANDLERS = ['csv', 'xlsx', 'json']
    def __init__(self, data, path, text_option='write') -> None:
        self._path = path
        self._data = data
        self._text_option = self.TEXT_OPTIONS[text_option]

    def save(self):
        file_extension = self._path.suffix[1:]

        with open(self._path, 'rb') as f:
            handler = getattr(self, f'_read_{file_extension}')
            self._data = handler()
        return self._data

    def _save_xlsx(self):
        """
            Purpose: Save the data as an xlsx file
        """
        self.data.to_excel(self._path,
                           index=False)

    def _save_csv(self):
        """
            Purpose: Save the data as a csv file
        """
        self.data.to_csv(self._path,
                         index=False)

    def _save_json(self):
        """
            Purpose: Save the data as a csv file
        """
        with open(self._path, self._text_option) as outfile:
            json.dump(self.data, outfile)


def save(data, path):
    s = Saver(data=data, path=path)
    return s.save()