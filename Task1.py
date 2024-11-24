# Вводимо рядок
input_string = input("Введіть рядок: ")

# Знаходимо індекс останнього входження фрагмента "da"
last_index = input_string.rfind("da")

# Виводимо результат
print(f"Останній індекс входження 'da': {last_index}")
