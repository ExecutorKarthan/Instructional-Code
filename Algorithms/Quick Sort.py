import random

def make_list():
    list = []
    while len(list) < 10:
        rand_val = random.randint(-200, 200)
        list.append(rand_val)
    return list
   
def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    
random_list = make_list()
print(random_list)
print(quick_sort(random_list))