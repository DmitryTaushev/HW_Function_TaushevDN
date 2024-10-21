# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата,
# символ и переменную логического типа:
# если она равна True, квадрат заполненный;
# если False, квадрат пустой.

def pic_square():
    len = int(input("Введите длину стороны квадрата"))
    symbol = input('Введите символ из которого будет состоять квадрат')
    condition = input("Введите True - если квадрат должен быть заполненым, False, если пустым")
    space = ' '
    if condition == "True":
        for i in range(len):
            print(len*symbol)
    elif condition == "False":
        print(len * symbol)
        for i in range(len-2):
            print(symbol + space*(len-2) + symbol)
        print(len * symbol)

pic_square()


