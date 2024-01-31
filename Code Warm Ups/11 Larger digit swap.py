raw_input = input("Enter your two digit value. ")
current_input = int(raw_input)
swapped_input = int(raw_input[1] + raw_input[0])

if swapped_input == current_input:
    print(True, " You cannot do better")
elif(swapped_input < current_input):
    print(True)
else: 
    print(False)

