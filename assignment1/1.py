from random import randint

print("I picked a number between 0 and 20, endpoints included. Guess it!")
pick = randint(0, 20)

bingo = False

while not bingo:
	guess = int(input("Your guess: "))
	if guess > pick:
		print("Pick a lower number!")
	elif guess < pick:
		print("Pick a higher number!")
	else:
		print("Your guess is correct!")

	bingo = guess == pick
