# Name: Mark Dymek
# Purpose: Create a program for real estate sales
# Date: 5/1/2025

import random

NUMBER_FORMAT = ",.2f"

def getFloatInput(prompt):
    while True:
        try:
            fValue = float(input("Please enter a positive amount: "))
            if fValue > 0:
                return fValue
            else:
                print("Please enter a positive non-zero number")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def getMedian(salesList):
    iNumber = len(salesList)
    sortedList = sorted(salesList)
    if iNumber % 2 == 1:
        return sortedList[iNumber // 2]
    else:
        iMid = iNumber // 2
        return (sortedList[iMid - 1] + sortedList[iMid]) / 2

def main():
    salesList = []
    while True:
        choice = input("Do you want to enter a value yes or no? ").strip().upper()

        if choice == "JOE":
            print("\n🚨 Joe Mode Activated...")
            print("🛒 You may have won the 1995 Walmart Grand Prix...")
            print("...but I won the war. 💻🐍")

            # Add fake sales
            salesList.append(1995.00)
            salesList.append(999999.99)
            print("🏷️ Special: Joe's legendary 1995 property and a fake million-dollar sale were added.")

            # Save Joe's crime to a file
            with open("joe_mode_activated.txt", "w") as file:
                file.write("Joe tried to cheat again in 2025...\n")
                file.write("George still won. 🏁\n")

            # Bugs Bunny quote
            quotes = [
                "Eh, what's up Doc?",
                "I knew I shoulda taken that left turn at Albuquerque.",
                "You realize, of course, this means war."
            ]
            print(random.choice(quotes))

            # ASCII trophy
            print("""
     _______
    /       \\
   |   🏆    |
    \\_______/
   George Wins
""")
            continue

        if choice == "N":
            break
        elif choice == "Y":
            amount = getFloatInput("Enter the property value: ")
            salesList.append(amount)
        else:
            print("Invalid input. Please enter Y or N.")

    print()
    for i, sale in enumerate(sorted(salesList), start=1):
        print(f"Property {i}: ${sale:{NUMBER_FORMAT}}")

    print(f"\n{'Lowest sale:':<20}${min(salesList):>15,.2f}")
    print(f"{'Highest sale:':<20}${max(salesList):>15,.2f}")
    fTotal = sum(salesList)
    print(f"{'Total sales:':<20}${fTotal:>15,.2f}")
    iItems = len(salesList)
    fAverage = fTotal / iItems
    print(f"{'Average sale:':<20}${fAverage:>15,.2f}")
    fMedian = getMedian(salesList)
    print(f"{'Median sale:':<20}${fMedian:>15,.2f}")

    # Override commission if Joe is cheating
    if any(abs(sale - 1995.00) < 0.01 for sale in salesList):
        fCommission = 0
        print("❌ Joe can't earn commission. Cheaters get nothing.")
    else:
        fCommission = 0.03 * fTotal
    print(f"{'Commission:':<20}${fCommission:>15,.2f}")

    print("\nGeorge is the winner 🏆")

main()