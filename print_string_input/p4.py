'''
input function 
'''
print("Enter your name")
name=input()
print("Enter your age")
age=input()
print("Enter your gender")
gender=input()


name=str(input("Enter your name\n"))
age=int(input("Enter your age\n"))
gender=str(input("Enter your gender\n"))

name,age,gender =input("Enter your name ,age and gender").split(' ')
print(f"name of student is {name} and age is {age} and gender is {gender}")

name=str(input("Enter the name which you want to print the count"))

for char in name:
    print(f"{char} : {name.count(char)}")


name,age,gender=input("Enter your name , age and gender (include space between)").split(' ')

print(f"the name of student is {name.title()} and age is {age} and gender is {gender.upper()}")