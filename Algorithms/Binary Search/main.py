# a213_pw_analyzer.py
import time
import search_algorithms as search

function_used = input("Would you like a linear search or a binary search?  ")
target_word = input("What word are you looking for?  ")
result_word = ''
num_guesses = 0
missing_part = ""

print("Analyzing ...")
time_start = time.time()

if(function_used == "linear"):
  try:
    target_word.index(" ")
    word_to_process = target_word.split(" ")
    for word in word_to_process:
      found = False
      temp_guesses = 0
      temp_result_word = ""
      found, temp_guesses, temp_result_word = search.linear(found, word, result_word)
      if(found == False):
        missing_part = word
        break 
      num_guesses += temp_guesses
      if(temp_result_word == word_to_process[len(word_to_process)-1]):
        result_word += temp_result_word
      else:
        result_word += temp_result_word + " "
  except:
    found, num_guesses, result_word = search.linear(found, target_word, result_word)
else:
  try:
    target_word.index(" ")
    word_to_process = target_word.split(" ")
    for word in word_to_process:
      found = False
      temp_guesses = 0
      temp_result_word = ""
      found, temp_guesses, temp_result_word = search.binary(found, word, result_word)
      if(found == False):
        missing_part = word
        break 
      num_guesses += temp_guesses
      if(temp_result_word == word_to_process[len(word_to_process)-1]):
        result_word += temp_result_word
      else:
        result_word += temp_result_word + " "
  except:
    found, num_guesses, result_word = search.binary(found, target_word, result_word)
time_end = time.time()

if (found):
  print(target_word, "found in", num_guesses, "guesses.")
else: 
  print(target_word, "NOT found in", num_guesses, "guesses! The missing part was " + missing_part)
print("Time:", format((time_end-time_start), ".8f"))