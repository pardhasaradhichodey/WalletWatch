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

def view_expenses(expenses):
    """
    Display all expenses.

    Args:
    - expenses (list): The list of all expenses.
    """
    for expense in expenses:
        print(f"Date: {expense['Date']}, Category: {expense['Category']}, Amount: {expense['Amount']}, Description: {expense['Description']}")

def load_expenses(filename):
    """
    Load expenses from a CSV file.

    Args:
    - filename (str): Name of the CSV file to load expenses from.

    Returns:
    - list: A list of expense records.
    """
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
    """
    Save expenses to a CSV file.

    Args:
    - expenses (list): The list of all expenses.
    - filename (str): Name of the CSV file to save expenses to.
    """
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
