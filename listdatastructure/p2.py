'''
Modifying List Data Structure
'''

'''
Insertion
   ---append
   ---insert
   ---extend
Deletion
   ---pop
   ---remove
   ---del
Sorting
'''

'''
Mutable
'''
# #insert , insert , append ,extend
My_List=["Banana","Mangoe","Apple","Orange"]
My_List.append("Cherry")
print(My_List)

#insert
My_List.insert(2,"potatoe")
print(My_List)

#extend

l1=[1,2,3,4]
l2=[5,6,7,8]

l1.extend(l2)


# '''
# Deletion
# '''
# #pop , del , remove

my_list=[1,2,3,4,5]
element=my_list.pop()
print(my_list)
print(element)

#remove
my_list.remove(1)
print(my_list)


del my_list[0]
print(my_list)



