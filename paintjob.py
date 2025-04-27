#Name: Mark Dymek
#Purpose: Code a program that calculates a estimate for a paint job
#Date: 4/18/2025

from math import ceil

NUMBER_FORMAT = ",.2f"

def getFloatInput(prompt): #data validation  code
    while True:
        try:
            fValue = float(input(prompt))
            if fValue > 0:
                return fValue
            else:
                print("You have not entered a positive, non-zero number please try again")
        except ValueError:
            print("Input must be a numeric value please try again")



#set up code for the estimator

def getGallonsOfPaint(fSQFT, fFeet_Gallon):
    nGallons = ceil(fSQFT / fFeet_Gallon)
    return int(nGallons)

def getPaintCost(nGallons,fPrice):
    fPaint_Cost = (nGallons * fPrice)
    return fPaint_Cost

def getLaborHours(fGallon_Hrs, nGallons):
    fTLabor_Hour = (fGallon_Hrs * nGallons)
    return fTLabor_Hour

def getLaborCost(fTLabor_Hour, fPainting_Labor):
    fLabor_Cost = (fTLabor_Hour * fPainting_Labor)
    return fLabor_Cost

def getSales_Tax(sState):
    if sState == "MA":
        fTax_Rate = 0.0625
    elif sState == "CT":
        fTax_Rate = .06
    elif sState == "ME":
        fTax_Rate = .085
    elif sState == "RI":
        fTax_Rate = .07
    elif sState == "VT":
        fTax_Rate = .06
    else:
        fTax_Rate = 0
    return fTax_Rate

def main():
    sState = input("Enter the state this job is taking place in: ")  #main function that handles everything
    sLast_Name = input("Enter the last name of the customer: ")
    fuser_Input_Wall = getFloatInput("Enter the sqaure footage of your wall: ")
    fuser_Input_Price = getFloatInput("Enter the price of the paint: ")
    iuser_Input_Gallons = getFloatInput("Enter the number of feet per gallon of paint: ")
    fuser_Input_Hours = getFloatInput("Enter the number of labor hours worked per gallon: ")
    fuser_Input_Labor = getFloatInput("Enter the painting labor charge per hour: ")
    fTax_Rate_For_Job = getSales_Tax(sState)
    ical_Gallons = getGallonsOfPaint(fuser_Input_Wall, iuser_Input_Gallons)
    fPaint_Cost = getPaintCost(ical_Gallons, fuser_Input_Price)
    fHours_Paid = getLaborHours(fuser_Input_Hours, ical_Gallons)
    fLabor_Amount = getLaborCost(fHours_Paid, fuser_Input_Labor)
    fTax = (fPaint_Cost + fLabor_Amount) * fTax_Rate_For_Job
    fTCost = fPaint_Cost + fLabor_Amount + fTax
    showCostEstimate(sLast_Name, sState, ical_Gallons, fHours_Paid, fuser_Input_Labor, fPaint_Cost, fLabor_Amount, fTax, fTCost)

#print outputs to screen
def showCostEstimate(sLast_Name, sState, ical_Gallons, fHours_Paid, fuser_Input_Labor, fPaint_Cost, fLabor_Amount, fTax, fTCost):

    print(f"Gallons of paint: {ical_Gallons}")
    print(f"Hours of labor: {fHours_Paid:{NUMBER_FORMAT}}")
    print(f"Labor charge per hour: ${fuser_Input_Labor:{NUMBER_FORMAT}}")
    print(f"State job is in: {sState}")
    print(f"Customer last name: {sLast_Name}")
    print(f"Paint Charges: ${fPaint_Cost:{NUMBER_FORMAT}}")
    print(f"Labor Charges: ${fLabor_Amount:{NUMBER_FORMAT}}")
    print(f"Tax: ${fTax:{NUMBER_FORMAT}}")
    print(f"Total Cost: ${fTCost:{NUMBER_FORMAT}}")

    sFileName = f"{sLast_Name}_PaintJobOutput.txt" #setup and output to a file
    with open(sFileName, "w") as outfile:
        outfile.write(f"Gallons of paint: {ical_Gallons}\n")
        outfile.write(f"Hours of labor: {fHours_Paid:{NUMBER_FORMAT}}\n")
        outfile.write(f"Labor charge per hour: ${fuser_Input_Labor:{NUMBER_FORMAT}}\n")
        outfile.write(f"State: {sState}\n")
        outfile.write(f"Customer last name: {sLast_Name}\n")
        outfile.write(f"Paint Charges: ${fPaint_Cost:{NUMBER_FORMAT}}\n")
        outfile.write(f"Labor Charges: ${fLabor_Amount:{NUMBER_FORMAT}}\n")
        outfile.write(f"Tax: ${fTax:{NUMBER_FORMAT}}\n")
        outfile.write(f"Total Cost: ${fTCost:{NUMBER_FORMAT}}\n")

    print(f"Output file {sFileName} has been successfully created.")



main()