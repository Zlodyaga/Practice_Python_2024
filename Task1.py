import math

# Введення чисел
a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))

# Обчислення модулів
mod_a = abs(a)
mod_b = abs(b)

# Середнє арифметичне
average_arithmetic = (mod_a + mod_b) / 2

# Середнє геометричне
average_geometric = math.sqrt(mod_a * mod_b)

# Виведення результатів
print(f"Середнє арифметичне модулів: {average_arithmetic:.5f}")
print(f"Середнє геометричне модулів: {average_geometric:.5f}")
