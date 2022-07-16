from pathlib import Path

from anduril_kpi import DATA_PATH
from anduril_kpi.modules.files import loader

CURRENT_PATH = Path(__file__).parent
METRIC_FILENAME = 'metric_list.csv'


def metric_file():
    return loader.load(path=DATA_PATH.joinpath(METRIC_FILENAME))

LOADED_FILE = metric_file()