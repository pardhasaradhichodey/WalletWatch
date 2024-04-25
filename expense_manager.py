import csv
from datetime import datetime

def add_expense(date, category, amount, description, expenses):
    expense_id = len(expenses)  # Unique ID for the new expense
    expenses.append({
        "ExpenseId": expense_id,
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    })

def sort_expenses(expenses, sort_by):
    """
    Sort the list of expenses based on the specified criteria.

    Args:
    - expenses (list): The list of all expenses.
    - sort_by (str): The criteria to sort by ('Date', 'Category', 'Amount').

    Returns:
    - list: The sorted list of expenses.
    """
    key_func = {
        "1": lambda x: x["Date"],
        "2": lambda x: x["Category"],
        "3": lambda x: float(x["Amount"])
    }.get(sort_by, lambda x: x["ExpenseId"])  # Default to sorting by ExpenseId

    return sorted(expenses, key=key_func)

def view_expenses(expenses):
    for expense in expenses:
        print(f"Date: {expense['Date']}, Category: {expense['Category']}, Amount: {expense['Amount']}, Description: {expense['Description']}")

def load_expenses(filename):
    expenses = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        print(f"No existing file found named {filename}. Starting with an empty expense list.")
    return expenses

def save_expenses(expenses, filename):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["ExpenseId","Date", "Category", "Amount", "Description"])
        writer.writeheader()
        writer.writerows(expenses)

def delete_expense(expenses, expense_id):
    for i, expense in enumerate(expenses):
        if expense['ExpenseId'] == expense_id:
            del expenses[i]
            return True
    return False
def update_expense(expense_id, new_details, expenses):
    """
    Update an existing expense.

    Args:
    - expense_id (int): The ID of the expense to update.
    - new_details (dict): A dictionary containing the updated expense details.
    - expenses (list): The list of all expenses.

    Returns:
    - bool: True if the update was successful, False otherwise.
    """
    for expense in expenses:
        if expense['ExpenseId'] == str(expense_id):
            expense.update(new_details)
            return True
    return False

