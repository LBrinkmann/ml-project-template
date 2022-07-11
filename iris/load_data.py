import pandas as pd


def load_dataset(source, target_column, feature_columns):
    df = pd.read_csv(source)
    X = df[feature_columns].values
    y = df[target_column].values
    return X, y
