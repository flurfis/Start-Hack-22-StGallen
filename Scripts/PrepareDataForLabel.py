import pandas as pd

"""
    This method converts an sql table into a pandas dataframe and melts all the columns except the id
"""
def melt_table(sql_table):
    pd_table = pd.read_table(sql_table)
    pd.melt(pd_table, id_vars=[])
