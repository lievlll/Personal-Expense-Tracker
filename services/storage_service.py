import json
from models.expense import Expense

class StorageService:
    FILE_PATH = "data/expenses.json"

    def load(self):
        try:
            with open(self.FILE_PATH, "r") as f:
                data = json.load(f)
                return [Expense(**item) for item in data]
        except FileNotFoundError:
            return []

    def save(self, expenses):
        with open(self.FILE_PATH, "w") as f:
            json.dump([e.__dict__ for e in expenses], f, indent=4)
