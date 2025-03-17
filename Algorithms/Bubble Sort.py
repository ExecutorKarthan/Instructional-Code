import random

def make_list():
    list = []
    while len(list) < 10:
        rand_val = random.randint(-200, 200)
        list.append(rand_val)
    return list

def bubble_sort(list):
    for first_index in range(len(list)-1, len(list)):
        for second_index in range(len(list)):
            if(list[first_index] < list[second_index]):
                temp = list[first_index]
                list[first_index] = list[second_index]
                list[second_index] = temp
    return list               
    
random_list = make_list()
print(random_list)
print(bubble_sort(random_list))