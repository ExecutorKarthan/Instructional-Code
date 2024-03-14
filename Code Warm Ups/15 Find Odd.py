data_set = [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]
#[1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
result = "All values are even"
stored_vals = {}
data_set.sort()

for value in data_set:
    if value in stored_vals:
        stored_vals[value] += 1
    else:
        stored_vals[value] = 1
        
for value in stored_vals:
    if stored_vals[value]%2 == 1:
        result = "The odd counted value is " + str(value) + " with a count of " + str(stored_vals[value])
        break
    else:
        pass

print(result)