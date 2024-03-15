import os
import json

TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r") as file:
            transactions = json.load(file)
        return transactions
    return {"income": [], "expenses": []}

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=2)

def add_transaction(transactions, transaction_type, category, amount):
    transaction = {"category": category, "amount": amount}
    transactions[transaction_type].append(transaction)
    print(f"{transaction_type.capitalize()} added successfully!")

def calculate_budget(transactions):
    income = sum(transaction["amount"] for transaction in transactions["income"])
    expenses = sum(transaction["amount"] for transaction in transactions["expenses"])
    return income - expenses

def analyze_expenses(transactions):
    categories = {}
    for transaction in transactions["expenses"]:
        category = transaction["category"]
        amount = transaction["amount"]
        categories[category] = categories.get(category, 0) + amount
    return categories

def display_transactions(transactions):
    print("\n===== Transactions =====")
    print("Income:")
    for income in transactions["income"]:
        print(f"- Category: {income['category']}, Amount: {income['amount']}")
    print("\nExpenses:")
    for expense in transactions["expenses"]:
        print(f"- Category: {expense['category']}, Amount: {expense['amount']}")
    print("\n")

def main():
    transactions = load_transactions()

    while True:
        print("===== Budget Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            add_transaction(transactions, "income", category, amount)

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_transaction(transactions, "expenses", category, amount)

        elif choice == "3":
            remaining_budget = calculate_budget(transactions)
            print(f"Remaining budget: {remaining_budget}")

        elif choice == "4":
            expense_analysis = analyze_expenses(transactions)
            print("\n===== Expense Analysis =====")
            for category, amount in expense_analysis.items():
                print(f"{category}: {amount}")

        elif choice == "5":
            save_transactions(transactions)
            print("Exiting. Your transactions are saved.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
