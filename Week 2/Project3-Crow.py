New = int(input("Enter number of new movies rented."))
Old = int(input("Enter number of old movies rented."))
Days = int(input("Enter number of days rented for."))
totalCost = int(New * Old * Days)
print("Your total cost is", totalCost, "dollars.")
input("Press any key, then press enter to exit.")