"""
1. Cree una estructura de objetos que asemeje un Stack.
    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None   

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def print_stack(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

stack = Stack()
stack.push(1)
stack.push(2)  
stack.push(3)
stack.print_stack() 
print("Popped:", stack.pop())
stack.print_stack()
print("Popped:", stack.pop())
stack.print_stack() 
print("Popped:", stack.pop())
stack.print_stack() 