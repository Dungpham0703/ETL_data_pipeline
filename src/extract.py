from datasets import load_dataset
import pandas as pd

def extract_data():
    dataset = load_dataset("ashraq/movielens_ratings")
    return dataset["train"].to_pandas()
