import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
make_guess = input('guess the letter- ').lower
print(chosen_word)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# if chosen_word==make_guess:
#   print('you guess correctly..')
# else:
#   print('sorry your wrong...')
for letter in chosen_word:
    if letter == make_guess:
        print("Right")
    else:
        print("Wrong")
