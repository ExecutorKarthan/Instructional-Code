import random

def make_list():
    list = []
    while len(list) < 10:
        rand_val = random.randint(-200, 200)
        list.append(rand_val)
    return list
   
def insertion_sort(list):
    for index in range(1, len(list)):
        value_being_sorted = list[index]
        list_position = index - 1
        while list_position >=0 and value_being_sorted < list[list_position]:
            list[list_position + 1] = list[list_position]
            list_position -= 1
            list[list_position+1] = value_being_sorted
    return list
    
random_list = make_list()
print(random_list)
print(insertion_sort(random_list))