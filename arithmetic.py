def find(exp):
    operand = []
    operator = []
    priority = {'+': 1, '-': 1, '*': 2, '//': 2}
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            num = ""
            while i < len(exp) and exp[i].isdigit():
                num += exp[i]
                i += 1
            operand.append(int(num))
        elif exp[i] in priority:
            while (operator and
                   priority[operator[-1]] >= priority[exp[i]]):
                op = operator.pop()
                num2 = operand.pop()
                num1 = operand.pop()
                if op == '+':
                    operand.append(num1 + num2)
                elif op == '-':
                    operand.append(num1 - num2)
                elif op == '*':
                    operand.append(num1 * num2)
                elif op == '//':
                    operand.append(num1 // num2)
            operator.append(exp[i])
            i += 1
        else:
            i += 1  
    while operator:
        op = operator.pop()
        num2 = operand.pop()
        num1 = operand.pop()
        if op == '+':
            operand.append(num1 + num2)
        elif op == '-':
            operand.append(num1 - num2)
        elif op == '*':
            operand.append(num1 * num2)
        elif op == '//':
            operand.append(num1 // num2)
    return operand[0]


expression = "2+3*4"
result = find(expression)
print(result)  