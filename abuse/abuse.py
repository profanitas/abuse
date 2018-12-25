__all__ = ('list_abuses_from', 'random_abuse_from', 'list_all_abuses', 'random_abuse')

import bisect
import csv
import itertools
import os
import random

_DATASET = None

DATASET_FILENAME = 'abuse_en.csv'


def get_dataset():
    global _DATASET

    if _DATASET is None:
        _DATASET = sorted(set(load_dataset()))
    return _DATASET


def load_dataset():
    with open(_file_full_path(DATASET_FILENAME), newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # headers
        return (r[0].strip().lower() for r in list(reader) if r[0].strip())


def dump_dataset(filename=None):
    filename = filename or DATASET_FILENAME

    with open(_file_full_path(filename), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow(['words'])
        for w in get_dataset():
            writer.writerow([w])


def list_abuses_from(first_letter):
    """ Returns list of abuses starting from a specific letter provided in argument of the function. """
    if not (isinstance(first_letter, str) and first_letter.isalpha() and len(first_letter) == 1):
        raise ValueError("argument must be a letter")
    first_letter = first_letter.lower()

    dataset = get_dataset()
    index_first = bisect.bisect_left(dataset, first_letter)
    return list(itertools.takewhile(lambda w: w.startswith(first_letter), dataset[index_first:]))


def random_abuse_from(first_letter):
    """ Returns a random abuse starting from a specific letter provided in argument of the function. """
    words = list_abuses_from(first_letter)
    return random.choice(words) if words is not None else None


def random_abuse():
    """ Returns any random abuse from it's built-in dataset. """
    return random.choice(get_dataset())


def list_all_abuses():
    """ Just returns all the abusive words present in the dataset. """
    return get_dataset().copy()


def _file_full_path(filename):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_dir, filename)


load_dataset()
