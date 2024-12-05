import re
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def parse_expression(expression):
    tokens = re.findall(r'\(|\)|,|\d+', expression)
    stack = []
    i = 0

    while i < len(tokens):
        token = tokens[i]
        if token.isdigit():  # Если токен является числом, создаем новый узел
            node = Node(int(token))
            stack.append(node)
        elif token == '(':
            pass  # Игнорируем открывающую скобку
        elif token == ')':  # При встрече закрывающей скобки завершаем текущий уровень
            right_child = stack.pop() if stack else None
            left_child = stack.pop() if stack else None
            parent = stack.pop() if stack else None

            if parent:
                parent.left = left_child
                parent.right = right_child
            else:
                # Если нет родителя, то левый ребенок становится новым родителем
                parent = left_child or right_child

            stack.append(parent)
        elif token == ',':  # Игнорируем запятую
            pass
        else:
            raise ValueError(f'Неверный символ в выражении: {token}')
        i += 1

    if len(stack) > 1:
        raise ValueError('Несоответствие открывающих и закрывающих скобок')

    return stack[-1] if stack else None

# Прямой обход родитель-левый потомок-правый потомок
def preorder(node):
    steps = []

    def preorder_recursive(node):
        if node:
            steps.append(node.data)
            if node.left:
                preorder_recursive(node.left)
            if node.right:
                preorder_recursive(node.right)

    preorder_recursive(node)
    return " ".join(map(str, steps))


# Центральный обход левый потомок-родитель-правый потомок
def inorder(node):
    steps = []

    def inorder_recursive(node):
        if node:
            if node.left:
                inorder_recursive(node.left)
            steps.append(node.data)
            if node.right:
                inorder_recursive(node.right)

    inorder_recursive(node)
    return " ".join(map(str, steps))


# Концевой обход левый потомок-родитель-правый потомок
def postorder(node):
    steps = []

    def postorder_recursive(node):
        if node:
            if node.left:
                postorder_recursive(node.left)
            if node.right:
                postorder_recursive(node.right)
            steps.append(node.data)

    postorder_recursive(node)
    return " ".join(map(str, steps))


drevo1 = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
drevo2 = "10 (, 14(13,))"
drevo3 = "5 (2 (1,"  # Неправильное количество скобок
drevo4 = "5 ) 2 (1,"  # Закрывающая скобка перед открывающей

try:
    root = parse_expression(drevo1)
    print("Прямой обход:")
    print(preorder(root))
    print("Центральный обход:")
    print(inorder(root))
    print("Концевой обход:")
    print(postorder(root))
except ValueError as e:
    print(f"Ошибка при разборе дерева: {e}")

