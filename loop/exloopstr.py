'''
Problem:

name , daily working , weekly working days 
5 probability
'''

# criteria =  70 ghante , 1 month python 
#             50 ghante , 2 month python 
#             30 ghante , 3 month python
#             0 ghante , it will not happen in future

# kam loop ke bagair , loop

for i in range(0,3):
    name , workingdaysinweek, dailyworkinghours=input("Enter the details : \n").split(' ')
    weeklyhours=int(workingdaysinweek)*int(dailyworkinghours)
 
    if weeklyhours >= 70:
        print(f"There is a probability that {name} will cover python in 1 Month")
    elif weeklyhours == 50:
        print(f"There is a probability that {name} will cover python in 2 Month")
    elif weeklyhours == 30:
        print(f"There is a probability that {name} will cover python in 3 Month")
    else:
        print("Not happening")


