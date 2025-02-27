'''
what is set 
   -- set does not follow the order
   -- set is not subscriptable 
   -- set does not support repetition of elements
   -- set mutable
Define
  ----{1,2,3,4} -> set -> python builtin class -> data structure
Element access
  ---- we have to convert the set in list to access elements by index

operations
Methods 
Functions

For loop
If else
'''

#defination
m={1,2,3} 

#accessing elements
# print(m[0])

# print(set([1,2,4,5,5]))

print(list(m)[0])

for i in range(len(m)):
    print(list(m)[i])

for i in m:
    print(i)

id=[1,2,3,4,5]
name=["arham","hassan","taimoor","ali","rahdain"]

# for i in range(len(m)):
#     print(list(m)[i])

for i in name:
    print(f"name = {i}")

for i in id:
    print(f"id = {i}")

for i in range(len(name)):
    print(f"name={name[i]}, id={id[i]}")
# for i in range(10):
#     print(i)

# total_number=len([1,2,3,4,5])
# for i in range(total_number): 
#     print([1,2,3,4,5][

# k=["arham","taimmor","hassan"]
# for i in k:   
             
