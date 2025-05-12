"""
Cree un decorador que haga print de los parámetros y retorno de la función que decore.
"""


def operations(func):
    
    def wrapper(*args):
        print(f"Parameters: {args}")
        result = func(*args)
        print(f"Return: {result}")
        return result
    return wrapper

@operations
def add(a, b):
    return a + b    

@operations
def subtraction(a, b):
    return a - b    


resultado = add(12, 25)
resultado = subtraction(21, 13)