from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from scipy import special



def main():
    r = Rectangle("синего", 29, 29)
    c = Circle("зеленого", 29)
    s = Square("красного", 29)
    print(r)
    print(c)
    print(s)

    d = special.cosdg(0)
    print("cos(0) =", d)

if __name__ == "__main__":
    main()