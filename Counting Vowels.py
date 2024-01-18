input_raw = input(" What word do you want to submit to count its vowels?")
input_val = input_raw.lower()

vowel_count = 0
for letter in input_val:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        vowel_count = vowel_count + 1
        
print("The number of vowels in \"", input_raw, "\" is", vowel_count)