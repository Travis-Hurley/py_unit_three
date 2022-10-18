#travis Hurley - Oct/17/2022 - calculate surface area of prism
import math
def intro():
    print("This program will calculate the surface area of any prism!")
    input("Enter anything to proceed >>")
    """Assigns variables to numbers from user"""
def length():
    length = int(input("What is the length of the prism? >>"))
    a=int(length)
    return a

def width():
    width = int(input("What is the width of the prism? >>"))
    b=int(width)
    return b
def height():
    height = int(input("What is the height of the prism? >>"))
    return height

def side1(a,b):
    rectangle_side1 = int(a)*2
    rec2=b*2
    both1=a*b
    return both1,rectangle_side1,rec2

"""
def side2(height,width):
    rectangle_base = (height*width)*2
    return rectangle_base
def side3(width,length):
    rectangle_side2 =(width*length)*2
    return rectangle_side2
def combine(x,y,z):
    surfaceArea=x+y+z
    return surfaceArea

def closing():
   print("The surface area of your prism is",combine(x,y,z))

"""
intro()
length()
height()
width()
side1(a,b)
"""
y=side2()
z=side3()
combine(x,y,z)
closing()
def main():
    intro()
    reciving_info()
    side1()
    side2()
    side3()
    closing()
    closing()

main()
"""