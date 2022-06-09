from pandas import DataFrame


def gerarDicionarioDoDataFrame(df: DataFrame, chave, valor):
    dd = {}
    for i, cc in enumerate(df[chave]):
        dd[cc] = df[valor][i]
    return dd