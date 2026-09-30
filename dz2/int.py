def square():
    return int(input("Введіть число: ")) ** 2

print(square())


def add():
    return int(input("Введіть перше число: ")) + int(input("Введіть друге число: "))

print(add())

def division():
    z = int(input("Введіть друге число: "))
    x = int(input("Введіть перше число: "))
    return divmod(x, z) if z != 0 else 'На нуль ділити не можна'

print(division())