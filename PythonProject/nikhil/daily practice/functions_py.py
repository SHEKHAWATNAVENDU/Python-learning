# # user defined function
# def greeting_note(name):
#     print(f"hello how are you {name}! ")
#
# greeting_note("nikhil")

# create a function for , a no. is odd or even
# def odd_even(num):
#     if num%2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# odd_even(5)

# value returning in py example
#
# def arithmetic(num1 , num2):
#     a=num1+num2
#     b=num1-num2
#     c=num1*num2
#     d=num1/num2
#     return a,b,c,d
# val1=int(input("enter the value of the num1 "))
# val2=int(input("enter the value of num2 "))
# res1,res2,res3,res4=arithmetic(val1,val2) # we called the function in this line
# print(f"addition of the {val1} and {val2} is {res1} ")
# print(f"subtraction  of the {val1} and {val2} is {res2} ")
# print(f"multiplication of the {val1} and {val2} is {res3} ")
# print(f"dividation of the {val1} and {val2} is {res4} ")
#
#

# kwargs ex.1
#
# def details(**kwargs):
#     for key, value in kwargs.items():
#         print(key,":",value)
# details(name="navendu",age=21)
# print(type(details))

# ex.2
#
# def student_detail(**kwargs):
#
#         if   "age" in kwargs : # used membership function`
#             print("key foud")
#         else:
#             print("key not found")
# student_detail(name="nikhil",height="6ft")
#

# docstring : this means it tells every thing about the function what is happening in docstring .
#
# def student_info(name,age,add):
#     """
#     print("the name of the student is : {name}")
#     print("the age of the student is : ")
#     print("the add of the student of is :")
#     return : null
#     """
#
# help(student_info)

# # ex factorial using loop
# result = 1
# for i in range(5,1,-1):
#     result = result*i
# print(result )
#

# # factorial by the while loop
# i = int(input("enter the value of the i"))
# result=1
# while i>1:
#     result=result*i
#     i=i-1
# print(result)
#
# # recursion
# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         factorial=num* fact(num-1)  # return value is usually stored in the variable that receives the function call.
#         return factorial
# result=fact(4)
# print(result)


# # ex2  printing counting from 1 to 100
#
# def counting(num):
#     if num==100:
#         return
#     else:
#         print(num)
#         counting(num+1)
#
# counting(1)
# function as the argument
# def add(number):
#     return number +1
#
# def square(number):
#     return number**2
# print(square(add(4))
#       )
def greet():
    print("hello")
def execute(func):
    func
print(execute(greet()))