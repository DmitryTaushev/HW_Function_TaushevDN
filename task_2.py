# Напишите функцию, которая принимает два числа в качестве
# параметра и отображает все четные числа между ними



def oddnum(a , b):
    odd_number = []
    for num in range(a , b):
        if num%2 == 0:
            odd_number.append(num)
    print(odd_number)
a=10
b=20
oddnum(a,b)