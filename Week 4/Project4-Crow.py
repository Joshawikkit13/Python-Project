dropHeight = float(input("Enter height you are dropping ball from in feet."))
Bounciness = .6
timesBounced = int(input("Enter number of times the ball bounced."))
ballDistance = dropHeight
currentBallHeight = dropHeight
x = 0
while (x < timesBounced):
    currentBallHeight = currentBallHeight * Bounciness
    ballDistance = ballDistance + currentBallHeight
    x = x + 1
    while (x < 2):
        ballDistance = ballDistance + currentBallHeight
        x = x + 1
print("Distance the ball traveled =", ballDistance, "feet")
print("Number of times bounced =", x, "feet")
print("Height of last bounce =", currentBallHeight, "feet")
input("Press any key, then press enter to exit.")