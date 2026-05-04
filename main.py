from controllers.expense_controller import ExpenseController
from services.expense_service import ExpenseService
from services.storage_service import StorageService

service = ExpenseService()
controller = ExpenseController(service)
storage = StorageService()

service.expenses = storage.load()

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. Delete expense")
    print("3. Show total")
    print("4. Filter by category")
    print("5. Save & Exit")

    choice = input("> ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        date = input("Date: ")
        note = input("Note: ")
        controller.create_expense(amount, category, date, note)

    elif choice == "2":
        eid = int(input("ID: "))
        service.delete_expense(eid)

    elif choice == "3":
        print("Total:", service.get_total())

    elif choice == "4":
        cat = input("Category: ")
        res = service.filter_by_category(cat)
        for r in res:
            print(r)

    elif choice == "5":
        storage.save(service.expenses)
        break
