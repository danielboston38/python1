#Name: Mark Dymek
#Purpose: Create a program for real estate sales
#Date: 5/1/2025
NUMBER_FORMAT = ",.2f"

def getFloatInput(prompt):#handle getting input and make sure its correct
    while True:
        try:
            fValue = float(input("Please enter a positive amount: "))
            if fValue > 0:
                return fValue
            else:
                print("Please enter a positive non-zero number")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            
def getMedian(salesList): #get the average
    iNumber = len(salesList)
    sortedList = sorted(salesList)
    if iNumber % 2 == 1:
        return sortedList[iNumber // 2]
    else:
        iMid = iNumber // 2
        return (sortedList[iMid - 1] + sortedList[iMid]) / 2

def main():#our main code block. calls our functions.
    salesList = []
    while True:
        choice = input("Do you want to enter a value yes or no?").strip().upper()
            continue
        if choice == "N":
            break
        elif choice == "Y":
            amount = getFloatInput("Enter the property value: ")
            salesList.append(amount)
        else:
            print("Invalid input. Please enter Y or N.")

        for i, sale in enumerate(sorted(salesList), start=1):
            print(f"Property {i}: ${sale:{NUMBER_FORMAT}}")
    print(f"{'Lowest sale:':<20}${min(salesList):>15,.2f}")
    print(f"{'Highest sale:':<20}${max(salesList):>15,.2f}")
    fTotal = sum(salesList)
    print(f"{'Total sales:':<20}${fTotal:>15,.2f}")
    iItems = len(salesList)
    fAverage = fTotal / iItems
    print(f"{'Average sale:':<20}${fAverage:>15,.2f}")
    fMedian = getMedian(salesList)
    print(f"{'Median sale:':<20}${fMedian:>15,.2f}")
    fCommission = 0.03 * fTotal
    print(f"{'Commission:':<20}${fCommission:>15,.2f}")
main()
