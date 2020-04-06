import pandas as pd


def convert(df, var):

    new_df = pd.DataFrame (columns=var)
    count = 0
    row = ()

    while count < len (df):
        if df.iloc[count, 0] == 'assettypenumber':
            if count != 0:
                new_df = new_df.append (dict(row), ignore_index=True)
            row = ()

        row += ((df.iloc[count, 0], df.iloc[count, 1]),)

        count += 1

        if count == len (df):
            new_df = new_df.append (dict(row), ignore_index=True)

    return new_df