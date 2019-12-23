"""
Знайти добуток усіх цілих чисел,що лежать у діапазоні між 2 дійсними числами
"""



num1 = float(input("num1="))
num2 = float(input("num2="))
num_1 = int(num1)
num_2 = int(num2)
import math
if num_1 > num_2:
        result = math.factorial(num_2)
        print(result)
else:
        result = num_1, num_2
        print(result)


