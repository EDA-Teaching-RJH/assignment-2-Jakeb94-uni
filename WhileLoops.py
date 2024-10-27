import random
correctnumber = random.randint(1, 100)
print("It's The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guess = None
while guess != correctnumber:
    try:
        guess = int(input("What number am i thinking?: "))
        if guess < 1 or guess > 100:
            print("The number needs to be greater than 0, less than or equal to 100.")
        elif guess <correctnumber>0 :
            print("That's too low, give it another go!")
        elif guess >correctnumber<101:
            print("That's too high, give it another try!")
        else:
            print("Great Job, you guessed the number!")
    except ValueError:
        print("Try Again, something wasn't quite right.")
# 1st line, imports random. 2nd line assigns correct number, 3rd 4th and 8th intro to game. 6th starts while loop.
# ive added "thats too high","thats too low" so the game dosent feel like a shot in the dark.
# valueError so it will not error the game if you have a invlaid input.