from Semana_15.Eje_Algor_Orden import bubble_sort
import pytest

def test_bubble_sort_small_list():
    #Arrange
    test_list = [5, 2, 9, -2, -4, 1, 55, 6, 45]
    #Act
    expected_result = [-4, -2, 1, 2, 5, 6, 9, 45, 55]
    bubble_sort(test_list)
    #Assert
    assert test_list == expected_result

def test_bubble_sort_large_list():
    #Arrange
    test_list = [i for i in range(100, 0, -1)]  # List of 100 elements in reverse order
    #Act
    expected_result = [i for i in range(1, 101)]  # Sorted list from 1 to 100
    bubble_sort(test_list)
    #Assert
    assert test_list == expected_result


def test_bubble_sort_empty_list():
    #Arrange
    test_list = []
    #Act
    expected_result = []
    bubble_sort(test_list)
    #Assert
    assert test_list == expected_result


def test_bubble_sort_invalid_input():
    #Arrange
    test_list = "not a list"
    #Act
    #Assert
    with pytest.raises(TypeError):
        bubble_sort(test_list)

