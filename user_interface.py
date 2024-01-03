def show_menu():
    print("\n===== Personal Expense Tracker Menu =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Update Expense")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

from datetime import datetime


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_valid_amount(amount_str):
    try:
        float(amount_str)
        return True
    except ValueError:
        return False

def get_validated_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")


def get_expense_details():
    print("\n--- Add New Expense ---")
    date = get_validated_input("Enter date (YYYY-MM-DD): ", is_valid_date)
    category = input("Enter category: ")
    amount = get_validated_input("Enter amount: ", is_valid_amount)
    description = input("Enter description: ")

    return {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }

def display_expenses(expenses):
    print("\n--- Your Expenses ---")
    for expense in expenses:
        print(f"ID: {expense['ExpenseId']}, Date: {expense['Date']}, Category: {expense['Category']}, Amount: {expense['Amount']}, Description: {expense['Description']}")
    if not expenses:
        print("No expenses recorded.")

def choose_expense_to_delete(expenses):
    display_expenses(expenses)
    if expenses:
        try:
            choice = int(input("Enter the ID of the expense to delete: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
    return -1

def get_updated_expense_details():
    print("\n--- Update Expense Details ---")
    date = get_validated_input("Enter new date (YYYY-MM-DD) or press enter to keep unchanged: ", lambda x: not x or is_valid_date(x))
    category = input("Enter new category or press enter to keep unchanged: ")
    amount = get_validated_input("Enter new amount or press enter to keep unchanged: ", lambda x: not x or is_valid_amount(x))
    description = input("Enter new description or press enter to keep unchanged: ")

    updates = {}
    if date: updates['Date'] = date
    if category: updates['Category'] = category
    if amount: updates['Amount'] = amount
    if description: updates['Description'] = description

    return updates

def choose_expense_to_update(expenses):
    display_expenses(expenses)
    if expenses:
        try:
            choice = int(input("Enter the ID of the expense to update: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
    return -1
