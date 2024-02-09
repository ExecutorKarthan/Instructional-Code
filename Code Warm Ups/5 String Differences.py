raw_input1 = input("What is your first word?")
raw_input2 = input("What is your second word?")

index = 0
count = 0

max_length = 0
num_remain = 0

if(len(raw_input1) > len(raw_input2)):
    max_length = len(raw_input2)
    num_remain = len(raw_input1) - len(raw_input2)
else:
    max_length = len(raw_input1)
    num_remain = len(raw_input2) - len(raw_input1)

while(index < max_length):
    if(raw_input1[index] != raw_input2[index]):
        count = count + 1
    index = index + 1

result = num_remain + count
print(result)