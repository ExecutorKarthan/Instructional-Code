# a213_pw_analyzer.py
import time
import pwalgorithms_with_updates as pwa

def validated_input():
    try:
        selection = int(input("What would you like to select? Please just type in a numerical value" +"\n"
                        + "1 - Break a 1 word password" + "\n"
                        + "2 - Break a 2 word password" + "\n"
                        + "3 - Break a 3 word password" + "\n"
                        + "4 - Break a 2 word and digit password" + "\n"
                        + "5 - Exit" + "\n"))
        return selection
    except:
        print("Invalid entry. Please use a 1, 2, or 3 to make a selection.")
        
def pw_break(selection):
  time_start = time.time()
  # attempt to find password
  if(selection == 1):
    found, num_guesses = pwa.one_word(password, time_start)
  if(selection == 2):
    found, num_guesses = pwa.two_word(password, time_start)
  if(selection == 3):
    found, num_guesses = pwa.three_word(password, time_start)
  if(selection == 4):
    found, num_guesses = pwa.two_word_one_digit(password, time_start)
  time_end = time.time()
  # report results
  if (found):
    print(password, "found in", num_guesses, "guesses")
  else: 
    print(password, "NOT found in", num_guesses, "guesses!")
  print("Time:", format((time_end-time_start), ".8f"))
  print("")

run = True
while(run):
    selection = validated_input()
    if(selection == 5 ):
        run = False
        break
    password = input("Enter password:")
    if(selection == 1 ):
        print("Analyzing a one-word password ...")
        pw_break(selection)
    if(selection == 2 ):
        print("Analyzing a two-word password ...")
        pw_break(selection)
    if(selection == 3 ):
        print("Analyzing a three-word password ...")
        pw_break(selection)
    if(selection == 4 ):
        print("Analyzing a two-word and one-digit password ...")
        pw_break(selection)
