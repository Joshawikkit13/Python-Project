evenOdd = 2
numOfIterations = int(input("Please enter the number of iterations you would like to approximate the value of pi."))
loopTimes = 0
Denominator = 1
Iteration = 1/Denominator
Pi = 1.0
while (loopTimes < numOfIterations):
    Denominator = Denominator + 2
    if (evenOdd % 2 == 0):
        Iteration = 1 / Denominator
        Pi = Pi - Iteration
    else:
        Iteration = 1 / Denominator
        Pi = Pi + Iteration
    evenOdd = evenOdd + 1
    loopTimes = loopTimes + 1
print("You used", numOfIterations, "iterations.")
print("Pi is approximately", Pi)
input("Press any key, then press enter to exit.")