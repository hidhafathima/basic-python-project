print("Simple calculator\n")
num1=float(input("Enter the first number:\n"))
num2=float(input("Enter the second number:\n"))
oper=input("Enter an operator from '+','-','*','/':\n")
if oper== "+":
    result=num1+num2
elif oper== "-":
    result=num1-num2
elif oper== "*":
    result=num1*num2
elif oper== "/":
    result=num1/num2
else:
    print("Invalid operator")
print("Result is:",result)


