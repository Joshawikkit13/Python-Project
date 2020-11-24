numOfAddends = int(1)
stillLooping = "y"
userInput = float(input("Please enter your first number"))
while(stillLooping == "y"):
    userInput2 = float(input("Please enter your next number."))
    userInput = userInput + userInput2
    numOfAddends = numOfAddends + 1
    stillLooping = input("Would you like to add another number? (y or n)")
Average = userInput/numOfAddends
print("The sum of all your numbers is", userInput)
print("The average of all your numbers is", Average)
input("Press enter to exit.")