class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []

    def add_expense(self):
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        self.expenses.append({"description": description, "amount": amount, "category": category})

    def add_category(self):
        category = input("Enter new category: ")
        self.categories.append(category)

    def total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def category_expenses(self, category):
        return sum(expense["amount"] for expense in self.expenses if expense["category"] == category)

    def display_expenses(self):
        for expense in self.expenses:
            print(f"Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")

    def run(self):
        while True:
            print("1. Add expense")
            print("2. Add category")
            print("3. Total expenses")
            print("4. Category expenses")
            print("5. Display expenses")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.add_category()
            elif choice == '3':
                print(f"Total expenses: {self.total_expenses()}")
            elif choice == '4':
                category = input("Enter category: ")
                print(f"Expenses in {category}: {self.category_expenses(category)}")
            elif choice == '5':
                self.display_expenses()
            elif choice == '6':
                break

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run() 