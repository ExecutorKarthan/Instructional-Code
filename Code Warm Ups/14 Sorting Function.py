sort_type = input("What kind of sort would you like? You can choose Asc, Des, or None" + "\n")

numbers = [2, 5, 1, 9, 11, 7, 24]

if(sort_type.lower() == "asc"):
    numbers.sort()
    print(numbers)
if(sort_type.lower() == "des"):
    numbers.sort()
    numbers.sort(reverse = True)
    print(numbers)
if(sort_type.lower() == "none"):
    print(numbers)
