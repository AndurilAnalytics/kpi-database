from pathlib import Path

from anduril_kpi import DATA_FOLDER
from anduril_kpi.modules.files import loader

CURRENT_FOLDER = Path(__file__).parent
METRIC_FILENAME = 'metric_list.xlsx'


def metric_file():
    loader.load(path=DATA_FOLDER.joinpath(METRIC_FILENAME))


