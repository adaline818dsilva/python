def hello(n):
    return n + 2

def hai(n):
    a = hello(n - 1)
    if n == 2:
        return "End"
    b = hello(n - 2)
    print("hai")
    print(a)
    return hai(n - 1) 

print(hai(5))
