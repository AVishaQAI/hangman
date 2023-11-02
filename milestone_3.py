import random

word_list = ['Apple', 'Bananna', 'Grape', 'Orange', 'Peach']
word = random.choice(word_list)

while True:
    guess = input('Guess the fruit (enter the first letter only):\n').strip().lower()  # Convert to lowercase for case-insensitive comparison

    if len(guess) == 1 and guess.isalpha():  # Check if the input is a single alphabetical character
        break
    else:
        print('Invalid input. Please, enter a single alphabetical character.')

if guess.lower() in word.lower():
    print('Good Guess')
else:
    print(f'Sorry, {guess} is not the first letter of the word. Try again')

