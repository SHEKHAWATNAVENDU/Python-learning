# # a = input("enter the side a: ")
# # b = int(input("enter the side b: "))
# # c = input("enter the side c: ")
# # a=int(a)
# #
# # c=int(c)
# # s= ( a + b +c)/2
# # area = s*(s-a)*(s-b)*(s-c)**0.5
# # print("area of the triangle is ",area)
# num=input("enter the number")
# print(len(num))
p =int(input("enter the value of initial amount"))
r=int(input("enter the value of rate"))
t=int(input("enter the value of time"))
a=p*(1+(r/100))**t
ci=a-p
print(ci)