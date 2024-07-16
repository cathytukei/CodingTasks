import random

def guess_number(number_range, tries):
  """
  This function implements a number guessing game.

  Args:
      number_range: Tuple representing the lower and upper bound of the guessing range (inclusive).
      tries: Integer representing the number of allowed guesses.
  """
  secret_number = random.randint(number_range[0], number_range[1])
  guesses_left = tries

  while guesses_left > 0:
    guess = int(input(f"You have {guesses_left} guesses left. Enter a number between {number_range[0]} and {number_range[1]}: "))
    guesses_left -= 1

    if guess == secret_number:
      print("Congratulations! You guessed the number!")
      break
    elif guess < secret_number:
      print("Too low, try again!")
    else:
      print("Too high, try again!")

  if guesses_left == 0:
    print(f"Sorry, you ran out of guesses. The secret number was {secret_number}.")

# Example usage with range 1 to 10 and 5 tries
guess_number((1, 10), 5)
