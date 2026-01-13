count =1
while count<=10:
    print(count)
    count +=1


num=5
for i in range(1,11):
   print(num,"x",i ,"=",num*i)

total=0
for i in range(1,100):
  total=total +i
print("total",total)


text="pyhton is fun"
words=text.split()
for word in words:
  print(words)

secret_number =7
guess= int(input("enter the guess no"))
while guess != secret_number:
    print("wrong guess try again")
guess=int(input("enter the guess no"))
print( "congrats you guess the secert number")
    

for i in range(1, 6):         
    for j in range(i):        
        print("*", end="")
    print()           



