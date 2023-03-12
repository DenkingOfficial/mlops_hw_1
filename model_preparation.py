import pandas as pd
from sklearn.linear_model import Ridge
import pickle

TRAIN_DATA_PATH = "./train/polution_train.csv"

MODEL_NAME = "./polution_model.pkl"


def train_model(train_data_path):
    df = pd.read_csv(train_data_path, delimiter=",", index_col="index")
    X_train = df.iloc[:, :-1]
    Y_train = df.iloc[:, -1]
    model = Ridge(alpha=0.26)
    model.fit(X_train, Y_train)
    return model


if __name__ == "__main__":
    print("Training model:", end=" ")
    model = train_model(TRAIN_DATA_PATH)
    pickle.dump(model, open(MODEL_NAME, "wb"))
    print("Done")
