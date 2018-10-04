import random
import pandas as pd
import os

DATASET = []


def load_dataset(func):
    """ Loads the dataset from the csv and puts it into the global variable DATASET"""
    def inner(*args):
        global DATASET

        if len(DATASET) == 0:
            current_file = os.path.abspath(os.path.dirname(__file__))
            csv_filename = os.path.join(current_file, 'abuse_en.csv')
            DATASET = pd.read_csv(csv_filename)['words'].values.tolist()
        return func(*args)
    return inner


@load_dataset
def listAbusesFrom(data_in):
    """ Returns list of abuses starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    words = [i for i in DATASET if i.lower().startswith(data_in.lower())]
    return words


@load_dataset
def randomAbuseFrom(data_in):
    """ Returns a random abuse starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    words = [i for i in DATASET if i.lower().startswith(data_in.lower())]
    if not words:
        return None
    return random.choice(words)


@load_dataset
def listAnyAbuse():
    """ Returns any random abuse from it's built-in dataset. """
    return random.choice(DATASET)


@load_dataset
def listAllAbuses():
    """ Just returns all the abusive words present in the dataset. """
    return list(DATASET)  # Cast to list to make a copy


__all__ = ('listAbusesFrom', 'randomAbuseFrom', 'listAllAbuses', 'listAnyAbuse')
