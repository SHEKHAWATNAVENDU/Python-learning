# always check how many star we have to print in cloumn(j)




# # decreasing triangle
#
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# increasing triangle with the space

# for i in range(1,5):
#     for k in range(4-i):
#         print(" ",end="")
#
#     for j in range(i):
#            print("*",end="")
#     print()
#
# pyramid
#
# for i in range(1,6):
#     for k in range(5-i):# this for the space
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# hollow square

for i in range(5):
    for j in range(5):
        if i==0  or