import random

print("Hello what is your age?")
name = input()

print("Well, "+ name + ", I am thinking of a number between 1 and 20. ")
secret_Number = random.randint(1,20)
print("Take a guess")
guess = int(input())

guesses = 0
game_play = True
while game_play:
	if guesses > 2 and guess != secret_Number:
		print("Bad " + name + " the number i was thinking of is " + str(secret_Number))
		break
	else:	
		if secret_Number !=  guess and guess < secret_Number:
			print("You guess is too low. Try again")
			guess = int(input())
			guesses += 1
		if secret_Number !=  guess  and guess > secret_Number:
			print("Your guess is too high. Try again")
			guess = int(input())
			guesses += 1
		if guess == secret_Number:
			guesses += 1
			print("Good job, " +name+"! You guessed my number in " + str(guesses) + " guesse(s)")
			break
	
		