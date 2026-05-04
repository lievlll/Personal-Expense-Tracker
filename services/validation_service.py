class ValidationService:
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def validate_text(text):
        return isinstance(text, str) and len(text.strip()) > 0
