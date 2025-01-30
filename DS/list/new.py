print(dir(dict))

# l=[1,2,3,4,5,2,"arham"]
# a=l.pop(0)
# print(l)

# m=l.copy()
# print(m)

# print(m.count("arham"))

# print(m.index(3))
list1 = [1, 2]
list2 = [3, 4]
result = list1.__add__(list2)  # Output: [1, 2, 3, 4]
print(result)

my_list = [10, 20, 30, 20,20,20,20,20]
index = my_list.index(20,3)  # Output: 1
print(index)


d={}
a=d.fromkeys([1,2,3,4,5],0)
print(a)

d.clear()
my_dict = {"a": 1, "b": 2}
value = my_dict.get("a")  # Output: 1
# value = my_dict.get("c", "Not Found")  # Output: "Not Found"
print(value)