'''
class str (string)
'''

#string defination

# '''',"""" not possible

name="tAimooR azam"


print(type(name))


#title 
name_title=name.title()
print(name_title)

# #lower 
name_lower=name.lower()
print(name_lower)

# #upper

name_upper=name.upper()
print(name_upper)

# #string slicing

print(name.count("t"))

#excercies

'''
t: 1
a:2
r:1
'''
# taimoor azam
# for charcters in name:
#     print(f"{charcters} : {name.count(charcters)}")

#split
# taimoor azam
print(name.split('a'))

# path="D:/python/p1.py"
# print(path.split('/')[-1])


#slicing -- step 

# print(name[: : -1])

# print(name*3)
# name.count('taimoor')

name="maham"

reverse=name[: :-1 ]

# if name == reverse:
#     print("This is that name")
# else:
#     print("not that name")
