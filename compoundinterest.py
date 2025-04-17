#Mark Dymek
#2/28/2025
#purpose: Create python program to calcuate compound interest on savings

NUMBER_FORMAT=",.2f"

#ask how much you are saving, the interest rate, how many times will it compound and for how many years wil you be saving.

fAmount=float(input("Enter the starting principal: "))
fInterest=float(input("Enter the interest rate: ")) / 100 #convert percentage to decimal
nTime=int(input("How many times per year is the interest compounded?: "))
fYear=float(input("For how how time will the account earn interest: "))
#calcuate the interest
fFuture_value = fAmount * (1 + fInterest / nTime) ** (nTime * fYear)
#print the results
print(f"At the end of {fYear} years you will have: ${fFuture_value:{NUMBER_FORMAT}}")
#Joe told me to do it this way. i guess its ok for now that it says 2.0 years?
#prof c. you may show my code with my name i don't mind
