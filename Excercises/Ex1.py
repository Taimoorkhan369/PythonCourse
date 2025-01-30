'''
String Class
    Implement all the methods present in string class
'''

#define
m="arham khan"

#accessing elements
print(m[0])

#slicing
print(m[0:5])

#step arguments
print(m[::-1])

#methods 
print(dir(str))

# upper,lower,title,count ,reverse,find

l="5"

print(l.isnumeric())
# print(l.find("a",4))


#if else
#for loop

n="arham khan"

# for i in n:
#     print(i)


'''
input - > string
print()
'''
m="arham"

m=input("Enter the name").split(' ')

j=' '.join(m)

m=["arham","khan","hassan"]

print(' '.join(m))
print(j)
