#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 9/22/21
#Project #: Paycheck Calculator App
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Austin Jordan's Pay Check Calculator App")

# create variable for hours worked and ask for user input
hoursWorked = float(input("Enter hours worked: "))

# create variable for pay rate and ask for user input
payRate = float(input("Enter pay rate: "))

# blank line
print()

# create variable for gross pay
grossPay = hoursWorked * payRate

# tells user their gross pay after calculations
print("Gross Pay: " + str(round(grossPay, 2)))

# creates variable for the tax rate
taxRate = 18

# tells user the tax rate
print("Tax Rate: " + str(taxRate))

# creates variable for tax amount
taxAmnt = grossPay * (taxRate / 100)

# tells user the amount they are being taxed
print("Tax Amount: " + str(round(taxAmnt, 2)))

# creates variable for take home pay
takeHomePay = grossPay - taxAmnt

# tells user what their take home pay is, after taxes
print("Take Home Pay: " + str(round(takeHomePay, 2)))