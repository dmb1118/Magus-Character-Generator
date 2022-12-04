import random
from traits_flaws import *
import os.path
import pickle


def rng(num):
    return random.randint(1, num)


def selector(prompt, min_num, max_num):
    valid = False
    while not valid:
        try:
            var = int(input(prompt))
        except TypeError as err:
            print(err)
            continue
        except ValueError as err:
            print(err)
            continue
        if min_num <= var <= max_num:
            return var
        else:
            continue


def trait_list():
    for key in traits_dict:
        print("-" * 25)
        print(key + " : " + traits_dict[key])


def unpickle_char():
    path = (os.getcwd() + "/pickles/")
    pickles = []
    for obj in os.listdir(path):
        f = os.path.join(path, obj)
        if os.path.isfile(f):
            pickles.append(f)
    num = 1
    for obj in pickles:
        print(f"{num}. {obj}")
        num += 1
    var = int(input("Please enter the corresponding number to the save file you wish to load\n"))
    with open(pickles[var - 1], 'rb') as inp:
        obj = pickle.load(inp)
    return obj


def str_input(prompt):
    x = ""
    try:
        x = str(input(prompt))
    except ValueError as err:
        print(err)
    return x
