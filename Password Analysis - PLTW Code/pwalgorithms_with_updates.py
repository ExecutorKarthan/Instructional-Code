# Module pwalgorithms
import time

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password, original_start):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    start_time = time.time()
    guesses += 1
    if (w == password):
      return True, guesses
    end_time = time.time()
    print("")
    print(w + " has been completely searched.")
    print("It took " + str((end_time-start_time)/60) + " minutes to search.")
    print("It has been " + str((end_time-original_start)/60) + " minutes since the program began.")
    print("")
  return False, guesses

# analyze a two-word password
def two_word(password, original_start):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for first in words:
    start_time = time.time()
    for second in words:
      guesses += 1
      if ((first+second) == password):
        return True, guesses
    end_time = time.time()
    print("")
    print(first + " has been completely searched.")
    print("It took " + str((end_time-start_time)/60) + " minutes to search.")
    print("It has been " + str((end_time-original_start)/60) + " minutes since the program began.")
    print("")
  return False, guesses

# analyze a two-word password
def three_word(password, original_start):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for first in words:
    start_time = time.time()
    for second in words:
      for third in words:
        guesses += 1
        if ((first+second+third) == password):
          return True, guesses
    end_time = time.time()
    print("")
    print(first + " has been completely searched.")
    print("It took " + str((end_time-start_time)/60) + " minutes to search.")
    print("It has been " + str((end_time-original_start)/60) + " minutes since the program began.")
    print("")
  return False, guesses

# analyze a two-word password
def two_word_one_digit(password, original_start):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for first in words:
    start_time = time.time()
    for second in words:
      for value in range(0,10):
        guesses += 1
        if ((first+second+str(value)) == password):
          return True, guesses
    end_time = time.time()
    print("")
    print(first + " has been completely searched.")
    print("It took " + str((end_time-start_time)/60) + " minutes to search.")
    print("It has been " + str((end_time-original_start)/60) + " minutes since the program began.")
    print("")
  return False, guesses

