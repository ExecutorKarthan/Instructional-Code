raw_input = input("What value do you want to add the digits of?")

total_valu = 0.0
count = 0

for digit in raw_input:
    total_valu = float(digit)+ total_valu
    count = count + 1
    print(total_valu, count)
    
print(total_valu/count)