# Чтение исходного файла
with open('хешишешиш.txt', 'r', encoding='utf-8') as file:
    text = file.read()
def hash_function(key, size):
    hash_value = 0
    for char in key:
        hash_value = (hash_value + ord(char)) % size
    return hash_value
def create_hash_table(words, table_size):
    hash_table = [None] * table_size

    for word in words:
        hash_code = hash_function(word,table_size)
        origin = hash_code

        while hash_table[hash_code] is not None:
            hash_code = (hash_code + 1) % table_size
            if hash_code == origin:
                raise Exception("Хеш-таблица переполнена")

        hash_table[hash_code] = word

    return hash_table


def write_hash_table(hash_table, output_file):
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for hash_code, values in enumerate(hash_table):
            result_file.write(f'Хеш {hash_code}: {values}\n')


def check_word(word, text, hash_table, table_size):

    in_text = word.lower() in [w.lower() for w in text.split()]
    hash_code = hash_function(word, table_size)
    origin = hash_code
    in_hash_table = False
    while hash_table[hash_code] is not None:
        if hash_table[hash_code] == word:
            in_hash_table = True
            break
        hash_code = (hash_code + 1) % table_size
        if hash_code == origin:
            break

    return in_text, in_hash_table

output_file ='хешрез.txt'
table_size = 106
words = text.split()
table = create_hash_table(words, table_size)
write_hash_table(table, output_file)
word_to_check = input()
in_text, in_hash_table = check_word(word_to_check, text, table, table_size)
print(f"Слово '{word_to_check}' в тексте: {in_text}")
print(f"Слово '{word_to_check}' в хеш-таблице: {in_hash_table}")