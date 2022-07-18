from pathlib import Path

from anduril_kpi import DATA_PATH
from anduril_kpi.modules.files import loader

CURRENT_PATH = Path(__file__).parent
METRIC_FILENAME = 'metric_list.csv'


def load_file(file_name):
    return loader.load(path=DATA_PATH.joinpath(file_name))

LOADED_FILE = load_file(METRIC_FILENAME)

KPI_DATA_FILE_NAME_V1 = 'kpi_data_071722 V1.csv'

KPI_DATA = load_file(KPI_DATA_FILE_NAME_V1)

