from user_interface import (show_menu, get_expense_details, display_expenses, 
                            choose_expense_to_delete, choose_expense_to_update, get_updated_expense_details)
from expense_manager import (add_expense, view_expenses, load_expenses, save_expenses, 
                             delete_expense, update_expense)
def main():
    filename = "expenses.csv"
    expenses = load_expenses(filename)

    while True:
        choice = show_menu()

        if choice == '1':
            expense_details = get_expense_details()
            add_expense(expense_details['Date'], expense_details['Category'], expense_details['Amount'], expense_details['Description'], expenses)

        elif choice == '2':
            display_expenses(expenses)

        elif choice == '3':
            expense_id = choose_expense_to_delete(expenses)
            if expense_id != -1:
                if delete_expense(expenses, expense_id):
                    print("Expense deleted successfully.")
                else:
                    print("Failed to delete expense.")
            else:
                print("Deletion cancelled.")
        elif choice == '4':
            expense_id = choose_expense_to_update(expenses)
            if expense_id != -1:
                new_details = get_updated_expense_details()
                if update_expense(expense_id, new_details, expenses):
                    print("Expense updated successfully.")
                else:
                    print("Failed to update expense.")
            else:
                print("Update cancelled.")
        elif choice == '5':
            save_expenses(expenses, filename)
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
