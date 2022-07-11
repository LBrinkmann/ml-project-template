import pandas as pd


def add_labels(df, labels):
    label_df = pd.DataFrame(data=labels, dtype='category', index=df.index)
    return pd.concat([label_df, df], axis=1)
