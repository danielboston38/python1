##Name; Mark Dymek
##Purpose: Compute compound interest on deposits over times.
##Date: 4/4/25

#Setup Constant

NUMBER_MONTHS = ",.2f"



#data validation and input
while True:
    try:
        fDeposit = float(input("Please enter your deposit as a positive non-zero number:"))
        if fDeposit < 0:
            print("You did not follow the rules i don't accept zero or negative numbers:")
            continue
        break
    except ValueError:
        print("Please enter a valid number:")
while True:
    try:
        fInterest = float(input("Please enter your interest rate as a positive non-zero number:")) / 100 / 12
        if fInterest < 0:
            print("You did not follow the rules i don't accept zero or negative numbers:")
            continue
        break
    except ValueError:
        print("Please enter a valid number:")
while True:
    try:
        iMonths = int(input("Please enter how many months you are saving:"))
        if iMonths < 1:
            print("You did not follow the rules i don't accept zero or negative numbers:")
            continue
        break
    except ValueError:
        print("Please enter a valid number:")

while True:
    try:
        fGoal = float(input("Please enter your goal it can be zero:"))
        if fGoal < 0:
            print("You did not follow the rules i don't accept negative numbers:")
            continue
        break
    except ValueError:
        print("Please enter a valid number:")



faccount_Bal = fDeposit

for current_Month in range (1, iMonths +1):
     faccount_Bal += fInterest * faccount_Bal
     print(f"After {current_Month} months your balance is ${faccount_Bal:{NUMBER_MONTHS}}")

faccount_Bal= fDeposit
iloop_Count = 0
while faccount_Bal < fGoal:
    fmonthlyInterest = fInterest * faccount_Bal
    faccount_Bal += fmonthlyInterest
    iloop_Count += 1

print(f"it will take {iloop_Count} months to reach the goal of ${fGoal:{NUMBER_MONTHS}}")
