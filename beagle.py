import random

NUM_DIGITS = 3
Max_guess = 20

def main():
    print('''Beagles is a guessing game . I think of an {}-digit number with no repeated digits 
          try to guess it .
          CLUES: 
          when i say::   that means ::
          PICO::          One digit is correct but in wrong position
          FERMI::         one digit is correct and in the right position 
          BEAGLES::       no digit is correct ''')
    while True:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(Max_guess))

        numGuess = 1
        while numGuess <= Max_guess:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}".format(numGuess))
                guess = input("Enter your guess (type 'exit' to quit): ")

                if guess.lower() == 'exit':
                    print("Thanks for playing.")
                    return
            clues = getClues(guess, secretNum)
            print(clues)
            numGuess += 1
            if guess == secretNum:
                break
            if numGuess > Max_guess:
                print("Ran out of guesses.")    
                print("The answer was {}.".format(secretNum))
                print('Do you want to play again? (yes or no)')
                if not input('>').lower().startswith('y'):
                    break 
                print("Thanks for playing.")

def getSecretNum():  
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it!"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('fermi')
        elif guess[i] in secretNum:
            clues.append("pico")
    if len(clues) == 0:
        return "beagles"
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
