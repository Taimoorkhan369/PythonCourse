'''
take input 
     name , age , salary
     output : if age is greater than 50 increase salary by 20 percent
     output : if age is less than 50 increase salary by 10 percent
     
'''
name,age,salary=input("name,age and salary").split(" ")
name,age,salary=str(name), int(age), int(salary)

if age>50:
    salary20=((salary/100)*20)+salary
    print(f"the salary of the people above 50 is increase by 20%\nbefore salary:{salary}\nafter increase:{salary20}")

elif age<50:
    salary10=((salary/100)*10)+salary
    print(f"the salary of the people below 50 is increase by 10%\nbefore salary:{salary}\nafter salary increase:{salary10}")

else:
    print("salary is not increase")