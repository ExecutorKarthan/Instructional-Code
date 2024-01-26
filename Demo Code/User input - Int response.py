loop = True
loop_count = 0
while(loop):
    raw_input = input("Give me a number? \n")
    try:
        processed_value = int(raw_input)*5
        print(processed_value)
        loop = False
    except:
        print("No dummy! You need to enter a numeric value, not a linguisitc value.")
        loop_count += 1
        if(loop_count > 5):
            print("Wow. Ultra stupid")
            loop = False
