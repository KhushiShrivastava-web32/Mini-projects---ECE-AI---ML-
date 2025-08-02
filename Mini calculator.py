a = float(input("Enter a number \n"))
b= float(input("Enter another number \n"))

Oper = input("Which operation you want to perform on these two numbers ? ")

if Oper == "+":
    print("The sum of two numbers is = ", a+b)
elif Oper =="-":
    if a>b:
        print("Result = ", a-b)
    else:
        print("Result =  -", b-a)
elif Oper == "×" or Oper == "*":
    print("The product of two numbers is =",a*b)
elif Oper == "÷" or Oper == "/":
    if a>b:
        print("Result =", a/b)
    else :
        print("Not possible as ", a ,"is less than ", b)
else:
    print("Invalid input")
