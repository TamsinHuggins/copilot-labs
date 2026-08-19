import os
import pandas as pd

# Path resolved relative to this file so the app works from any working directory
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "spotify.csv")


def load_data():
    df = pd.read_csv(DATA_PATH, index_col=0)
    df = df.dropna()
    return df


def filter_by_genres(df, genres):
    return df[df["track_genre"].isin(genres)]


def get_genres(df):
    return sorted(df["track_genre"].unique().tolist())
