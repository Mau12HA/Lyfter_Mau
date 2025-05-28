import pytest
from logic import FinanceManager


def test_add_category_success():
    manager = FinanceManager()
    assert manager.add_category("Comida") is True
    assert "Comida" in manager.categories


def test_add_category_duplicate():
    manager = FinanceManager()
    manager.add_category("Transporte")
    with pytest.raises(ValueError):
        manager.add_category("Transporte")


def test_add_category_empty():
    manager = FinanceManager()
    with pytest.raises(ValueError):
        manager.add_category("")


def test_add_movement_success_income():
    manager = FinanceManager()
    manager.add_category("Trabajo")
    result = manager.add_movement("income", 1000, "Sueldo", "Trabajo")
    assert result is True
    assert manager.total_income == 1000


def test_add_movement_success_expense():
    manager = FinanceManager()
    manager.add_category("Comida")
    result = manager.add_movement("spent", 200, "Almuerzo", "Comida")
    assert result is True
    assert manager.total_expenses == 200


def test_add_movement_invalid_category():
    manager = FinanceManager()
    with pytest.raises(ValueError):
        manager.add_movement("income", 100, "Extra", "Inexistente")


def test_add_movement_negative_amount():
    manager = FinanceManager()
    manager.add_category("Deudas")
    with pytest.raises(ValueError):
        manager.add_movement("spent", -100, "Pago de Deuda", "Deudas")


def test_add_movement_empty_title():
    manager = FinanceManager()
    manager.add_category("Salud")
    with pytest.raises(ValueError):
        manager.add_movement("spent", 50, "", "Salud")


def test_get_balance():
    manager = FinanceManager()
    manager.add_category("Trabajo")
    manager.add_category("Comida")
    manager.add_movement("income", 1000, "Sueldo", "Trabajo")
    manager.add_movement("spent", 300, "Cena", "Comida")
    assert manager.get_balance() == 700


def test_get_balance_no_movements():
    manager = FinanceManager()
    assert manager.get_balance() == 0.0

def test_total_income_and_expenses():
    manager = FinanceManager()
    manager.add_category("Salario")
    manager.add_category("Alquiler")
    manager.add_movement("income", 1500, "Salario Mensual", "Salario")
    manager.add_movement("spent", 500, "Alquiler Mensual", "Alquiler")
    
    assert manager.total_income == 1500
    assert manager.total_expenses == 500
    assert manager.get_balance() == 1000

def test_add_movement_invalid_type():
    manager = FinanceManager()
    manager.add_category("Ahorros")
    with pytest.raises(ValueError):
        manager.add_movement("invalid_type", 100, "Ahorro Mensual", "Ahorros")

def test_add_movement_zero_amount():
    manager = FinanceManager()
    manager.add_category("Regalos")
    with pytest.raises(ValueError):
        manager.add_movement("income", 0, "Regalo Cumpleaños", "Regalos")


def test_add_movement_non_numeric_amount():
    manager = FinanceManager()
    manager.add_category("Educación")
    with pytest.raises(ValueError):
        manager.add_movement("income", "cien", "Beca", "Educación")

def test_add_movement_non_string_title():
    manager = FinanceManager()
    manager.add_category("Salud")
    with pytest.raises(ValueError):
        manager.add_movement("spent", 100, 12345, "Salud")  # Title should be a string

def test_add_movement_non_string_category():
    manager = FinanceManager()
    manager.add_category("Viajes")
    with pytest.raises(ValueError):
        manager.add_movement("income", 200, "Bono de Viaje", 12345)  # Category should be a string

        