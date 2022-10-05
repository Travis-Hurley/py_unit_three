# Start writing your functions below this line


def top_egg():
    print("  _________")
    print(" /         \\")
    print("/           \\")

    # all of your function calls should go here. Remove the word "pass" before adding function calls.
def bottom_egg():
    print("\\           /")
    print(" \\         /")
    print("  ---------")
def line():
    print("-\"-\'-\"-\'-\"-\"-")
def egg():
    top_egg()
    bottom_egg()
def main():
    egg()
    line()

    egg()
    line()
    bottom_egg()

    top_egg()
    line()
    bottom_egg()

if __name__ == '__main__':
    main()