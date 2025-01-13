'''
F string -- String Formatting 
'''
name = "taimoor"
age = 22

age=age-2
print(age)
# print(type(name))
# print(type(age))
# the name of student is taimoor and age of student is 22

# print("student name is"+name+"and age is "+str(age))

# print("student name is" +name +"and age is" +str(age))

print(f"student name is {name} and age is {age}")

final=f"student name is {name} and age is {age}"
print(final)

'''
method -- class dependent
function -- global functions
'''

l=[1,2,3,4]
l.pop(1)
print(l)
# sum(1,2,3,4)
# str int sum avg functions 

# a=[1,2,3,4,5]
# a.pop()
# a.remove()
# a.insert()

# a=6
# b="ab"

# print(f"type of b is {type(b)},type of a is {type(a)}")

print(dir(str))

l=["1","2","3"]

l="my name is arham khan"
