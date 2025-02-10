# '''
# data structure
# key value pairs
# '''

# #dictdefine
# m={}
# print(type(m))


# #initializing dict
# k={
#     1:"arham",
#     2:"hassan"
# }

# #accessing elements in dict
# print(k[1])


# #dictionary eng-urdu
# meaning={
#     "what":"kia",
#     "why":"kyun",
#     "who":"kon"
# }
# string=input("Enter the word i will tell you the meaning")
# print(meaning[string])

# #adding new element in dict
# meaning["when"]="kab"
# print(meaning)


# #updating new element in dict
# meaning["what"]="kia hua"
# print(meaning)


# m={[1,2,3,4]:2} -> int , string , list, dict float,double

#snake case writing -> variable dict define karna
english_to_urdu={
    "who":"kon",
    "what":"kia",
    "why":"kyun"
}

print(english_to_urdu)
#accessing elemnts
meaning=english_to_urdu["what"]
print(meaning)

# while True:
#     word =input("Enter the word I will tell you the meaning\n")
#     word=word.lower()

#     if word in list(english_to_urdu.keys()): 
#         print(english_to_urdu[word])
#     elif word not in list(english_to_urdu.keys()) and word != "exit":
#         #  True and True , 1 and 1 , 0 and 0 , 1 and 0 ,0 and 1 ->0 -> False
#         print("OOP's word is not present in our dictionary")
#     else:
#         break


#Dict new element



# keys=["or","if","go"]
# values=["yaa","agar","jao"]
# for i in range(len(keys)):
#     english_to_urdu[keys[i]]=values[i]

# print(english_to_urdu)

#update values 
english_to_urdu["what"]="kyun"
english_to_urdu["why"]="kia"
print(english_to_urdu)
   

#dict mutable 
# h="arham khan"
# a="r"+h[1:]
# print(a+b)

print(dir(dict))



#clear
new=english_to_urdu.copy()
english_to_urdu.clear()

#copy


#fromkeys
j={}
m=j.fromkeys([1,2,3,4,5,6,7],0)
print(m)

#get
print(new.get("why"))

#items
# k=new.items()
# print(k)
# print(type(k))

for key,value in new.items():
    print(key,value)

#deletion
new.pop("who")
print(new)


#dict loop
# l=["arham","khan"]
# for i in range(len(l)):
#     print(l[i])
# for i in l:
#     print(i)

l=[1,2,3,4]
m=[3,4,5,7]

# for i in l:          
#    for j in m:
#         print((j*i))

for i in new:
    print(i,new[i])

#keys
for key in new.keys():
    print(key,new[key])
        
#values
for value in new.values():
    print(value)
#items
for key,value in new.items():
    print(key,value)

#if else
for key in new:
    if key == "what":
        print("hello")
    else:
        print("fine")

d={
    "name":["arham","hassan","taimoor"],                                    
    "id":[1,2,3],                         
    "marks":[90,80,70]
} 

print(d["name"][0])
print(d["id"][0])
print(d["marks"][0])

for i in range(len(d["name"])):   
    print(d["id"][i],d["name"][i],d["marks"][i])

# import pandas as pd

# d={
#     "name":["arham","hassan","taimoor"],
#     "id":[1,2,3],
#     "marks":[90,80,70]
# }                                
# table=pd.DataFrame(d)


# table.to_csv("data.csv")