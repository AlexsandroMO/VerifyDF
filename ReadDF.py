import pandas as pd

def describe_df(df):
    len_df = ['QT_Lines Data Frame', len(df)]
    len_col_df = ['QT_Col Data Frame', len(df.columns)]
    name_col_df = []
    for a in df.columns:
        name_col_df.append(a)

    var_max = []
    for b in name_col_df:
        var_max.append([b, df[b].max()])

    print('[ Len Maxima por Coluna ]')
    for a in var_max:
        print(a)

    print('\n')

    var_min = []
    for b in name_col_df:
        var_min.append([b, df[b].max()])

    print('[ Len Mínima por Coluna ]')
    for a in var_min:
        print(a)

    print('\n')

    read_all = [len_df, len_col_df]

    for a in read_all:
        print(a)