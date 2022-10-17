#travis Hurley - Oct/17/2022 - calculate surface area of prism

def intro():
    print("This program will calculate the surface area of any prism!")
    input("Enter anything to proceed >>")
    """Assigns variables to numbers from user"""
def length(length):
    l = int(input("What is the length of the prism? >>"))
    return l
def width(width):
    w = int(input("What is the width of the prism? >>"))
    return w
def height(height):
    h = int(input("What is the height of the prism? >>"))
    return h
    """calculates sides"""


def side1(l,h):
    rectangle_side1 = (length(l)*height(h))*2
    return rectangle_side1
def side2(h,w):
    rectangle_base = (height(h)*width(w))*2
    return rectangle_base
def side3 (w,l):
    rectangle_side2 =(width(w)*length(l))*2
    return rectangle_side2
def combine():
    surfaceArea=side1+side2+side3
    return surfaceArea
def closing():
   print("The surface area of your prism is",combine())


intro()
length()
height()
width()
side1()
side2()
side3()
combine()
closing()

"""
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