totalHours = float(input("Enter total hours worked. "))
overHours = totalHours - 40
Wage = float(input("Enter your hourly wage. "))
if overHours > 0:
    normHours = 40
    totalPay = (normHours * Wage) + (overHours * Wage * 1.5)

else:
    normHours = totalHours
    totalPay = (normHours * Wage)

print("Your total weekly pay is", totalPay, "dollars.")
input("Press any key, then press enter to exit.")