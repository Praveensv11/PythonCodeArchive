import random

def number_guess():
    secret_num = random.randint(1, 100)

    print("Let's start the game")
    print("Guess the number between 1 - 100")

    while True:
        guess_num = int(input("Enter the Guess num: "))

        try:
            if guess_num < secret_num:
                print('Guess is too low')
            elif guess_num > secret_num:
                print('Guess is too high')
            else:
                print('Congratulation you guessed the number')
                break
        except TypeError:
            print('Enter number')

number_guess()

playAgain = input("Do you want to paly again? (yes/no)").lower()


if playAgain == "yes":
    number_guess()
else:
    print('Thanks for playing')