import sys
from math import sqrt

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

def calculate_roots_of_quadratic_equation(a, b, c):
    root1_discriminant = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    root1_discriminant = (-b + sqrt(b**2 - 4*a*c))/(2*a)