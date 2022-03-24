import pandas as pd

"""
    This method converts an sql table into a pandas dataframe and melts all the columns except the id
"""
def pivot_table(sql_table):
    pd_table = pd.read_table(sql_table)
    result = pd_table['id']
    result.to_frame()

    for column in pd_table.columns[1:]:
        # temp_list = pd_table[1:idpd_table] + pd_table[idx + 1:]
        z = pd.pivot(pd_table, columns=column, values=column)

        z.reset_index(inplace=False)
        z.columns.name = None
        # print(z)
        # z.columns = [c[0] + c[1] for c in z.columns]
        # z.columns = [c[1] for c in z.columns]
        z = z.reset_index(drop=True)
        result = pd.concat([result, z], axis=1)

    #result.to_csv("result.csv", index=False)
    return result



def labelling(table_to_lable):
    lol = 5