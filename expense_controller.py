from models.expense import Expense

class ExpenseController:
    def __init__(self, service):
        self.service = service

    def create_expense(self, amount, category, date, note):
        expense = Expense(
            id=len(self.service.expenses) + 1,
            amount=amount,
            category=category,
            date=date,
            note=note
        )
        self.service.add_expense(expense)
