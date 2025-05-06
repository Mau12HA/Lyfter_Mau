"""
Analice el algoritmo de bubble_sort usando la Big O Notation

"""

def bubble_sort(list_to_sort):

    for outer_index in range(len(list_to_sort) - 1): # O(log n)
        has_made_changes = False
        for index in range(0, len(list_to_sort) -1 -outer_index): # O(log n)
            current_element = list_to_sort[index] # O(1)
            next_element = list_to_sort[index + 1] # O(1)

            print(f"-- Iteration {index}, Checking {current_element} with {next_element}") # O(1)
        
            if current_element > next_element: # O(1)
                    print(f"Exchanging {current_element} with {next_element}") # O(1)
                    list_to_sort[index] = next_element # O(1)
                    list_to_sort[index + 1] = current_element # O(1)
                    print(f"Updated List: {list_to_sort}") # O(1)
                    has_made_changes = True
            
        if not has_made_changes:
            break

my_test_list = [5, 2, 9, -2, -4, 1, 55, 6, 45] # O(1)
bubble_sort(my_test_list) # O(1)
print(my_test_list) # O(1)
