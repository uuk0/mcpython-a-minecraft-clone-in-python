import math
import random
import pickle


def randint(seed, values):
    random.seed(pickle.dumps([seed] + [values]))
    return random.randint(0, 100000) / 100000


def choice(seed, data, list):
    return list[round(randint(seed, data))]
