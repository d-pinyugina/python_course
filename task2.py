
# 1
def function(number1, number2, op):
    op = op.strip()
    if op == '+':
        return number1 + number2
    elif op == '-':
        return number1 - number2
    elif op == '*':
        return number1 * number2
    elif op == '/':
        return number1 / number2
    else:
        return "Неизвестная ошибка"


print(function(10, 5, '+'))


# 2
# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево. (довод там и т.п.)
def is_palindrome(word):
    if word == word[::-1]:
        print("Это палиндром")
    else:
        print("Не палиндром")


print(is_palindrome("довод"))

# 3 Есть список a = [0, 4, 78, 2, 1, 1, 13, 21, 34, 55, 89, 167]
# Выведите все элементы, которые меньше 5

a = [0, 4, 78, 2, 1, 1, 13, 21, 34, 55, 89, 167]
for i in range(len(a)):
    if a[i] < 5:
        print(a[i])
