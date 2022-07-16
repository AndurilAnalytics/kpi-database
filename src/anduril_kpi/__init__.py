# Standard Imports
from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath('data')
DATABASE_PATH = ROOT_PATH.joinpath('database')

def dbify():
    """
        Purpose: Turn the files into a database
    """
    pass

def load():
    # from anduril_kpi.models.company import companies
    # print("Companies: ", companies())

    # from anduril_kpi.models.industry import industries
    # print("Industries: ", industries())

    # from anduril_kpi.models.kpi import kpis
    # print("KPIs: ", kpis())

    # from anduril_kpi.models.kpi_meta import kpis_meta
    # print("KPIs Meta: ", kpis_meta())

    # from anduril_kpi.models.kpi_tags import kpis_tags
    # print("KPIs DF Tags: ", kpis_tags())

    from anduril_kpi.models.kpi_tags import kpis_tags
    print("KPIs List Tags: ", kpis_tags(return_type='list'))
