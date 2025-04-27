# Compounding Interest with Loops
# Professor C.

import inputPromptValidationModule

# This code use the inputPromptValidation module for learning purposes:
# -Deposit must be positive value and non-zero
# -Interest must be positive value and non-zero
# -Number of Months must be positive value and non-zero
# -Goal must be positive value and zero is OK

#Created function to calculate compounding interest
def MonthlyInterest(fDeposit,fInterestRate):
  return fDeposit * fInterestRate

#Main function asking for input(calling inputValidation and MonthlyInterest functions)
def main():

    fDeposit = inputPromptValidationModule.inputFloatValidation("What is the Original Deposit (positive value): ", 0.01)
    fInterestRate = inputPromptValidationModule.inputFloatValidation("What is the Interest Rate (positive value): ", 0.01)
    iMonths = inputPromptValidationModule.inputIntValidation("What is the Number of Months (positive value): ", 0)
    fGoal = inputPromptValidationModule.inputFloatValidation("What is the Goal Amount (can enter 0 but not a negative): ", 0.0)

    # Test using the String input function:
    sName = inputPromptValidationModule.inputStringValidation("What is your Name? " )
    print("Hello", sName)

    
#Calculating monthly interest  rate
    fMonthlyInterestRate = (fInterestRate/100)/12
    fAccountBalance = fDeposit

#Loop to output the month and monthly totals
    for iMonth in range(1, iMonths + 1):
      fAccountBalance += MonthlyInterest(fAccountBalance, fMonthlyInterestRate)
    
      print("Month: ", iMonth, "Account Balance is: $" + format(fAccountBalance, ",.2f"))

#Loop to calculate how long it would take to reach the goal set
    iMonth = 0
    fAccountBalance = fDeposit
    while fAccountBalance <= fGoal:
      fAccountBalance += MonthlyInterest(fAccountBalance, fMonthlyInterestRate)
      iMonth += 1
    
    print("It will take: ", iMonth, " months to reach the goal of $" + format(fGoal, ",.2f"))

#calling the main function
main()


