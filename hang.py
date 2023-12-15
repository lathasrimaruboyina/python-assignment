import random
def word_collection():
   
    words = ['student','cermony','minister','boat','tree','donkey','camel','lamp','chair','table','doll','mouse']
    return random.choice(words)

def word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
        display += ' '
    return display

def hangman():
    print("guessing a word")
    secret_word =  word_collection()
    guessed = []
    attempts = 5  

    while attempts > 0:
        print("\n" + word(secret_word, guessed ))
        if '_' not in word(secret_word, guessed):
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()
        guessed.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess! You have", attempts, "attempts left.")

    if attempts == 0:
        print("\nSorry, you're out of attempts. The word was:", secret_word)

hangman()
