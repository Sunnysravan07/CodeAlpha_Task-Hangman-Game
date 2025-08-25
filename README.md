

Track guessed letters
Task 1: Hangman Game
Goal

Create a simple text-based Hangman game where the player guesses a word one letter at a time.

Project Scope

Use a small list of 5 predefined words

 Allow a maximum of 6 incorrect guesses

Run entirely in the console (text input/output only)

No graphics, audio, or external files/APIs

 Key Concepts Used

random module (for word selection)

while loop (to keep the game running)

if-else statements (to handle logic)

String and list operations (to manage guesses and display)

 How It Works

A random word is selected from a predefined list.

The player guesses one letter at a time.

If the guess is correct, the letter is revealed in its position(s).

If incorrect, the number of remaining attempts is reduced.

The game ends when:

The player correctly guesses all letters (Win 🎉)

The player runs out of attempts (Lose 💀)

 Example Word List
words = ["apple", "banana", "cherry", "grape", "mango"]

Sample Game Flow
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Correct!

Word: a _ _ _ _
Guess a letter: z
Incorrect! You have 5 attempts left.

...
 How to Run

Make sure you have Python installed.

Save the Python script (e.g., hangman.py).

Run it in your terminal:

python hangman.py

Future Improvements (Optional)

Add a hint system
Allow replaying the game

Support full word guessing
