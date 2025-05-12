def verify_numbers(func):
    def wrapper(*args):
        values= list(args)
        for i in values:
            if not isinstance(i, (int, float)):
                raise ValueError("All arguments must be numbers",{i})
        return func(*args)
    return wrapper

@verify_numbers
def add(a, b):
    return a + b

print(add(4, 5)) 
print(add(3, "hola"))