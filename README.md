# guess_number
Guess the number game using python 

This code is a simple number guessing game where the user needs to guess a randomly generated number between 1 and 50. Here's a breakdown of what the code does:

It imports the `random` module to generate a random number.

It uses `random.randrange(1,50)` to generate a random number between 1 and 50 and stores it in the variable `num`.

It prompts the user to guess the number using `int(input("Guess the number : "))` and stores the guess in the variable `guess`.

It initializes the variable `chances_left` to 4, representing the number of chances the user has to guess the correct number.

It enters a `while` loop that continues until the user correctly guesses the number or runs out of chances.

Inside the loop, it checks if the user's guess is greater or smaller than the random number and provides feedback accordingly.

It asks the user to guess again and decrements the `chances_left` variable.
If the user's guess is correct (guess == num), it prints "You win!!"; otherwise, it prints the correct number and "You lose."

In summary, the code generates a random number, allows the user to guess the number multiple times, provides feedback on each guess, and finally, informs the user whether they won or lost.
