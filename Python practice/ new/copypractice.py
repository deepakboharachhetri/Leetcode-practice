
a=[1,2,3]

# b=a # same object 
# b.append(10)
# print("a","b",a,b)
# b[0]=12
# print("a","b",a,b)



import copy
# shallow copy -> new list same object references 
c=a.copy() 

# print("a","c",a,c)
c.append(12)
# print("a","c",a,c)
c[0]=99
# print("a","c",a,c)

# test 0 -> testing for nested list copy checking

d=[[1,2],[3,4]]
e=d.copy()
# print("d","e", d, e) #d e [[1, 2], [3, 4]] [[1, 2], [3, 4]]
e[0].append(199)
# print("d","e", d, e) #d e [[1, 2, 199], [3, 4]] [[1, 2, 199], [3, 4]]
e.append([5,6])
# print("d","e", d, e) #d e [[1, 2, 199], [3, 4]] [[1, 2, 199], [3, 4], [5, 6]]
e[0][0]=99
# print("d","e", d, e) # d e [[99, 2, 199], [3, 4]] [[99, 2, 199], [3, 4], [5, 6]]

# NOTE:
# A shallow copy creates a new list, but the references to nested items remain the same.
# So, modifying nested objects in the copied list will also affect the original list.
#
# If the list contains only primitive/simple values (not nested objects),
# a shallow copy is usually sufficient.

# To solve the nested copy problem, Python provides deepcopy().


# deepcopy 

f=copy.deepcopy(d)
print("d","f",d,f)
d[0].append(12)
print("d","f",d,f)
d[0][2]=88
print("d","f",d,f)

# d f [[99, 2, 199], [3, 4]] [[99, 2, 199], [3, 4]]
# d f [[99, 2, 199, 12], [3, 4]] [[99, 2, 199], [3, 4]]
# d f [[99, 2, 88, 12], [3, 4]] [[99, 2, 199], [3, 4]]