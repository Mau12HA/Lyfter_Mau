import FreeSimpleGUI as sg
from persistence import save_to_file, load_from_file
from logic import FinanceManager
from interfaces import show_main_window, show_category_window, show_income_window, show_expense_window, update_table



def main():
    """Main function to run the Personal Finance Manager application."""

    manager = FinanceManager()
    load_from_file(manager)

    main_window = show_main_window()
    update_table(main_window, manager)

    while True:
        event, values = main_window.read()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            save_to_file(manager)
            break

        elif event == 'New Category':
            win = show_category_window()
            ev, val = win.read(close=True)
            if ev == 'Add Category':
                name = val['category_name'].strip()
                try:
                    manager.add_category(name)
                    sg.popup(f'Category "{name}" added!')
                except Exception as e:
                    sg.popup_error(str(e))
            win.close()

        elif event == 'Income':
            if not manager.categories:
                sg.popup_error('Please add a category first.')
                continue
            win = show_income_window(manager)
            ev, val = win.read(close=True)
            if ev == 'Add Income':
                try:
                    amount = float(val['income_amount'])
                    title = val['income_title']
                    category = val['income_category']
                    if not title:
                        raise ValueError("Title cannot be empty.")
                    if not category:
                        raise ValueError("Category must be selected.")
                    manager.add_movement('income', amount, title, category)
                    sg.popup('Income added!')
                    update_table(main_window, manager)
                except Exception as e:
                    sg.popup_error(str(e))
            win.close()

        elif event == 'Expenses':
            if not manager.categories:
                sg.popup_error('Please add a category first.')
                continue
            win = show_expense_window(manager)
            ev, val = win.read(close=True)
            if ev == 'Add Expense':
                try:
                    amount = float(val['expense_amount'])
                    title = val['expense_title']
                    category = val['expense_category']
                    if not title:
                        raise ValueError("Title cannot be empty.")
                    if not category:
                        raise ValueError("Category must be selected.")
                    manager.add_movement('spent', amount, title, category)
                    sg.popup('Expense added!')
                except Exception as e:
                    sg.popup_error(str(e))
            win.close()

    main_window.close()