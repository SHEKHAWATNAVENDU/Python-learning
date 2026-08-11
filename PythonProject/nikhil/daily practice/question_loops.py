# star printing
# ex .1

# for i in range(5):
#     for j in range(i+1):
#         print("*" , end="") # this we use because the star of the j does not go in next line
#     print() # this print is for the new line
#
# ex 2.
#
# for i in range(5):
#     for j in range(5):
#         print("*" ,end="")
#     print()

# ex .3
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#ex.4
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
#

# # ex . 5
# for i in range(5):
#     for k in range(5 - i):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("*", end="")
#     print()
#

# # ex.5
#
# for i in range(1 ,5):
#     for j in range(1 , i+1):
#         print(i,end="")
#     print()

# ex . 6  dice roll game
#
# import random
# print("enter the die rolling game ")
# while True:
#     user=input("press 'ok' start or 'q' to end the game ")
#     if user == 'ok':
#      print(random.randint(1,6))
#
#     elif user == 'q':
#         print("game is over ")
#         break

# ex . 7 we have the list of the country and we want to count the countries starting with the "i"
#
# l1 = ["india","iran","indonesia","pakistan","japan","america"]
# i=0
# while i< len(l1):
#     if l1[i][0]=="i":
#         print(l1[i])
#         i=i+1
# # ex.7 by for loop
# l1 = ["india", "iran", "indonesia", "pakistan", "japan", "america"]
# output=[]
# for i in range(len(l1)): # list ki sari value i mai assing ho jatti hai
#     if l1[i].startswith('i'):
#         output.append(l1[i])
#
# # print(output)
#
# # ex . 8
# user = {
#     'user_name': "nikhil",
#     'password': "tddakh@132",
#     'email': "shekhawatnavendu@gmail.com",
#     "address": "sikar",
#     'country': "indian"
# }
#
# i = 0
# sensitive_info = ["password", "address"]
#
# while i < len(sensitive_info):
#     if sensitive_info[i] in user: # in method in py is used to check that the element is present in collection
#         user.pop(sensitive_info[i])
#     i = i + 1
#
# print(user)

# ex . 9  number guessing game
# import random
#
# guessed =random.randint(0, 100)
# print(guessed)
#
# for i in range(10):
#     user = int(input("enter the number "))
#     if user==guessed:
#      print("congrates !!")
#      break
#      i = i +1
# print("next time")


user = {
     'user_name': "nikhil",
    'password': "tddakh@132",
    'email': "shekhawatnavendu@gmail.com",
   "address": "sikar",
    'country': "indian"
} 
i=0
sensitive_info=["password","address"]
while i<len(sensitive_info):
    if sensitive_info[i] in user:
        user.pop(sensitive_info[i])
