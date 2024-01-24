# Module pwalgorithms

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
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a two-word password
def two_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    for word in words:
      guesses += 1
      if (w+word == password):
        return True, guesses
  return False, guesses
