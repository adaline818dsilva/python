class Rect:
    prop1 = "sum of all "
    prop2 = "rectangle properties"

    def get_info(self):
        a = int(input("Enter length of rect: "))
        b = int(input("Enter breadth of rect: "))
        self.len = a
        self.breadth = b

    def area(self):
        print("Area:", self.len * self.breadth)


print("The rectangle properties")
print(Rect.prop1)
print(Rect.prop2)
a1 = Rect()
a2 = Rect()
a1.get_info()
a2.get_info()
a1.area()
a2.area()

   