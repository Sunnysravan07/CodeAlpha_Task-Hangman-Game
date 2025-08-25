import random

words = ["apple", "banana", "cherry", "grape", "mango"]

word = random.choice(words)
guessed = ["_"] * len(word)  
attempts = 6  
guessed_letters = []  

print(" Welcome to Hangman Game!")
print("Word: ", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(" You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f" Wrong guess! Attempts left: {attempts}")

    print("Word: ", " ".join(guessed))
    
if "_" not in guessed:
    print(" You won! The word was:", word)
else:
    print(" Game Over! The word was:", word)