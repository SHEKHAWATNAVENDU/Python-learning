import copy
# l1=[1,[1,2,3,4],'nikhil']
# #for shallow copy
# l2=copy.copy(l1)
# print(l2)
# print(id(l1))
# print(id(l2))

import copy

d1 = {
    "name": "Nikhil",
    "marks": {"eng": 12, "bio": 15}
}

d2 = copy.copy(d1)
d1["name"] = "Nikh"
d1["marks"]["bio"] = 100

print(d1)
print(d2)