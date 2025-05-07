# Name: Mark Dymek
# Purpose: Create a mini banking system in Python to show proficiency
# Date: 4/30/25

NUMBER_FORMAT = ",.2f"
sInitials = "md"

def main():
    print("Welcome to Mark's mini banking system.")

    # Gate entry: require user to press 7 to start
    while True:
        gate = input("Please enter 7 to access the program: ")
        if gate == "7":
            break
        print("Invalid input. Please enter 7 to continue.")

    balance = 0.0
    transactions = []

    while True:
        # Display the menu each loop
        print("\nMain Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Apply Interest Calculation")
        print("6. Save Transaction History to a file")
        print("7. Exit")
        choice = input("Please select an option (1-7): ")

        if choice == "1":
            balance = deposit(balance, transactions)
        elif choice == "2":
            balance = withdrawal(balance, transactions)
        elif choice == "3":
            checkBalance(balance)
        elif choice == "4":
            transaction_History(transactions)
        elif choice == "5":
            balance = interestApplication(balance, transactions)
        elif choice == "6":
            produceStatement(sInitials, balance, transactions)
        elif choice == "7":
            print("Exiting the banking system.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 7.")

def PromptForInput():
    """Prompts until the user enters a positive float."""
    while True:
        try:
            amount = float(input("Please enter a positive amount: "))
            if amount <= 0:
                print("You did not enter a positive number; try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def deposit(balance, transactions):
    amount = PromptForInput()
    balance += amount
    transactions.append(("Deposited", amount))
    print(f"You have successfully deposited ${amount:{NUMBER_FORMAT}}")
    return balance

def withdrawal(balance, transactions):
    withdrawal_Amount = PromptForInput()
    if withdrawal_Amount <= balance:
        balance -= withdrawal_Amount
        transactions.append(("Withdrawn", withdrawal_Amount))
        print(f"You have successfully withdrawn ${withdrawal_Amount:{NUMBER_FORMAT}}")
    else:
        print("You do not have enough money to withdraw that amount.")
    return balance

def checkBalance(balance):
    print(f"Here is your current balance: ${balance:{NUMBER_FORMAT}}")

def transaction_History(transactions):
    # Draw a box around the transaction history
    width = 33  # total inner width
    border = "+" + "-" * width + "+"
    title = "| Transaction History" + " " * (width - 1 - len("Transaction History")) + "|"

    print()
    print(border)
    print(title)
    print(border)

    if not transactions:
        line = "| No transactions to report." + " " * (width - len(" No transactions to report.")) + "|"
        print(line)
    else:
        for action, amount in transactions:
            # Format each line as: | Action           | $   1,234.56 |
            action_cell = f" {action:<15}"
            amount_cell = f"$ {amount:>10,.2f}"
            padding = width - len(action_cell) - len(amount_cell)
            line = "|" + action_cell + " " * padding + amount_cell + "|"
            print(line)

    print(border)

def interestApplication(balance, transactions):
    if balance <= 0:
        print("Your balance is zero or negative; no interest applied.")
        return balance

    # Prompt for a valid positive interest rate
    while True:
        try:
            rate_input = float(input("Enter annual interest rate (e.g., 5 for 5%): "))
            if rate_input <= 0:
                print("Please enter a positive interest rate.")
                continue
            monthly_rate = rate_input / 100 / 12
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    interest_amount = balance * monthly_rate
    balance += interest_amount
    transactions.append(("Interest", interest_amount))
    print(f"Interest of ${interest_amount:{NUMBER_FORMAT}} applied. New balance is ${balance:{NUMBER_FORMAT}}")
    return balance

def produceStatement(sInitials, balance, transactions):
    filename = f"{sInitials}BankStatements.txt"
    width = 33  # total inner width
    border = "+" + "-" * width + "+"
    title = "| Transaction History" + " " * (width - 1 - len("Transaction History")) + "|"
    with open(filename, "w") as file:
        file.write(border + "\n")
        file.write(title + "\n")
        file.write(border + "\n")

        if not transactions:
            empty_line = "| No transactions to report." + " " * (width - len(" No transactions to report.")) + "|"
            file.write(empty_line + "\n")
        else:
            for action, amount in transactions:
                action_cell = f" {action:<15}"
                amount_cell = f"$ {amount:>10,.2f}"
                padding = width - len(action_cell) - len(amount_cell)
                line = "|" + action_cell + " " * padding + amount_cell + "|"
                file.write(line + "\n")

        # Final balance line
        balance_content = f" Final Balance: ${balance:{NUMBER_FORMAT}}"
        balance_line = "|" + balance_content + " " * (width - len(balance_content)) + "|"
        file.write(border + "\n")
        file.write(balance_line + "\n")
        file.write(border + "\n")

    print(f"Statement written to {filename}. Thank you for using the system.")

main()