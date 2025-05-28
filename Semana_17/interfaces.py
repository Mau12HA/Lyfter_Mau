import FreeSimpleGUI as sg
from logic import FinanceManager

sg.theme('Dark Blue 12')

#manager = FinanceManager()

def update_table(window,manager):
    """Updates the table in the main window with the current movements."""
    table_data = [[m.type_of_move, m.title, m.amount, m.category] 
                  for m in manager.movements]
    window['-TABLE-'].update(values=table_data)

def show_main_window():
     """Creates and returns the main window layout for the Personal Finance Manager."""

     layout = [
            [sg.Text('Welcome to the Personal Finance Manager!')],
            [sg.Table(values=[['','', '0', ''], ['','','0', '']], 
                    justification='center', expand_x=True, expand_y=True,
                    headings=['Type', 'Title', 'Amount', 'Category'], 
                    auto_size_columns=True, num_rows=5, key='-TABLE-')],
            [sg.Text('Please select income or expenses:')],
            [sg.Button('New Category')],[sg.Button('Income')],[sg.Button('Expenses')],[sg.Button('Exit')],
    ]

     return sg.Window('Personal Finance Manager',layout,finalize=True)


def show_category_window():
    """Creates and returns the window layout for adding a new category."""

    layout = [
        [sg.Text('Add New Category')],
        [sg.Text('Category Name'), sg.InputText(key='category_name')],
        [sg.Button('Add Category'), sg.Button('Cancel')]
    ]

    return sg.Window('New Category', layout, modal=True)


def show_income_window(manager):
    """Creates and returns the window layout for adding a new income entry."""

    layout = [
        [sg.Text('Add Income')],
        [sg.Text('Amount'), sg.InputText(key='income_amount')],
        [sg.Text('Title'), sg.InputText(key='income_title')],
        [sg.Text('Category'), sg.Combo(list(manager.categories.keys()), key='income_category')],
        [sg.Button('Add Income'), sg.Button('Cancel')]
    ]

    return sg.Window('Add Income', layout, modal=True)

def show_expense_window(manager):
    """Creates and returns the window layout for adding a new expense entry."""

    layout = [
        [sg.Text('Add Expense')],
        [sg.Text('Amount'), sg.InputText(key='expense_amount')],
        [sg.Text('Title'), sg.InputText(key='expense_title')],
        [sg.Text('Category'), sg.Combo(list(manager.categories.keys()), key='expense_category')],
        [sg.Button('Add Expense'), sg.Button('Cancel')]
    ]

    return sg.Window('Add Expense', layout, modal=True)

