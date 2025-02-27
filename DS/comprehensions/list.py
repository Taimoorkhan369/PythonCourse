'''
List Comprehensions
'''

'''
sequence input 1223455 int list append (manually) -> comprehension
sequence input 1234556 int square append(manually) -> comprehension
sequence input 1234455 int check odd square append (manually) -> comprehension
'''
# list=[]
# sequence=input("enter the numbers")
# # for i in sequence:
# #     list.append(int(i))
# # print(list)
# import math

# print([int(i) for i in sequence])
# print([int(i)**2 for i in sequence])
# print([int(i)**2 for i in sequence if not int(i)%2==0])

# print([round(math.sqrt(int(i)),2) for i in sequence])



# main=[i for i in range(1,101)]
# odd=[num for num in [i for i in range(1,101)] if num%2!=0]
# even=[num for num in [i for i in range(1,101)] if num%2==0]
# for num in main:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)
# print(odd,even)
main=[[num for num in [i for i in range(1,21)] if num%2!=0],[num for num in [i for i in range(1,21)] if num%2==0]]
print(main)






def return_list():
    return [i for i in range(1,11)]
def odd_checker(number):
    return number%2!=0
def even_checker(number):
    return number%2==0

