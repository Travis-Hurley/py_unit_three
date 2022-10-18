#travis Hurley - Oct/18/2022 - calculate surface area of prism
import math
"""promps the user and describes program"""
def intro():
    print("This program will calculate the surface area of any prism!")
    input("Enter anything to proceed >>")

"""defines variables from user"""
def length():
    length = int(input("What is the length of the prism? >>"))
    return length
def width():
    width = int(input("What is the width of the prism? >>"))
    return width
def height():
    height = int(input("What is the height of the prism? >>"))
    return height
'''calculates the surface area'''
def calculate(a,b):
    surfaceArea =int(a*b)
    return surfaceArea
def surfaceArea(l,w,h):
    rectangle_base=calculate(l,w)
    rectangle_side=calculate(w,h)
    rectangle_back=calculate(h,l)
    total=(rectangle_back+rectangle_side+rectangle_base)*2
    return total
'''
intro()
a=length()
b=width()
c=height()
area=surfaceArea(a,b,c)
print("The total surface area is",area)
'''
def main():
    intro()
    a = length()
    b = width()
    c = height()
    area = surfaceArea(a, b, c)
    print("The total surface area is", area)
if __name__ == '__main__':
    main()