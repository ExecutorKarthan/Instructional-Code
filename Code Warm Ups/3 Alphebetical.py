raw_input = input("What word do you want to reverse?")

processed_input = []

for letter in raw_input:
    processed_input.append(letter)

processed_input.sort()
print(processed_input)

