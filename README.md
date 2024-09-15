# BEAGLE_guessing_game
Here's a README file for your Beagles guessing game:

---

# Beagles Number Guessing Game

**Beagles** is a fun and interactive number-guessing game where the player tries to guess a secret number. The secret number has no repeated digits, and the player receives clues to guide their guesses.

## How the Game Works

1. The game thinks of a secret number with no repeated digits.
2. The player has a limited number of guesses to figure out the secret number.
3. After each guess, the game provides clues:
   - **PICO**: One digit is correct but in the wrong position.
   - **FERMI**: One digit is correct and in the right position.
   - **BEAGLES**: No digits are correct.

## Features

- The secret number is randomly generated with unique digits.
- Players get up to 20 guesses to figure out the number.
- The game provides clues to help players deduce the correct number.

## How to Play

1. **Start the game**: The game will generate a random 3-digit number (you can adjust the number of digits by changing the `NUM_DIGITS` variable in the code).
2. **Guess the number**: Enter a 3-digit guess. If the guess isn't 3 digits or contains non-numeric characters, you'll be prompted to try again.
3. **Receive clues**:
   - **PICO**: You guessed a correct digit, but it's in the wrong position.
   - **FERMI**: You guessed a correct digit in the right position.
   - **BEAGLES**: None of the digits in your guess are correct.
4. You have up to 20 guesses. If you run out of guesses, the game will reveal the secret number.
5. After a game ends, you can choose to play again or quit.

## Code Overview

The main components of the code are:

- **`main()`**: Handles the game logic, prompts the player for input, and checks guesses.
- **`getSecretNum()`**: Generates a random secret number with unique digits.
- **`getClues()`**: Provides clues based on the player's guess and the secret number.

### Example Gameplay

```bash
Beagles is a guessing game. I think of a 3-digit number with no repeated digits.
Try to guess it.
CLUES: 
When I say:           That means:
PICO                  One digit is correct but in the wrong position
FERMI                 One digit is correct and in the right position
BEAGLES               No digit is correct

I have thought up a number.
You have 20 guesses to get it.
Guess #1
Enter your guess (type 'exit' to quit): 123
fermi pico
Guess #2
Enter your guess (type 'exit' to quit): 456
beagles
Guess #3
Enter your guess (type 'exit' to quit): 312
pico pico pico
```

### Adjusting the Difficulty

- **Change the number of digits**: Modify the `NUM_DIGITS` variable to set a different length for the secret number (e.g., 4-digit or 5-digit numbers).
- **Change the number of guesses**: Adjust the `Max_guess` variable to increase or decrease the number of allowed guesses.

## Requirements

- Python 3.x

## How to Run

1. Save the script to a file (e.g., `beagles_game.py`).
2. Run the script:
   ```bash
   python beagles_game.py
   ```

## License

This project is open-source and free to use.

---

