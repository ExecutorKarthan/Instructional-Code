raw_input = input("Enter a 9 numbers no smaller than 1 and no greater than 10. There can be no repeates and must be seperated by spaces.")
processed_input = raw_input.split(" ")

num_list = []
reference_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for value in processed_input:
    num_list.append(int(value))

num_sum = 0
ref_sum = 0

for val in num_list:
    num_sum += val

for val in reference_list:
    ref_sum += val

print("Your missing value is:",(ref_sum-num_sum))