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
def linear(found, target_word, result_word):
  words = get_dictionary()
  words.sort()
  guesses = 0
  for word in words:
    guesses += 1
    if (word == target_word):
      result_word = word
      found = True
      return found, guesses, result_word
  return found, guesses, result_word

def binary(found, target_word, result_word):
  words = get_dictionary()
  words.sort()
  guesses = 0
  left_boundary = 0
  right_boundary = len(words)-1
  while (guesses < 50 and (right_boundary - left_boundary) != 1):
    mid_position = int((right_boundary - left_boundary)/2) + left_boundary
    if(target_word < words[mid_position]):
      right_boundary = mid_position
    else:
      left_boundary = mid_position
    guesses += 1
  result_word = words.pop(left_boundary)
  if (result_word == target_word):
    found = True
  else:
    found = False
  return found, guesses, result_word


