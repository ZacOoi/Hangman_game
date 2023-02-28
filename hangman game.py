import random
list_of_words = ['pizza', 'tree', 'bicycle']

secret_word = random.sample(list_of_words, 1)[0]
secret_letters = list(secret_word.lower())
guessed_letters = list('_'*len(secret_word))

def find(word, guessed_letter):
    correct_indices = [i for i, x in enumerate(word) if x == guessed_letter]
    return correct_indices

def correct_guesses(guess):
     for i in find(secret_word, guess):
         guessed_letters[i] = guess
     return guessed_letters

def hangman():
    num_guesses = 0
    max_guesses = 6
    print('this is the word ' + ''.join(guessed_letters) + ' it has ' + str(len(secret_word)) + ' letters!')
    while num_guesses < max_guesses and guessed_letters != secret_letters:
        guess = input('guess a letter').lower()
        if len(guess) < 1:
            print('Hey enter something')
        elif len(guess) > 1:
            print('Hey only one letter at a time')
        elif guess.isalpha() == False:
            print('Hey letters only!')
        elif guess not in secret_letters:
            num_guesses += 1
            print('Sorry, that is not one of the letters. ' + 'You now have ' + str(max_guesses - num_guesses) + ' guesses left')
        else:
            if guess in secret_letters:
                correct_guesses(guess)
            print('Good guess! Here is the word now: ' + ''.join(guessed_letters))
    if num_guesses == max_guesses:
        print('Game over, you lose. The word was ' + secret_word)
    else:
        print('Congratulations you are a genius, you beat me! You guessed the word! It is ' + secret_word)

hangman()


