import random

DATASET_FILENAME = "dataset.txt"
DATASET = []

def loadDataSet():
    """ Loads the dataset from dataset.txt into memory.
        Dataset created by scrapping https://www.noswearing.com/dictionary/ """
    with open(DATASET_FILENAME, "r") as dsFile:
        for profanity in dsFile.readlines():
            DATASET.append(profanity.replace("\n", ""))

def listAbusesFrom(data_in):
    """ Returns list of abuses starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    words = [i for i in DATASET if i.lower().startswith(data_in.lower())]
    return words

def randomAbuseFrom(data_in):
    """ Returns a random abuse starting from a specific letter provided in argument of the function. """
    if not isinstance(data_in, str):
        raise ValueError("data_in must be a string")

    words = [i for i in DATASET if i.lower().startswith(data_in.lower())]
    if not words:
        return None
    return random.choice(words)

def listAnyAbuse():
    """ Returns any random abuse from it's built-in dataset. """
    return random.choice(DATASET)

def listAllAbuses():
    """ Just returns all the abusive words present in the dataset. """
    return list(DATASET)  # Cast to list to make a copy

loadDataSet()

__all__ = ("listAbusesFrom", "randomAbuseFrom", "listAllAbuses", "listAnyAbuse")
