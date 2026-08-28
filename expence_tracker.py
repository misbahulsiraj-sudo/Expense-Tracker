import os

FILE_NAME = "expenses.txt"


def add_expense():
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{category},{amount}\n")

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        expenses = file.readlines()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expense History ---")
    for i, expense in enumerate(expenses, start=1):
        category, amount = expense.strip().split(",")
        print(f"{i}. {category} - ₹{amount}")


def show_total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        for line in file:
            _, amount = line.strip().split(",")
            total += float(amount)

    print(f"\nTotal Expense: ₹{total:.2f}")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expense")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total_expense()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()