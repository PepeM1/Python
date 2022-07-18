
print("enter three numbers to see which is the largest")
num1 = (float(input("input the first number: ")))
num2 = (float(input("input the second number: ")))
num3 = (float(input("input the third number: ")))
if (num1>=num2 and num1>=num3):
    print(str(num1) + " is the largest numbeer")
elif (num2>=num1 and num2>=num3) :
    print(str(num2) + " is the largest number ")
else:
    print (str(num3) + " is the largest number")
