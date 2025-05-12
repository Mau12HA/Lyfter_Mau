"""
2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y 
    `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        popped_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return popped_value

    def pop_right(self):
        if self.tail is None:
            return None
        popped_value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return popped_value

    def print_deque(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")


deque = Deque()
deque.push_left(1)
deque.push_right(2)
deque.push_left(3)
deque.push_right(4)
deque.print_deque()
print("Popped left:", deque.pop_left())
deque.print_deque()
print("Popped right:", deque.pop_right())
deque.print_deque()