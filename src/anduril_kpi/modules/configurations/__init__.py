from files.loader import load
from files.collector import collect

class ConfigurationLoader:
    """
        Purpose: Load a configuration
        Parameters:
            config_type(str) - config handler to use to load the configuration
            options(dict) - dynamic arguments to use with handler
    """
    HANDLERS = {
        'file': load,
        'folder': collect,
        'server': None,
        'bytes': None
    }
    def __init__(self, config_type, options) -> None:
        self._loader = self.HANDLERS[config_type]
        self._options = options

    def  _load(self):
        return self._loader(self._options)

    def load(self):
        return self._load()

class Configuration:
    def __init__(self, options) -> None:
        self._options = options
        self._config_type = self._options.pop('config_type', None)
        self._config = None

    def _load(self):
        loader = ConfigurationLoader(self._config_type, self._options)
        self._config = loader