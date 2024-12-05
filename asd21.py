try:
    result = eval(input("Ведите выражение: ")[:-1])
    print("Ответ:", result)
except ZeroDivisionError:
    print ("Не пытайся делить на 0.")
except SyntaxError:
    print ("Ваше выражение введено не коректно.")
except NameError:
    print("Буквы нельзя использовать в выражении")