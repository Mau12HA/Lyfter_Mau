"""
3. Cree una estructura de objetos que asemeje un Binary Tree.
    1. Debe incluir un método para hacer `print` de toda la estructura.
    2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)

    def print_tree(self):
        if self.root is not None:
            self._print_recursive(self.root)

    def _print_recursive(self, node):
        if node is not None:
            self._print_recursive(node.left)
            print(node.value, end=" ")
            self._print_recursive(node.right)

binary_tree = BinaryTree()
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(8)

binary_tree.print_tree()
print()
binary_tree.insert(1)
binary_tree.insert(9)
binary_tree.print_tree()
print()
binary_tree.insert(10)
binary_tree.insert(0)
binary_tree.print_tree()
print()