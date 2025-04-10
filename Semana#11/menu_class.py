

def menu_system_student():

    while True:
        try:
            operation = int(input("\nSELECT AN OPTION\n"
                                "\n1. Add student"
                                "\n2. See students information"
                                "\n3. TOP #3 students"
                                "\n4. General average"
                                "\n5. Export file CSV"
                                "\n6. Import file CSV\n \n"))

                            
            if(operation <=6 and operation > 0):
                
                break 
            else:
                print("Wrong option, enter a valid option from the menu")
        except ValueError:
            print("Enter an integer from 1 to 6 to select a valid menu option. \n")

    return operation
