import pandas as pd

# This file aims to correct the datatype of the converted csv DataFrame in order to plot and analyze easier.


def print_type(csv: str) -> list:
    '''
    Takes a string name of csv file and identifies the type of data present. Used in order to manipulate the dataframe to have the correct datatypes.
    :param csv: string name of csv file
    :return: list of tuples with column name, and type
    '''
    spd = pd.read_csv(csv)
    type_list = []
    for i in spd.columns:
        type_list.append((i,type(spd[i][0])))
    return type_list




x = print_type("starcraft_player_data.csv")
print(x)