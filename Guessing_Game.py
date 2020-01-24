
# GUESSING GAME

# secret word
secret_word = "antelope"

# empty variable to store guesses
guess = ""

# How many times the user has guessed
guess_count = 0

# Limit of Guesses
guess_limit = 3

#Boolean to toggle out of guesses
out_of_guesses = False


# if guess is = secret word, then User wins
# if not, then loop through until user loses.

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        # increment guess count by 1
        guess_count += 1
    else:
        out_of_guesses = True


# Success Message
if out_of_guesses:
    print("Out of Guesses, You Lose")
else:
    print("Correct Answer!")
