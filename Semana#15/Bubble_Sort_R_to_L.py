

def bubble_sort_right_to_left(list_to_sort):

    for outer_index in range(len(list_to_sort) - 1):
        has_made_changes = False
        for index in range(len(list_to_sort) -1, outer_index, -1):
            left_element = list_to_sort[index - 1]
            right_element = list_to_sort[index]

            print(f"-- Iteration {index}, Checking {left_element} with {right_element}")
        
            if left_element > right_element:
                    print(f"Exchanging {left_element} with {right_element}")
                    list_to_sort[index -1] , list_to_sort[index] = list_to_sort[index] , list_to_sort[index -1]
                    print(f"Updated List: {list_to_sort}")
                    has_made_changes = True
            
        if not has_made_changes:
            break

my_test_list = [5, 2, 9, 22, 4, 1, 15, 6, 12]
bubble_sort_right_to_left(my_test_list)
print(my_test_list)
