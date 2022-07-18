# Standard Imports
from pathlib import Path

# Module Imports
from anduril_kpi.modules import dataframes, files

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath('data')
DATABASE_PATH = ROOT_PATH.joinpath('database')

def join_index(index_df, index_column, df):
    # join on the index dataframe
    return dataframes.merge(df=df, other_df=index_df, fields=[index_column], join_type='left')

def dbify():
    """
        Purpose: Turn the files into a database
    """
    results = []

    from anduril_kpi.models.kpi import kpis
    kpi_data = kpis(include_index=True)
    # print("KPIs: ", kpi_data)
    file_name = 'kpis.csv'
    saved = files.saver.save(data=kpi_data, path=DATABASE_PATH.joinpath(file_name))
    results.append((file_name, saved))

    index_column = 'kpi_name'
    # from anduril_kpi.models.kpi_meta import kpis_meta
    # kpi_meta = kpis_meta(reindex_column=index_column, include_index=False)
    # kpi_meta = join_index(index_df=kpi_data.copy(), index_column=index_column, df=kpi_meta)
    # file_name = 'kpi_meta.csv'
    # saved = files.saver.save(data=kpi_meta, path=DATABASE_PATH.joinpath(file_name))
    # results.append((file_name, saved))

    # from anduril_kpi.models.kpi_variables import kpis_variables
    # kpi_variables = kpis_variables(reindex_column=index_column, include_index=False)
    # kpi_variables = join_index(index_df=kpi_data.copy(), index_column=index_column, df=kpi_variables)
    # file_name = 'kpi_variables.csv'
    # saved = files.saver.save(data=kpi_variables, path=DATABASE_PATH.joinpath(file_name))
    # results.append((file_name, saved))

    # from anduril_kpi.models.kpi_tags import kpis_tags
    # kpis_tags = kpis_tags(reindex_column=index_column, include_index=False)
    # kpis_tags = join_index(index_df=kpi_data.copy(), index_column=index_column, df=kpis_tags)
    # file_name = 'kpi_tags.csv'
    # saved = files.saver.save(data=kpis_tags, path=DATABASE_PATH.joinpath(file_name))
    # results.append((file_name, saved))

    # from anduril_kpi.models.industry import industries
    # industries = industries(reindex_column=index_column, include_index=False)
    # industries = join_index(index_df=kpi_data.copy(), index_column=index_column, df=industries)
    # file_name = 'industries.csv'
    # saved = files.saver.save(data=industries, path=DATABASE_PATH.joinpath(file_name))
    # results.append((file_name, saved))

    from anduril_kpi.models.company import companies
    companies = companies(reindex_column=index_column, include_index=False)
    companies = join_index(index_df=kpi_data.copy(), index_column=index_column, df=companies)
    file_name = 'companies.csv'
    saved = files.saver.save(data=companies, path=DATABASE_PATH.joinpath(file_name))
    results.append((file_name, saved))
    
    return results

def reindex_kpis():
    from anduril_kpi.models import KPI_DATA
    

    print('Original: ', KPI_DATA)
    data = dataframes.reindex(df=KPI_DATA, columns=['kpi_name']).reset_index()
    print('Reindexed: ',data)
    # file_name = 'kpi_data_reindexed.csv'

    # return files.saver.save(data=data, path=DATA_PATH.joinpath(file_name))
    return True



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

    # from anduril_kpi.models.kpi_tags import kpis_tags
    # print("KPIs List Tags: ", kpis_tags(return_type='list'))

    #Reindex on KPI name
    #reindexed = reindex_kpis()
    
    dbified = dbify()
    print('DBIfied: ', dbified)
