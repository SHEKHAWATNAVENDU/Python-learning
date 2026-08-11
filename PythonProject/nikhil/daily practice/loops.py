
# # for loop( we need for loop because if we want to print the multiple things so we can use the loops )
#
# marks =[20,21,33,34,23,43]
# for p in marks :  {Take each element from l1 one by one, store it in the variable i, and execute the loop body."}
#     print(p)

# for loop in string
#
# s1 =" my name is nikhil "
#
# for char in s1:
#     print(char)

# for loop in dic

# d1 = { "name ": "nikhil", "age": 85,"class":'B'}
# for i in d1.items(): # in this step this dic will give output in tuple , each pair in diff line
#     print(i[0],i[1]) #

# range () ex . printing 1 to 100 counting
# start = (input("!"))
# if start== 'go':
#     for i in range(1,100,1):
#         print(i)



# even number between 1 to 20
#
# for i in range(2,20,2):
#     print(i)



#reverse order
# for i in range (20,1,-1):
#     print(i)





# countdown

# button = input("wirtre ok > ")
# if button =="ok":
#     for i in range(10,1,-1):
#         print(i)
#
# print("happy birthday rahul")





# writing the elements of the collections with their  index

# names = ["nikhil",'bittu','jangid','rahul']
# for i in range(len(names)):
#     print(i,names[i]) # for revising again chatgpt
#

# printing key value both by the for loop in dic
#
# d1= {1:20,2:29,3:34,4:43}
# for i in d1:
#     print(i,d1[i])

# sum of the element by thew for loop
#
# l1 = [1,22,3,33,44,43,6,3]
# total = 0
# for i in l1:
#     total = total + i
#
# print(total)


# highest of all element
# *****
# l1 = [2,3,33,4,55,4,1]
# highest =l1[0]
# for i in l1:
#     if highest <i:
#         highest = i
# print(highest)

# same we can find for the smallest


# use of continue and break
#
# for i in range(10):
#     if i%2==0:
#      break
#

# while loop
# ex .1
# num= 1
# while num < 5:
#     print(num)
#     num = num+1
# ex .2 # first we need intialization in loops
# correct_password= ("nikhil")
# while True:
#     user_pass=input("enter the user pass")
#     if user_pass == correct_password:
#         print("password is correct ")
#         break

# now for the 5 time only we can try pass
#
# correct_password = ("nikhil")
# num = 0
# while num<5:
#     user_pass = input("enter the user pass")
#     if user_pass == correct_password:
#         print("password is correct ")
#         break
#
#
#     else:
#         print("wrong pass")
#         num = num + 1
#

# example writing the program for the above q . in for loop
# correct= "nikhil"
# for i in range(5):
#     user = input("enter the pass ")
#     if correct==user:
#         print("correct pa")
#
#     else:
#         print("wrong")
#


# import random
# print(random.randint(5,65))

