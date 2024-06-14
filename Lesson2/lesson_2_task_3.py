import math

def square(сторона):
    if not isinstance(сторона, int):
        side = math.ceil(сторона)
    
    площадь = сторона * сторона
    return площадь

сторона_string = input("Введите длину стороны квадрата: ")
сторона_length = float(сторона_string)
result = square(сторона_length)
print(f"Площадь квадрата со стороной {сторона_length} равна {result}")