def show_menu():
    print("\n===== Personal Expense Tracker Menu =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    return input("Enter your choice (1-4): ")


def get_expense_details():
    """
    Get details of a new expense from the user.

    Returns:
    - dict: A dictionary containing the expense details.
    """
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
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

