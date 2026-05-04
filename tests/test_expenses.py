import unittest
from services.expense_service import ExpenseService
from models.expense import Expense

class TestExpenseService(unittest.TestCase):

    def test_add(self):
        s = ExpenseService()
        s.add_expense(Expense(1, 100, "food", "2026-01-01", "test"))
        self.assertEqual(len(s.expenses), 1)

    def test_total(self):
        s = ExpenseService()
        s.add_expense(Expense(1, 100, "food", "2026-01-01", "a"))
        s.add_expense(Expense(2, 50, "food", "2026-01-01", "b"))
        self.assertEqual(s.get_total(), 150)

    def test_delete(self):
        s = ExpenseService()
        e = Expense(1, 100, "food", "2026-01-01", "a")
        s.add_expense(e)
        s.delete_expense(1)
        self.assertEqual(len(s.expenses), 0)
        
    def test_empty(self):
        service = ExpendeService()
        self.assertEqual(service.get_total(),0)

if __name__ == "__main__":
    unittest.main()
