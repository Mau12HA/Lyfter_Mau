from Semana_6.Funciones_Ejer_3 import get_sum_list
from Semana_6.Funciones_Ejer_4 import string_back_way
from Semana_6.Funciones_Ejer_5 import counter_lower_upper
from Semana_6.Funciones_Ejer_6 import order_words_alpha
from Semana_6.Funciones_Ejer_7 import list_prime_numbers


def test_get_sum_list():
    # Arrange
    test_list = [23,4,5,7,78,61]
    # Act
    expected_result = 178
    result = get_sum_list(test_list)
    # Assert
    assert result == expected_result


def test_string_back_way():
    # Arrange
    test_string = "Hola mundo"
    # Act
    expected_result = "odnum aloH"
    result = string_back_way(test_string)
    # Assert
    assert result == expected_result


def test_counter_lower_upper():
    # Arrange
    test_string = "I love Nación Sushi"
    # Act
    expected_result = {'Mayusculas': 3, 'minusculas': 13}
    result = counter_lower_upper(test_string)
    # Assert
    assert result == expected_result


def test_order_words_alpha():
    # Arrange
    test_string = "python-variable-funcion-computadora-monitor"
    # Act
    expected_result = "computadora-funcion-monitor-python-variable"
    result = order_words_alpha(test_string)
    # Assert
    assert result == expected_result


def test_list_prime_numbers():
    # Arrange
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Act
    expected_result = [2, 3, 5, 7]
    result = list_prime_numbers(test_list, []) 
    # Assert
    assert result == expected_result


