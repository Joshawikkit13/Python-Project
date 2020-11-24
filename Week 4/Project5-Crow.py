startingNumOrganisms = int(input("Enter the starting number of organisms."))
Growth = float(input("Enter a rate of growth greater than zero."))
rateHours = float(input("Enter the number of hours it took to achieve this growth."))
totalHours = float(input("Enter the total hours to estimate growth for."))
growthRate = Growth/rateHours
totalGrowth = startingNumOrganisms * growthRate * totalHours
print("Estimated number grown after", totalHours, "is", totalGrowth)
input("Press any key, then press enter to exit.")