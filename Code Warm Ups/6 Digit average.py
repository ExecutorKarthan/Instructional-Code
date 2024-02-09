raw_input = input("What value do you want the average of the digits? ")

total_valu = 0
count = 0

for digit in raw_input:
    total_valu = int(digit)+ total_valu
    count = count + 1
    
print(total_valu/count)