import random
import maths


"""Debugging Exercise
The following code is intended to take a list of numbers, double each number, add a random integer between 1 and 3 to each doubled number,
and then store the results in a new list. However, there are several bugs in the code that prevent it from working correctly"""

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = math.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)


# mutate([1, 2, 3, 5, 8, 13])

"""Fixed Code"""

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
        print(b_list)


mutate([1, 2, 3, 5, 8, 13])
