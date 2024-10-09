# a213_pw_analyzer.py
import time
import pwalgorithms as pwa

function_used = input("Would you like a linear search or a binary search?  ")
target_word = input("What word are you looking for?  ")
result_word = ''
found = False

print("Analyzing ...")
time_start = time.time()

if(function_used == "linear"):
  found, num_guesses, result_word = pwa.linear(found, target_word, result_word)
else:
  found, num_guesses, result_word = pwa.binary(found, target_word, result_word)
time_end = time.time()

if (found):
  print(result_word, "found in", num_guesses, "guesses")
else: 
  print(result_word, "NOT found in", num_guesses, "guesses!")
print("Time:", format((time_end-time_start), ".8f"))