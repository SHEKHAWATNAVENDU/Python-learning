# #t1=("nikhil",1,54,[1,25,5])
# # print(len(t1))
#  print(t1[3][1])
#type casting in tuple
# # # # #
# # # # # T1 =[1,3,54,5,5,6]
# # # # # print(type(T1))
# # # # # a=tuple(T1)
# # # # # print(a)
# # # # # print(type(a))
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # sum , min ,max
# # # #
# # # # t1 =  (1,3,54,5,5,7,6,8,8,67,8,8)
# # # # print(min(t1))
# # # # print(max(t1))
# # # # print(sum(t1[0:4:1]))
# # # #
# # # #
# # #
# # # t1=( 1,2.3,4,5,6)
# # # print(t1[1:4:1])
# # #
# #
# # fruits=["apple","banana","mango"]
# # fruits.replace("apple","app")
# # print(fruits)
#
# # mutability
# l1=[1,2,3,4,5,6,7,8,8]
# l1[1]=3
# print(l1)
#
# name= ("nikhil", "bittu")
# name[1]=("bittus")

#
# t1=(1,3,4,5,6,6,7,7)
# print(t1[0])

# Sets
# sets do not have the duplicate elements
#
# s1={"nikhil","bittu","jangid" , "jangid"}
# print(type(s1),s1)
#
# # if the duplicate element is present in the set the oly the one of them will be printed or considererd
# print(len(s1))


# membership in or notin

# s1={1,2,3,4,5,6}
# print(2 in s1)
# we cannot do the indexing and the slicing of the sets
# concatanation
#
# s2={7,8,9,0,}
# print(s1+s2)
# sets do not supports the concatanation

# mutability of set
#
# s1=set(input().split())
# print(s1)


# l1 = input("enter the list ").split()
# print(l1)

# #intersection in sets
# subjects1={"hindi","english","maths","bio"}
# subjects2={"hindi","english","maths","bio","cs"}
# subjects3={"hindi","english","maths","bio","sanskrit"}
#
# all_subjects=subjects1.union(subjects2).union(subjects3)
# print(all_subjects)
#
# common_subjects=subjects1.intersection(subjects2).intersection(subjects3)
# print(common_subjects)
#
# # so to avoid the long code we have & for the intersection and | for the union
#
# subjects1={"hindi","english","maths","bio"}
# subjects2={"hindi","english","maths","bio","cs"}
# subjects3={"hindi","english","maths","bio","sanskrit"}
#
# all_subjects=subjects1|subjects2|subjects3
# print(all_subjects)
# #
# common_subjects=subjects1 & subjects2 & subjects3
# print(common_subjects)


# dictionary

student = {"nikhil":20,"jangid":29,"rahul":16}
print(len(student))
print(student['nikhil'])

# values of the dictionary can be of any data type

d1 ={"nikhil":1,"name":"navendu","marks":{'eng':90.7 , 'math':89.7} }
print("marks of the  english is =  ",d1["marks"] ["eng"])
