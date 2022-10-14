#travis Hurley - Oct/13/2022 - calculate surface area of prism

def intro():
    print("This program will calculate the surface area of any prism!")
    input("Enter anything to proceed >>")
    """Assigns vaiables to numbers from user"""
def reciving_info():
    l = int(input("What is the length of the prism? >>"))
    w = int(input("What is the width of the prism? >>"))
    h = int(input("What is the height of the prism? >>"))
    """calculates sides"""
    ll = l
    ww = w
    hh = h
def side1(ll,hh):
    rectangle_side1 = (ll*hh)*2
    return rectangle_side1
def side2(hh,ww):
    rectangle_base = (hh*ww)*2
    return rectangle_base
def side3 (ww,ll):
    rectangle_side2 =(ww*ll)*2
    return rectangle_side2
def combine():
    surfaceArea=side1+side2+side3
    return surfaceArea
def closing():
   print("The surface area of your prism is",combine())
intro()
reciving_info()
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