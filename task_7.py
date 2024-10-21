# Напишите функцию, которая проверяет является ли число
# палиндромом. Число передаётся в качестве параметра. Если
# число палиндром нужно вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна
# второй перевернутой части цифр. Например, 123321—
# палиндром(первая часть 123, вторая 321, которая после
# переворота становится 123), 546645 — палиндром, а 421987 —
# не палиндром.

def palindrom(number):

    if len(str(number)) % 2 != 0:
        print("Число определенно не палиндром")
    number_str = str(number)

    count = len(number_str)
    number_list = list(number_str)

    count_1 = int(count / 2)
    number_slice_1 = number_list[count_1:count]

    number_1 = ''.join(number_list[0:count_1])
    number_2 = ''.join(number_slice_1[::-1])

    if number_1 == number_2:
        print("Число палиндром")
    else:
        print("Число не палиндром")

number = int(input("Введите число"))
palindrom(number)