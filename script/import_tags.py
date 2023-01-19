from ast import literal_eval
import pandas as pd
import numpy as np

from recipes.models.tag import Tag

def append_unique_values(df, column_name, target_array):
    column = df[column_name].apply(literal_eval).values
    target_array = np.unique(np.concatenate(column).ravel())

    return target_array


def import_tags(file_path):
    df = pd.read_csv(file_path)

    target_array = []

    target_array = append_unique_values(df, 'tags', target_array)

    for item in target_array:
        tag = Tag()

        tag.name = item
        tag.save()

TAG = "/Users/alessandrotisi/Downloads/RAW_recipes.csv"

import_tags(TAG)