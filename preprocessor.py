import pandas as pd


def preprocess(df, region_df):
    #filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merging with region dataset
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates value from the dataframe
    df.drop_duplicates(inplace=True)
    # One Hot Encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)
    return df
