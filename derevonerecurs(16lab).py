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
#Не рекурсирный обход
def preorder_iterative(node):
    steps = []
    stack = [node]

    while stack:
        current = stack.pop()
        if current:
            steps.append(current.data)
            stack.append(current.right)  # Добавляем правый потомок в стек ПЕРВЫМ.
            stack.append(current.left)  # Добавляем левый потомок в стек ВТОРЫМ.

    return " ".join(map(str, steps))


drevo1 = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
drevo2 = "10 (, 14(13,))"
drevo3 = "5 (2 (1,"  # Неправильное количество скобок
drevo4 = "5 ) 2 (1,"  # Закрывающая скобка перед открывающей

try:
    root = parse_expression(drevo4)
    print("Прямой обход:")
    print(preorder_iterative(root))
except ValueError as e:
    print(f"Ошибка при разборе дерева: {e}")
