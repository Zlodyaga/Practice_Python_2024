# Вводимо рядок із дійсними числами через пробіл
input_string = input("Введіть дійсні числа через пробіл: ")

# Перетворюємо рядок у список чисел
numbers = list(map(float, input_string.split()))

# Знаходимо половини списку
half_length = len(numbers) // 2
first_half = numbers[:half_length]
second_half = numbers[-half_length:]

# Обчислюємо суми з точністю до сотих
sum_first_half = round(sum(first_half), 2)
sum_second_half = round(sum(second_half), 2)

# Виводимо результати
print(f"Сума першої половини: {sum_first_half}")
print(f"Сума другої половини: {sum_second_half}")
