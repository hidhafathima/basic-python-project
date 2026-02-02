print("Welcome to the Number Guessing game!")
import random
random.randint(1,10)
secret_number = random.randint(1,10)
guess=int(input("Enter your guess:"))
attempt=1
while guess!=secret_number:
   
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    guess=int(input("Enter your guess:"))
    attempt=attempt+1


print("Congratulations!You guessed the correct number")
print("You guessed it in ",attempt,"attempts")