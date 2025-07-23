class Rect:
    def set_dim(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

nums = []
d = int(input("Enter number of rectangles: "))
for i in range(d):
    R = Rect()
    a = int(input(f"Enter the length of Rectangle {i+1}: "))
    b = int(input(f"Enter the breadth of Rectangle {i+1}: "))
    R.set_dim(a, b)
    nums.append(R)

for idx, rect in enumerate(nums, 1):
    print(f"Area of Rectangle {idx}: is {rect.area()}")
  
