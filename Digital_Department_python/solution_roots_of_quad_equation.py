import sys
from math import sqrt

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

def calculate_roots_of_quadratic_equation(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    while True:
        if a == '' and b == '' and b == '':
            print('Введите коэффиценты уравнения!')
            break
        elif not a.isdigit() and b.isdigit() and c.isdigit():
            print('Можно вводить лишь цифры!')
            break
        elif a == 'exit' or  b == 'exit' or  c == 'exit':
            break
        
        a = int(a)
        b = int(b)
        c = int(c)
        discriminant_in_power2 = b**2 - 4*a*c

        if discriminant_in_power2 > 0:
            root1_discriminant = (-b - sqrt(discriminant_in_power2))/(2*a)
            root2_discriminant = (-b + sqrt(discriminant_in_power2))/(2*a)
            print(int(root1_discriminant),'\n', int(root2_discriminant))
            break
        else:
            print('Введите другие коэффиценты')
            break

if __name__ == '__main__':
    calculate_roots_of_quadratic_equation(a, b, c)