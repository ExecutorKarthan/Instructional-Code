list_to_sort = [1, 5, 2, 9, 11, 20, 4, 7]
total_length = len(list_to_sort)
current_value_index = 0
temp_holder = 0

while current_value_index+1 < total_length:
    current_val = list_to_sort[current_value_index]
    next_val = list_to_sort[current_value_index+1]
    if (list_to_sort[current_value_index] < list_to_sort[current_value_index+1]):
        current_value_index = current_value_index + 1
    else:
        temp_holder = list_to_sort[current_value_index+1]
        list_to_sort[current_value_index+1] = list_to_sort [current_value_index]
        list_to_sort [current_value_index] = temp_holder
        current_value_index = 0

print(list_to_sort)
        