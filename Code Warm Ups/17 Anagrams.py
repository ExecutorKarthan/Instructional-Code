word_1 = "Horsasde"
word_2 = "erssesoh"

stack = [*word_1.lower()]

stack.sort()

reference = [*word_2.lower()]

reference.sort(reverse=True)

print(stack)

print(reference)

for letter in reference:
    if letter not in reference:
        break
    else:
        if(letter == stack[len(stack)-1]):
            stack.pop()
if(len(stack) == 0):
    print("They are anagrams")
else:
    print("Not anagrams")