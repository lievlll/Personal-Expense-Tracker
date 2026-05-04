from utils.stack import Stack

class ExpenseService:
    def __init__(self):
        self.expenses = []
        self.undo_stack = Stack()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.undo_stack.push(("add", expense))

    def delete_expense(self, expense_id):
        for e in self.expenses:
            if e.id == expense_id:
                self.expenses.remove(e)
                self.undo_stack.push(("delete", e))
                return True
        return False

    def get_total(self):
        return sum(e.amount for e in self.expenses)

    def filter_by_category(self, category):
        return [e for e in self.expenses if e.category == category]
