import json
from logic import FinanceManager


def save_to_file(manager: FinanceManager, file='finance_data.json'):
    """Saves the finance data from the manager to a JSON file."""
    
    data = {
        'categories': list(manager.categories.keys()),
        'movements': [
            {
                'type_of_move': move.type_of_move,
                'amount': move.amount,
                'title': move.title,
                'category': move.category
            } for move in manager.movements
        ],
        'total_expenses': manager.total_expenses,
        'total_income': manager.total_income
    }
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
        print(f"Data saved to {file}")
    
def load_from_file(manager:FinanceManager, file='finance_data.json'):
    """Loads the finance data from a JSON file into the manager."""

    try:
        with open(file, 'r') as f:
            data = json.load(f)
            for name in data.get('categories', []):
                manager.add_category(name)
            for move in data.get('movements', []):
                manager.add_movement (
                    move['type_of_move'], 
                    float(move['amount']), 
                    move['title'], 
                    move['category'])
            manager.total_expenses = data.get('total_expenses', 0)
            manager.total_income = data.get('total_income', 0)
    except FileNotFoundError:
        print(f"File {file} not found. Starting with an empty finance manager.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file}. Starting with an empty finance manager.")


    
