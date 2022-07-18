print("Enter a number, operator and another number")
num1 = float(input("what is the first number: "))
op = input("what is the operator symbol: ")
num2 = float(input("what is the second number: "))
if (op=="+"):
    print(num1+num2)
elif (op=="-"):
    print(num1-num2)
elif (op=="*"):
    print(num1*num2)
elif (op=="/"):
    print(num1/num2)
elif (op=="//"):
    print(num1//num2)
elif (op=="%"):
    print(num1%num2)
elif (op=="**"):
    print(num1**num2)
else:
    print("invalid operator")
  