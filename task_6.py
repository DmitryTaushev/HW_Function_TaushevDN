# Напишите функцию, которая считает количество цифр в числе.
# Число передаётся в качестве параметра. Из функции нужно
# вернуть полученное количество цифр. Например, если
# передали 3456, количество цифр будет 4.

def count_num(i):
    num = len(i)
    print(num)
i = input("Введите число")
count_num(i)