password = "ishu123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")
    if user_input != password:
        print("Wrong")

print("Successful")


a = int(input("enter the value of a"))
b= int(input("enetr the value of b"))
operation = "*"

match operation:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)