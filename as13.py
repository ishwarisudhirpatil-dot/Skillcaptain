x=5
y=5
print(id(x))
print(id(y))

y=10
print(id(x))
print(id(y))

nums=[1,2,3]
print(id(nums))
nums.append(4)
print(nums)
print(id(nums))

s="hi"
s=s+"there"
print(s)
print(id(s))

t=(1,[2,3])
t[1].append(4)
print(t)

print(True+True)
print(True*10)
print(False+5)
print(isinstance(True,int))
