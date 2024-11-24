# Вводимо рядок з арифметичною операцією
expression = input("Введіть вираз (додати або відняти два числа): ")

# Видаляємо пробіли
expression = expression.replace(" ", "")

# Визначаємо операцію і обчислюємо результат
if "+" in expression:
    a, b = map(int, expression.split("+"))
    result = a + b
elif "-" in expression:
    a, b = map(int, expression.split("-"))
    result = a - b
else:
    result = "Невірний формат виразу"

# Виводимо результат
print(f"Результат: {result}")
