raw_input = input("Which triangle is this? ")
processed_input = int(raw_input)

def dot_count(val):
    if val == 0:
        return val
    else:
        return val + dot_count(val-1)
    
print("For triangle", raw_input, "there are" , dot_count(processed_input), "dots.")
