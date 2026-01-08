a=10
b=0

try:
   result=a/b
   print("result:",result)
except ZeroDivisionError:
   print("Error: Division by zero is not allowed.")

