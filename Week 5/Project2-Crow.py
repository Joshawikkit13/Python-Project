side1 = float(input("Please enter side 1 (not the hypotenuse) of the triangle."))
side2 = float(input("Please enter side 2 (also not the hypotenuse) of the triangle."))
side3 = float(input("Please enter the hypotenuse of the triangle."))
if((side1 * side1) + (side2 *side2) == (side3 * side3)):
    print("Congratulations, you have a right triangle!")
else:
    print("Sorry, this is not a right triangle.")
input("Press any key, then press enter to exit.")