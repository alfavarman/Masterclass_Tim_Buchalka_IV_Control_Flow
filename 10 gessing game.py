import random


# def get_integer(prompt):
#     while True:
#         temp = input(prompt)
#         if guess.isnumeric():
#             return int(temp)


guesses = 4
highest = 20
lotto = random.randint(1, highest)
print(lotto)        # TODO remove after testing
guess_index = 1
guess = 0
print("Guess the number in range from 1 to {}, "
                      "\n You can try up to {} times - first try "
                      ":\t".format(highest, guesses))

while guess != lotto:
    guess = int(input())

    if guess_index == guesses - 1:
        break
    if guess < lotto:
        guess_index += 1
        guess = int(input("Nop! Try higher number, left {} of {} guesses:\t".format(guess_index, guesses)))
    elif guess > lotto:
        guess_index += 1
        guess = int(input("Nop! Try lower number, left {} of {} guesses:\t".format(guess_index, guesses)))


if guess_index == guesses -1:
    guess = int(input("Your last chance:\t"))
    if guess == lotto:
        print("Great You got it!")
    else:
        print("Wrong. Game Over!")
        quit()


print("Correct! You have got it correctly at {} time!".format(guess_index))