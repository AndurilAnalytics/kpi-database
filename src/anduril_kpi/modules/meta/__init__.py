from files import saver, loader
from paths import path

class Meta:
    CONFIG = {
        "file_name": "meta",
        "file_extension": ".json"
    }
    def __init__(self, folder_path, meta_data=None) -> None:
        self._folder_path = folder_path
        self._file_path = self._create_file_path()
        self._meta_data = meta_data

    def _create_file_path(self):
        file_name = self.CONFIG['file_name']
        file_extension = self.CONFIG['file_extension']
        return path(self._folder_path, path_name=f'{file_name}{file_extension}')
        
    def _load(self):
        return loader.load(path=self._folder_path)

    def load(self):
        return self._load()

    def _save(self):
        return saver.save(data = self._meta_data, path=self._file_path)

    def save(self):
        return self._save()

def meta_data(folder_path):
     m = Meta(folder_path=folder_path)
     return m.load()

def save_meta_data(folder_path, meta_data):
    m = Meta(folder_path=folder_path, meta_data=meta_data)
    return m.save()

