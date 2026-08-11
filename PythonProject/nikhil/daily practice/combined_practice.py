# #  tuples  (tuples are immutable )
# from itertools import count
#
# t1 = (1,2,3,4,5,6,7,8,1,1)
# print(type(t1))
#
# # indexing in tuples
# print(t1[1])
#
# t2 = (1,2,3,4,5,6,7,8)
# print(t1+t2)
#
# print(t1.count(1))
#
# for i in range(1,5):
#     for j in range(i):
#         print ("*" , end="")
#     print()


t1=(25,36,48,59,60)

result=sum(t1)/len(t1)
print(result)
