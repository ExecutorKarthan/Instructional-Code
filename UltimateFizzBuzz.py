def FizzBuzz(options, min_range, max_range):
    for x in range(min_range, max_range):
        print_string = ""
        for index, key in enumerate(options):
            if x % key == 0:
                print_string += str(options[key])
            if x / key > 0 and index == len(options) -1 and print_string == "":
                print_string = str(x)
        print(print_string)
            
min_range = int(1)
max_range = int(101)
options_dict = {3:"fizz", 4:"buzz", 7:"doot", 11: "bata"}
FizzBuzz(options_dict, min_range, max_range)