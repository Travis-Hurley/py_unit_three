#travis Hurley - Oct/13/2022 - calculate surface area of prism
def main():

    print("This program will calculate the surface area of any prism!")

    """assigns numbers to the variables from user"""
    l = int(input("What is the length of the prism? >>"))
    w = int(input("What is the width of the prism? >>"))
    h = int(input("What is the height of the prism? >>"))
    """calculates sides"""
    rectangle_side1= (l*h)*2
    rectangle_base = (h*w)*2
    rectangle_side2 =(w*l)*2
    """adds them for surface area"""
    surface_area=rectangle_base+rectangle_side2+rectangle_side1
    print(surface_area)

main()

