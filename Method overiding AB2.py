class A:
    def show(self):
        print("hello")
class B(A):
            def show(self):
                print("Today is day 8")
s=A()
s1=B()
s.show()
s1.show()               