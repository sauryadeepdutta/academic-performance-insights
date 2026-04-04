def load_data(path):
    import pandas as pd
    return pd.read_csv(path)


def check_missing(df):
    return df.isnull().sum()


def basic_stats(df):
    return df.describe()