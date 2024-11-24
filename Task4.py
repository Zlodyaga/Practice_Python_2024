# Функція y(x) на основі наданого графіка
def y(x):
    if x >= 4:
        return 1
    elif 2 <= x < 4:
        return x**3 - x**2
    elif 1 <= x < 2:
        return x**2 + x
    else:
        return -1

# Введення значення x
x = float(input("Введіть аргумент x: "))

# Обчислення значення функції
result = y(x)

# Виведення результату
print(f"Значення функції y(x): {result:.2f}")
