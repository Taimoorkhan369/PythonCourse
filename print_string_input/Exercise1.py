'''
print function -fstring
Q1: write a python code which will print something like this 
       The name of student is variable and the age is variable and the gender is variable
       The type of student is type and the type of age is type and the type of gender is type
       

Q2: "My name is Taimoor"
     python instruction : capitalize,lower,every char of each word will be capital
     python instruction : My name  , Taimoor , is , also in reverse order 
     python instruction : print -- 'My' count ,'taimoor' count  

Q3: take input of name , gender and age in six lines , three lines and one line
    the input which you take it will be error free

    string -input 
              
              the lower case of sting is : 
              the upper case of string is : 
              the title of string is : 
              starting three characters are: 
              reverse of string is : 
              
Q4: Take input from user name , and char 
       char: count of character in str
'''
name= "taimoor"
age= 21
gender="male"


# print("student name is "+name+"  age is "+str(age) +" gender is "+ gender +"")
# print(f"student name is {name} and age is {age} and gender is {gender}")
# print(f"{type(name)} and {type(age)} and{type(gender)}")
# print(type(age))
# print(type(gender))



# name= "My name is taimoor"
# reverse=name[: : -1]
# print(reverse)

# name_title=name.title()
# name_lower=name.lower()
# name_upper=name.upper()
# name_count=name.count("o")


# print(f" title of name {name_title} lower case of name {name_lower} uper case of name {name_upper} count of name {name_count}")

# reverse=name[: :-1 ]
# if name == reverse:
#     print("this is that name")
# else:
#     print("not that name")




# print("Enter your name")
# name=input()
# print("Enter your age")
# age=input()
# print("Enter your gender")
# gender=input()




# name=str(input("Enter your name\n"))
# age=int(input("Enter your age \n"))
# gender=str(input("Enter your gender\n"))




# string -input 
              
#               the lower case of sting is : 
#               the upper case of string is : 
#               the title of string is : 
#               starting three characters are: 
#               reverse of string is :

# name = str(input("Enter the string : \n"))

# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name[0:3])
# print(name[::-1])


name,char=input("Enter the name and character you want to count ").split(' ')
name=name.lower()
char=char.lower()
print(name,char)
print(name.count(char))


    
