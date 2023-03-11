import gdown
import pandas as pd
import os
from sklearn.model_selection import train_test_split

DATASET_LINK_ID = "1HM0UY2YSIyDw4_WPwoatGp-3YF4jzt2W"
OUTPUT_PATH = "./polution_dataset.csv"
OUT = ["train", "test"]


def download_dataset(link_id, output_path):
    gdown.download(
        f"https://drive.google.com/uc?id={link_id}", output_path, quiet=True
    )


def main(out):
    download_dataset(DATASET_LINK_ID, OUTPUT_PATH)
    df = pd.read_csv(OUTPUT_PATH, delimiter=",", index_col="index")
    frames = train_test_split(df, test_size=0.2)
    for name, frame in zip(out, frames):
        if not os.path.exists(f"./{name}"):
            os.makedirs(name)
        frame.to_csv(f"./{name}/polution_{name}.csv")
    os.remove(OUTPUT_PATH)


if __name__ == "__main__":
    print("Dowloading dataset:", end=" ")
    main(OUT)
    print("Done")
