rows = int(input("Enter the number of rows: "))
num = 1

for i in range(1, rows + 1):
    if i % 2 == 1:
        for j in range(1, i + 1):
            print(num, end="")
            if j < i:
                print(" * ", end="")
            num =num+ 1
        print()
    else:
        temp = num + i - 1
        for j in range(i):
            print(temp, end="")
            if j < i - 1:
                print(" * ", end="")
            temp =temp - 1
        num =num + i
        print()


