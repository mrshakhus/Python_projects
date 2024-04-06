from random_words_for_hangman import random_words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    guessed_word = get_valid_word(random_words)
    lives = 7

    alphabet = set(string.ascii_uppercase)
    letters_from_guessed = set(guessed_word)
    used_letters = set()

    while letters_from_guessed != None or lives != 0:
        print(f'You have {lives} lives left and you used these letters:', ' '.join(used_letters))

        current_word_list = [letter if letter in used_letters else '-' for letter in guessed_word]
        print(f'Current word: ', ''.join(current_word_list))
        
        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in guessed_word:
                letters_from_guessed.remove(user_letter)
            
            else:
                lives -= 1
                print(f'Your letter, {user_letter} is not in the word')

        elif user_letter in used_letters:
            print('You already used that letter. Try another.')

        else:
            print("It's not a valid letter")

    if lives == 0:
        print(f'Sorry, you died. The word was {guessed_word}')
    else:
        print(f"Excelsior! You guessed it! It's {guessed_word}")
      
if __name__ == '__main__':
    hangman()