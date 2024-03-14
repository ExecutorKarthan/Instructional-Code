data = ["a", "a", "a", "b"]
sort_value = "a"

front_list = []
end_list = []

for value in data:
    if value == sort_value:
        end_list.append(value)
    else:
        front_list.append(value)
        
print(front_list + end_list)