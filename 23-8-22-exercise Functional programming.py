# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalized(name):
    return name.capitalize()


print(list(map(capitalized, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

zipped_list = list(zip(my_strings, my_numbers))


# Sorting list of tupple according to thr key
def middle(tup):
    return tup[1]


# function to sort the tuple
def sort(list_of_tuples):
    return sorted(list_of_tuples, key=middle)


print(sort(zipped_list))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def score_over_50_per(score):
    return score > 50


print(list(filter(score_over_50_per, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
from functools import reduce

new_list = my_numbers + scores


def sum_of_list(acc, item):
    return acc + item


print(reduce(sum_of_list, new_list, 0))
