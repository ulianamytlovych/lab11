import math

def calculate_trigonometric_expression(n: int, x: float) -> float:
    if n == 1:
        return math.sin(x) * math.cos(x)
    elif n == 2:
        return math.sin(x**2) + math.cos(x)
    else:
        return 1 - math.sin(x)


n = int(input("Введіть значення n (): "))
x = float(input("Введіть значення x (в радіанах): "))

result = calculate_trigonometric_expression(n, x)
print(f"Результат: {result}")
