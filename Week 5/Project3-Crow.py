import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
stopLooping: str = "n"
maxGuesses = int(input("How many guesses do I get?"))
while (stopLooping == "n"):
    count += 1
    myGuess = random.randint(smaller, larger)
    print("Is it", myGuess, "?")
    stopLooping = str(input("y or n"))
    if (stopLooping == "y"):
        print("It took me", count, "tries!")
    else:
        if (count == maxGuesses):
            print("I exceeded the maximum amount of guesses and lost!")
            stopLooping = "y"
input("Press any key, then press enter to exit.")