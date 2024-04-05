from random_words_for_hangman import random_words
import random

guessed_word = random_words[random.randrange(len(random_words))].upper()
length_of_guessed = len(guessed_word)
lives = length_of_guessed
used_letters = ''
current_word = ['-']*length_of_guessed


while True:
    print(f'You have {lives} lives left and you used these letters: {used_letters}')
    print(f'Current word: ', end='')
    for letter in current_word:
        print(f'{letter} ', end='')
    
    user_letter = input('\n\nGuess a letter: ').upper()

    if user_letter in guessed_word:
        print('\n')
        for index in range(length_of_guessed):
            if user_letter == guessed_word[index]:
                current_word[index] = user_letter
    else:
        lives -= 1
        print(f'\nYour letter, {user_letter} is not in the word')

    if lives == 0:
        print(f'Sorry, you died. The word was {guessed_word}')
        break

    used_letters += f' {user_letter}'    