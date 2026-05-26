# map is a built function in python map() like len()

#syntax
# def map(func, iterable):
#     for x in iterabele:
#         func(x)

# memor efficient because it is lazy executed one by one after full computed
# it accept two iterable

#  map(func, iter1,iter2)


# it return iterator or map object
# faster than loop beafauce it execute in c language


# 1. square of list
nums=[1,20,2,40]
square_nums=list(map(lambda x:x**2,nums))
print(square_nums)

nums_char=['1','2','2']
print(list(map(int, nums_char)))

print(list(filter(lambda x:x%2==0,nums)))

# Step 1: Filter even numbers
# evens = filter(lambda x: x%2==0, nums)
# Step 2: Double them
# doubled = map(lambda x: x*2, evens)
# Step 3: Sum them
# from functools import reduce
# result = reduce(lambda x,y: x+y, doubled)
# ⚠️ Important Insight

# This chain works because:
# 👉 All are iterators (lazy)
# 👉 No extra memory used

# 🔚 Final Advice (Real-world thinking)

# Use:

# ✔ map() → simple transformation
# ✔ filter() → condition-based selection
# ✔ reduce() → aggregation

# Avoid:

# ❌ Overusing lambda
# ❌ Making code unreadable