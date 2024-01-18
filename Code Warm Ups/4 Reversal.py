raw_input = input("What word do you want to reverse?")

result = ""

for current_letter in raw_input:
    result_letter = ""
    if current_letter.isupper():
        result_letter= current_letter.lower()
    else:
        result_letter= current_letter.upper()
    result = result_letter + result
    
print(result)