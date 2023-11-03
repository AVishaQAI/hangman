import random

word_list = ['Apple', 'Bananna', 'Grape', 'Orange', 'Peach']
word = random.choice(word_list)

def check_guess(guess):
    if guess in word:
        print('Good Guess')
    else:
        print(f'Sorry, {guess} is not in word. Try again')


def ask_for_input():
    while True:
        guess = input('Guess the fruit (enter the first letter only):\n').lower()  # Convert to lowercase for case-insensitive comparison
        if len(guess) == 1 and guess.isalpha():  # Check if the input is a single alphabetical character
            break
        else:
            print('Invalid input. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()

