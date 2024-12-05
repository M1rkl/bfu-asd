class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Проверка скобок
def check_parentheses(string):
    balance = 0
    for char in string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

def prepare_string(string):
    if not check_parentheses(string):
        raise ValueError("Некорректная введена строка: Несоответствие открывающих и закрывающих скобок")
    string = string.replace(" ", "")
    return print_tree(string)[0]

# Строение дерева
def print_tree(string, index=0):
    if index >= len(string):
        return None, index

    value = ""
    while index < len(string) and (string[index].isdigit() or (string[index]=='-' and not value)):
        value += string[index]
        index += 1

    if not value:
        raise ValueError("Некорректное значение")

    node = Node(int(value))

    if index < len(string) and string[index] == '(':
        index += 1

        if string[index] != ',':
            node.left, index = print_tree(string, index)

        index += 1

        if string[index] != ')':
            node.right, index = print_tree(string, index)
        index += 1

    return node, index

# Поиск
def search_node(node, key):
    if not node:
        return False
    if key == node.value:
        return True
    elif key < node.value:
        return search_node(node.left, key)
    else:
        return search_node(node.right, key)

def insert_node(node, key):
    if not node:
        return Node(key)
    if key < node.value:
        node.left = insert_node(node.left, key)
    elif key >= node.value:
        node.right = insert_node(node.right, key)
    return node

def delete_node(node, key):
    if not node:
        return None

    if key < node.value:
        node.left = delete_node(node.left, key)
    elif key > node.value:
        node.right = delete_node(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left

        min_larger_node = find_min(node.right)
        node.value = min_larger_node.value
        node.right = delete_node(node.right, min_larger_node.value)
    return node

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

def tree_to_string(node):
    if not node:
        return ""
    left = tree_to_string(node.left) if node.left else ""
    right = tree_to_string(node.right) if node.right else ""
    if left or right:
        return f"{node.value} ({left},{right})"
    else:
        return f"{node.value}"


def menu():
    data = input("Введите дерево в линейно-скобочной записи: ")
    root = prepare_string(data)

    while True:
        print("\nМеню:")
        print("1. Поиск элемента")
        print("2. Добавление элемента")
        print("3. Удаление элемента")
        print("4. Выход")
        choice = input("Выберите операцию: ")

        if choice == "1":
            key = int(input("Введите ключ для поиска: "))
            found = search_node(root, key)
            print(f"Узел с ключом {key} найден" if found else f"Узел с ключом {key} не найден.")
        elif choice == "2":
            key = int(input("Введите значение для добавления: "))
            tree = insert_node(root, key)
            print(f"Узел с ключом {key} добавлен.")
        elif choice == "3":
            key = int(input("Введите значение для удаления: "))
            tree = delete_node(root, key)
            print(f"Узел с ключом {key} удален (если существовал).")
        elif choice == "4":
            print("Итоговое дерево:", tree_to_string(root))
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
menu()