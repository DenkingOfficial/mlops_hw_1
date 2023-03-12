import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

TRAIN_DATA_PATH = "./train/polution_train.csv"
TEST_DATA_PATH = "./test/polution_test.csv"


def get_columns_list(df, col_type=np.number):
    return df.select_dtypes(include=col_type).columns.tolist()


def prepare_data(df_full):
    df_local = df_full.copy()
    df_local = pd.get_dummies(
        df_local, columns=get_columns_list(df_local, col_type=object)
    )
    for col in get_columns_list(df_local):
        df_local[col] = MinMaxScaler().fit_transform(
            np.array(df_local[col]).reshape(-1, 1)
        )
    return df_local


if __name__ == "__main__":
    print("Preparing data:", end=" ")
    df_train = pd.read_csv(TRAIN_DATA_PATH, delimiter=",", index_col="index")
    df_test = pd.read_csv(TEST_DATA_PATH, delimiter=",", index_col="index")

    X_train = df_train.iloc[:, :-1]
    Y_train = df_train.iloc[:, -1]

    X_test = df_test.iloc[:, :-1]
    Y_test = df_test.iloc[:, -1]

    df_full = pd.concat([X_train, X_test])

    df_full = prepare_data(df_full)

    df_train = df_full.iloc[0:df_train.shape[0], :]
    df_test = df_full.iloc[df_train.shape[0]:, :]

    df_train = pd.concat([df_train, Y_train], axis=1)
    df_test = pd.concat([df_test, Y_test], axis=1)

    df_train.to_csv("./train/polution_train.csv")
    df_test.to_csv("./test/polution_test.csv")
    print("Done")
