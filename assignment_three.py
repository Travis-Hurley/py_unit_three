#travis Hurley - Oct/17/2022 - calculate surface area of prism

def intro():
    print("This program will calculate the surface area of any prism!")
    input("Enter anything to proceed >>")
    """Assigns variables to numbers from user"""
def length(length):
    length = int(input("What is the length of the prism? >>"))
    return length
def width(width):
    width = int(input("What is the width of the prism? >>"))
    return width
def height(height):
    height = int(input("What is the height of the prism? >>"))
    return height
"""calculates sides"""
def side1(length,height):
    rectangle_side1 = (length*height)*2

    return rectangle_side1
def side2(height,width):
    rectangle_base = (height*width)*2

    return rectangle_base
def side3 (width,length):
    rectangle_side2 =(width*length)*2

    return rectangle_side2
def combine():
    surfaceArea=side1+side2+side3
    return surfaceArea

def closing():
   print("The surface area of your prism is",combine())


intro()
length(length)
height(height)
width(width)
side1(length,height)
side2(height,width)
side3(width,length)
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