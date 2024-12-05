def check_brackets(s):
    stack = []

    # Проверяем пункты 1 и 2
    if '(' in s or '[' in s or '{' in s:
        for a in s:
            if a == '(' or a == '[' or a == '{':
                stack.append(a)
            elif len(stack) > 0:
                last_opened = stack.pop()

                if a == ')' and last_opened != '(':
                    return False
                elif a == ']' and last_opened != '[':
                    return False
                elif a == '}' and last_opened != '{':
                    return False
            else:
                return False

        return True
    else:
        return False


# Чтение строки ввода и ответ
while True:
    input_string = input("Введите строку: ")
    if not input_string:
        print("Ошибка: Строка не может быть пустой.")
        continue
    result = check_brackets(input_string)

    if result:
        print("Строка существует")
    else:
        print("Строка не существует")