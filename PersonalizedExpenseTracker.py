class Expense:
    def __init__(self, category, description, amount):
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.category} - {self.description}: ${self.amount:.2f}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        expense = Expense(category, description, amount)
        self.expenses.append(expense)
        print(f"Expense added: {expense}")

    def delete_expense(self, index):
        try:
            deleted_expense = self.expenses.pop(index)
            print(f"Expense deleted: {deleted_expense}")
        except IndexError:
            print("Error: Invalid index.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
        else:
            print("Expenses:")
            for expense in self.expenses:
                print(expense)

    def generate_report(self):
        if not self.expenses:
            print("No expenses to generate report.")
        else:
            categories = {}
            for expense in self.expenses:
                if expense.category in categories:
                    categories[expense.category] += expense.amount
                else:
                    categories[expense.category] = expense.amount
            print("\nExpense Report:")
            for category, total in categories.items():
                print(f"{category}: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Generate Expense Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            category = input("Enter category (e.g., Food, Transport, Entertainment): ")
            description = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
                tracker.add_expense(category, description, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_expenses()
            try:
                index = int(input("Enter the index of the expense to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "4":
            tracker.generate_report()

        elif choice == "5":
            print("Exiting the expense tracker.")
            break

        else:
            print("Invalid choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
