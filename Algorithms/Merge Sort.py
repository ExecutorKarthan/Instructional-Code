import random

def make_list():
    list = []
    while len(list) < 10:
        rand_val = random.randint(-200, 200)
        list.append(rand_val)
    return list
   
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
   
random_list = make_list()
print(random_list)
print(merge_sort(random_list))