# Функция для вычисления хеша
def hash_function(key, size):
    hash_value = 0
    for char in key:
        hash_value = (hash_value + ord(char)) % size
    return hash_value

# Чтение исходного файла
with open('хешишешиш.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Создание хеш-таблицы
hash_table_size = 50
hash_table = [[] for i in range(hash_table_size)]

# Наполнение хеш-таблицы
for word in text.split():
    key = word.lower()
    index = hash_function(key, hash_table_size)
    hash_table[index].append(word)


# Запись таблицы в результирующий файл
with open('хешрез2.txt', 'w', encoding='utf-8') as result_file:
    for i, values in enumerate(hash_table):
        result_file.write(f'Хеш {i}: {values}\n')

def check_word(word, text, hash_table, hash_table_size):
    in_text = word.lower() in [w.lower() for w in text.split()] # регистронезависимый поиск в тексте
    index = hash_function(word.lower(), hash_table_size)
    in_hash_table = word.lower() in [w.lower() for w in hash_table[index]] # регистронезависимый поиск в хеш-таблице

    return in_text, in_hash_table


# Пример использования функции проверки
word_to_check = input()
in_text, in_hash_table = check_word(word_to_check, text, hash_table, hash_table_size)

print(f"Слово '{word_to_check}' в тексте: {in_text}")
print(f"Слово '{word_to_check}' в хеш-таблице: {in_hash_table}")