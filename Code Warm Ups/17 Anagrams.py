word_1 = "racecar"
word_2 = "carrace"

stack = [*word_1.lower()]

stack.sort()

reference = [*word_2.lower()]

reference.sort(reverse=True)

print(stack)

print(reference)

for letter in reference:
    if letter not in stack:
        break
    else:
        if(letter == stack[len(stack)-1]):
            stack.pop()
if(len(stack) == 0):
    print("They are anagrams")
else:
    print("Not anagrams")