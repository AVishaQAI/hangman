import random

word_list= ['Apple', 'Bananna', 'Grape', 'Orenge', 'Peach']
word = random.choice(word_list)

guess = input('Guess the fruit (enter the first letter only):\n')

if len(guess)== 1:
    print('Good Guess')
else:
    print('Oops! That is not a valid input')
print(word_list)
print(word)
print(guess.upper())

