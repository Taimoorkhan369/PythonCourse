'''
input -> string , sequence , int "123456" -> int {} add
20 -> superset
metehods implement
'''
# u={1,2,3,4,5,6,7,8}
# l=input("enter a number")
# print(l)
# m={1}
# for i in l:
#     print(int(i))
#     m.add(int(i))
# print(dir(set))
# set=m.issubset(u)
# print(set)

# super=u.issuperset(m)
# print(super)

# diff=m.difference(u)
# print(diff)

# pip=m.pop()
# print(pip)
# print(m)

# union=m.union(u)
# print(union)

# dis=m.discard(3)
# print(dis)
# print(m)
# joint=m.isdisjoint(u)
# print(joint)
# update=m.intersection_update(u)
# print(update)

'''
write a python code that will take two number as input
print their sum subtract multiply and division

write a python code that will take a string as input
apply for loop to print each character and its count

wirte a python code that will take three inputs 
and then append them to a list

write  a python code that will print table 
   - take number as input and print the table of it 

write a python code that will take age as input
   - then apply if age > 20 , allow
     if age<20 unerage
     if age > 70 above age
'''


# num1,num2=(input("enter the num1")).split(" ")   
# sum1=int(num1)+int(num2)
# print(sum1)

# multiple=int(num1)*int(num2)
# print(multiple)

# substract=int(num1)-int(num2)
# print(substract)

# divide=int(num1)/int(num2)
# print(divide)


sequence=input("Enter the Sequence \n")

try:
    print(f"Executing append number function as sequence does not contains any characters\n{[int(number) for number in sequence]}")
except Exception as e:
    print("Executing Character Count logic as Sequence contain characters")
    tenp=[]
    for char in sequence:
        if char not in tenp:
          print(f"{char} = {sequence.count(char)}")
          tenp.append(char)


list=[]
id,name,marks=input("Enter the info").split(" ")
mark=int(marks)
list.append(id)
list.append(name)
list.append(mark)
print(list)
   
