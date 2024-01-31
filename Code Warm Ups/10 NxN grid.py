raw_input = input("Enter your value. ")
processed_input = int(raw_input)

def process_grid(max_size):
    if max_size == 1:
        return 1
    else:
        return max_size**2 + process_grid(max_size-1)

print("The number of squares in", processed_input, "is", process_grid(processed_input))