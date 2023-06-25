# Напишите программу, которая принимает
# две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей.
# Для проверки своего кода используйте модуль fractions
import fractions

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 + f2)
print(f1 * f2)


def add(a, b):
    """Функция для сложения двух дробей"""
    num1, den1 = a.split('/')
    num2, den2 = b.split('/')
    lcm = int(den1) * int(den2) // gcd(int(den1), int(den2))
    num_sum = int(num1) * (lcm // int(den1)) + int(num2) * (lcm // int(den2))
    return f"{num_sum}/{lcm}"


def multiply(a, b):
    """Функция для умножения двух дробей"""
    num1, den1 = a.split('/')
    num2, den2 = b.split('/')
    num_product = int(num1) * int(num2)
    den_product = int(den1) * int(den2)
    if den_product % num_product == 0 and num_product != 1:
        den_product = den_product / num_product
        num_product = num_product / num_product
        return f"{int(num_product)}/{int(den_product)}"


def gcd(a, b):
    """Функция для нахождения наибольшего общего делителя"""
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


a = input("Введите первую дробь: ")
b = input("Введите вторую дробь: ")

sum_fraction = add(a, b)
product_fraction = multiply(a, b)

print(f"Сумма дробей {a} и {b} равна {sum_fraction}")
print(f"Произведение дробей {a} и {b} равно {product_fraction}")
