from typing import Dict

class Category():
    """A class to represent a category for financial movements."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    

class Movement():
    """A class to represent a financial movement, either income or expense."""

    def __init__(self,type_of_move, amount, title, category):
        self.type_of_move = type_of_move
        self.amount = amount
        self.title = title
        self.category = category

    def __str__(self):
        return f"Movement: {self.type_of_move},Title: {self.title}, Amount: {self.amount}, Category: {self.category}"
    

class FinanceManager():
    """A class to manage personal finances, including categories and movements."""

    def __init__(self):
        self.categories: Dict[str, Category] = {}
        self.movements = []
        self.total_expenses: float = 0.0
        self.total_income: float = 0.0

    def add_category(self, name):
        """Adds a new category to the manager."""
        
        if not name.strip():
            raise ValueError("The category name is empty.")
        if name in self.categories:
            raise ValueError("This category already exists.")
        self.categories[name] = Category(name)
        return True


    def add_movement(self, type_of_move, amount, title, category_name):
        """Adds a financial movement (income or expense) to the manager."""

        if category_name not in self.categories:
            raise ValueError("Category does not exist.")
        if not title.strip():
            raise ValueError("Empty Title.")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("The amount must be positive.")

        movement = Movement(type_of_move, amount, title, category_name)
        self.movements.append(movement)

        if type_of_move.lower() == "spent":
            self.total_expenses += amount
        elif type_of_move.lower() == "income":
            self.total_income += amount
        else:
            raise ValueError("Invalid movement type.")

        return True


    def get_balance(self):
        """Calculates the balance by subtracting total expenses from total income."""

        return self.total_income - self.total_expenses

    def __str__(self):
        return f"Total Income: {self.total_income}, Total Expenses: {self.total_expenses}, Balance: {self.get_balance()}"
    

