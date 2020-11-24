side1 = float(input("Please enter side 1 of the triangle."))
side2 = float(input("Please enter side 2 of the triangle."))
if(side1 == side2):
    side3 = float(input("Please enter side 3 of the triangle."))
    if(side2 == side3):
        print("Congratulations, you have an equilateral triangle!")
    else:
        print("Sorry, not an equilateral triangle.")
else:
    print("Sorry, not an equilateral triangle.")
input("Press any key, then press enter to exit.")