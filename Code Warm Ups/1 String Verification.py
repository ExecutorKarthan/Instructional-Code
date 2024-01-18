def string_verification(val1, val2):
    if(val1.lower() == val2.lower()):
        print("Your values are the same!")
    else:
        print("These values are different!")

cont_val = True

while(cont_val):

    initial_val = input("What is the first value? ")
    test_val = input("What is the second value? ")

    string_verification(initial_val, test_val)

    end_val = input("Do you want to continue? Yes(Y) or No(N)    ")
    if(end_val.lower() == "n" or end_val.lower() == "no"):
        cont_val = False