marks= int(input("Enter the marks"))
if marks >=40:
   print("pass")
else:
   print("fail")

num= int(input("enter the number"))
if num%2==0:
   print("even")
else:
   print("fail")

num1=int(input("enter the first value"))
num2=int(input("enter the second value"))
operator = input("Enter operator (+, -, *, /) ")
if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")


age =int(input("enter the age"))
if age <13:
  print("child")
elif 13 < age >19:
   print("teenager")
elif 20> age <59:
   print("adult")
else:
   print("senior")


