import random
num=random.randrange(1,50)
guess=int(input("Guess the number : "))
chances_left=4

while guess!=num and chances_left>0:
    if guess > num:
        print("Your guess is greater")

        guess = int(input("Guess the number again : "))
        chances_left -=1

    elif guess < num:
        print("Your guess is smaller")
        guess = int(input("Guess the number again : "))
        chances_left -= 1

if guess==num:
        print("You win !!")

else:
        print("The correct number is : " + str(num))
        print("You lose")
