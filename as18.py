secret_number = 15
guess = int(input("Enter the guess number: "))

if guess == secret_number:
    print("Correct")
elif guess > secret_number:
    print("High")
else:
    print("Low")



num =int(input("enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)