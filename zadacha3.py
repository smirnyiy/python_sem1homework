# Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def FindCoordinatePlane (x,y):
    if x>0 and y>0:
        print(f"Точка с координатами: x = {x} y = {y} находится в первой четверти.")
    elif x<0 and y<0:
        print(f"Точка с координатами: x = {x} y = {y} находится в третей четверти.")
    elif x>0 and y<0:
        print(f"Точка с координатамиs: x = {x} y = {y} находится в четвертой четверти.")
    elif x<0 and y>0:
        print(f"Точка с координатами: x = {x} y = {y} lнаходится во второй четверти.")
    elif x==0:
        print(f"Точка с координатами: x = {x} y = {y} находится на оси Y.")
    elif y==0:
        print(f"Точка с координатами: x = {x} y = {y} находится на оси X.")

x = int(input("Введите координаты х: "))
y = int(input("Введите координаты у: "))
if x==0 and y==0:
    print("X и Y не должны быть равны 0! Попробуйте снова!")
FindCoordinatePlane(x,y)