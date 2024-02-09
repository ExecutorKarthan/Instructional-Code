import re
import math

def generate_binary(val, power):
    if power == 0:
        return str(val)
    else:
        temp_val = val - 2**power
        if temp_val > 0:
            val = temp_val
            return "1" + generate_binary(val, power-1)
        else:
            return "0" + generate_binary(val, power-1) 
        
def generate_decimal(valueStr):
    result = 0
    base_power = len(valueStr)-1
    for letter in valueStr:
        if letter == "0":
            base_power = base_power - 1
        else:
            result = result + 2**base_power
            base_power = base_power - 1
    return result

raw_input = input("What value are you entering to be converted?")

its_numers = re.compile("\d+").search(raw_input)

if(its_numers):
    its_decimal = re.compile("^[^0][2-9]+")
    input_num = int(raw_input)
    if(its_decimal.search(raw_input)):
        power = math.ceil(math.log(input_num, 10)/math.log(2, 10))
        binary_string = generate_binary(input_num, power)
        print(binary_string)
    else:
        decimal_string = generate_decimal(raw_input)
        print(decimal_string)