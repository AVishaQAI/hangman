import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list= word_list
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good Guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    if self.word_guessed[i] == '-':
                        self.num_letters -= 1
                        self.word_guessed[i] = guess
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in word")
            print(f"You have {self.num_lives} left")
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) !=1:
                print("Invalid Letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
hangman = Hangman(["apple", "bananna", "pair"])
hangman.ask_for_input()