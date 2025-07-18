def circle():
    r=int(input("Enter radius of circle "))
    print("Area of circle is",3.14*r*r)

def rectangle(a, b):
    return a * b

def triangle():
    b = int(input("Enter base of triangle: "))
    h = int(input("Enter height of triangle: "))
    return 0.5 * b * h

def square(a):
    return a * a


while True:
    print("1. circle")
    print("2. rectangle")
    print("3. triangle")
    print("4. square")
    print("5. exit")

    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            circle()
        case 2:
            a = int(input("Enter length of rectangle: "))
            b = int(input("Enter breadth of rectangle: "))
            res = rectangle(a, b)
            print("Area of rectangle is", res)
        case 3:
            res = triangle()
            print("Area of triangle is", res)
        case 4:
            a = int(input("Enter side of square: "))
            res = square(a)
            print("Area of square is", res)
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")

              
                          
