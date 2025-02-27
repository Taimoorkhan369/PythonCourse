m=(1,2,3,4,5,1)

'''
tuple     list     set 
immutable mutable mutable
'''
#access
print(m[0:3])

#methods
print(dir(tuple))

#count
a=m.count(1)
print(a)

#index
print(m.index(1))

for i in m:
    print(i)

for i in range(len(m)):
    print(m[i])

if m[0] > m[1]:
    print("First element is greater")
else:
    print("second element is greater")

m=()
m=list(m)
for i in range(1,11):
    m.append(i)

m=tuple(m)
print(m)


sequence=input("Enter the sequence of numbers \n")

'''
Data structure speed
   speed : tuple < set < list
      --insertion 
      --deletion
      --update
      --traverse
'''

import time

print(time.time)


l=[1,2,3,4]
k={1,2,3,4,5}
m=(1,2,3,4,4)

print(time.time())
for i in l:
    print(i)
print(time.time())

print(time.time())
for i in k:
    print(i)
print(time.time())

print(time.time())
for i in m:
    print(i)
print(time.time())

m=[]
for i in range(1,10000000):
    m.append(i)


