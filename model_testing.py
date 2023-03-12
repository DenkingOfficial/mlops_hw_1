import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error, r2_score

TEST_DATA_PATH = "./test/polution_test.csv"

MODEL_NAME = "./polution_model.pkl"


def evaluate_model(test_data_path):
    df = pd.read_csv(test_data_path, delimiter=",", index_col="index")
    X_test = df.iloc[:, :-1]
    Y_test = df.iloc[:, -1]
    model = pickle.load(open(MODEL_NAME, "rb"))
    prediction = model.predict(X_test)
    mse = mean_squared_error(Y_test, prediction)
    msd = np.sqrt(mse)
    r2 = r2_score(Y_test, prediction)
    return f"Result metrics:\n\tMSE: {mse}\n\tMSD: {msd}\n\tR2: {r2}"


if __name__ == "__main__":
    print("Evaluating model:", end=" ")
    metrics = evaluate_model(TEST_DATA_PATH)
    print("Done")
    print(metrics)
