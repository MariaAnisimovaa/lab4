def z1():
    n=int(input("Введите число "))
    if n % 3 == 0:
        print("делится")
    else:
        print("не делится")

def z2():
    try:
        n = int(input("Введите число "))
        o = 100 / n
    except ValueError:
        print("Ошибка. Введено не число")
    except ZeroDivisionError:
        print("Ошибка. Введён ноль")
    else:
        print("Результат деления:", o)

def z3():
    d=input("Введите дату (дд/мм/гггг) ")
    d1=d.split("/")
    if (int(d1[0])*int(d1[1])) == (int(d1[2][2:4])):
        print(d,"Магическая дата")
    else:
        print("Дата не магическая")



z3()
