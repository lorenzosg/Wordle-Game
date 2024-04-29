#!/usr/bin/env python
# coding: utf-8

# In[78]:


#Top down strategy of wordle
import random
import colorama
from colorama import Back

turns = 0 
guess = 'guess'
file = open('wordle.txt')
file = file.read()
words = file.split('\n')

#1. State the rules of the game
def rules():
    print('You are trying to guess a five letter word which I have randomly selected')
    print('You have 6 guesses, and all guesses must be words found in the dictionary')
    print('You may only guess 5 letter words')
    print('If the tile of the letter turns green, it belongs to the word in the same location specified in the guess')
    print('If the tile of the letter turns yellow, the letter is in the word, but not in the location specified in the word which you guessed')
    print("If the color of the tile is white, then the letter is not in the word")

#2. Play the game 

def select_word():
    word = random.sample(words, 1)
    return word

def print_green(letter):
    print(Back.GREEN + f" {letter} " + Back.RESET, end='')
    
def print_yellow(letter):
    print(Back.YELLOW + f" {letter} " + Back.RESET, end='')

def print_white(letter):
    print(Back.WHITE + f" {letter} " + Back.RESET, end='')
    
def check_word(guess = 'guess', word = 'word'):
    result = []
    for ch, ch2 in zip(guess, word):
        if ch in word:
            if ch == ch2:
                result.append('green')
            else: 
                result.append('yellow')
                
        else: 
            result.append('black')
            

    return result
                

def outcome(outcome = 'outcome', turn = 'turns', word = 'word'):
    if outcome.count('green') == 5:
        print(f"Congratulations, you guessed the word '{word}' correctly!")
    if outcome.count('green') != 5:
        print(f"So close, but you're out of guesses, the word was '{word}', play again to see if you can get the next one!")
    

    
def is_valid(guess = 'guess', words = 'words'):
    length = True
    english = True
    if len(guess) != 5:
        print('I only accept 5 letter words. Pease try again')
        length = False
    if (len(guess) == 5) and (guess not in words):
        print('That word is not in the dictionary. Please Try again')
        english = False
    if (length +english) == 2:
        return 1
    else:
        return 0
    
    

def play_wordle(guess ='guess', turns = turns):
    rules()
    word = select_word()
    word = word[0]
    while(guess != word and turns < 6):
        guess = input('Enter a 5 letter word ')
        valid = is_valid(guess, words)
        turns += valid
        if valid == 1:
            colors = check_word(guess, word)
            print(f'guess {turns}/6: {guess}')
            for ch, col in zip(guess, colors):
                if col == 'green':
                    print_green(ch)
                if col == 'yellow':
                    print_yellow(ch)
                if col == 'black':
                    print_white(ch)
    outcome(colors, turns, word)


#3. Inform the player of outcome

play_wordle()

