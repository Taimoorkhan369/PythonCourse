# '''
# Methods
# '''
# m={1,2,3,5}
# print(dir(m))

# #operations on sets
# '''
# Insertion
# Deletion
# Updation
# '''

# my_first={i for i in range(1,11)}

# #add
# my_first.add(11)
# print(my_first)

# #delete
# deleted_element=my_first.pop()
# print(deleted_element)
# print(my_first)

# #remove
# my_first.remove(5)
# print(my_first)

# #third operation -> update

# my_first.update([1,2])
# print(my_first)

# # iterable non iterable -> loop sequence indexes

# # l=[1,2,3,4]
# # m={1,2,3,4}
# # m=(1,2,3,4)
# # k="arham khan"

# # i=12
# # i=0.2
# # n={"ah":12}

# new=my_first.copy()
# print(new)

# #clear
# new.clear()
# print(new)

# #union
# a={1,2,3,4}
# b={5,6,7,8,1}
# union=a.union(b)
# print(union)
# print(b.union(a))

# #intersection
# print(a.intersection(b))

# #difference
# print(a.difference(b))

# #symmetricdifference
# print(a.symmetric_difference(b))

# #symmetricdifferenceupdate
# a.symmetric_difference_update(b)
# print(a)

# U={1,2,3,4,5,6,7,9,10}
# A={1,2,3,4}

# print(A.issubset(U))
# print(U.issuperset(A))
# print(a.isdisjoint(b))
# print(dir(set))

m={1,2,"arham"}
for i in m:
    print(i)