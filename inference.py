# from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
from sklearn import preprocessing


def preprocessing_csv(df):

    x = df.values  # returns a numpy array
    std_scaller = preprocessing.StandardScaler()
    x_scaled = std_scaller.fit_transform(x)
    df = pd.DataFrame(x_scaled, columns=df.columns, index=df.index)
    return df
