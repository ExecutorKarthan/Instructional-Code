import re
expression = re.compile('[A-Za-df-z]')
random_string = "Nolan is the worst at everything execpt being Nolan."
print(random_string)
index_list = ""
for index in range(0, len(random_string)):
    index_list += str(index)
# print(index_list)
#string[start index : end index : index you are moving by]
# print(random_string[10:20])
# print(random_string[10:20:2])
# print(random_string[10:20:4])
# print(random_string[10:20:-1])
# print(random_string[len(random_string):0:-1])
# print(random_string.upper())
# print(random_string.lower())
print(random_string[0:6] + random_string[6:9] + "best")
print(expression.findall(random_string))