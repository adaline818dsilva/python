class abc:
    def dis(self, a, b):
        self.a = a
        self.b = b
    def greet(self):
        print("Good Morning")

z = abc()
x = abc()
z.dis(20, 10)
x.dis(50, 70)
varsha = []
varsha.append(z)
varsha.append(x)
# Example: print stored values
for idx, obj in enumerate(varsha, 1):
    print(f"Object {idx}: a = {obj.a}, b = {obj.b}")



