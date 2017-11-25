def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

print(methodception(add_two_numbers))

# ============================

print(methodception(lambda: 35 + 17))

answer = (lambda x: x*3)(5)
print(answer)

my_list = [13, 56, 77, 484]
# A lambda function is just a short, one-line function that has no name (anonymous)

# filter() passes each element of my_list as a parameter to the function.
# here filter takes a function, and a list
# for each x in list, return x where x!=13
temp = list(filter(lambda x: x != 13, my_list))
print(temp)


# or without lambda:

def not_thirteen(x):
    return x != 13

list(filter(not_thirteen, my_list))

# or can use list comprehension (might have slightly better performance), but filter is used in other languages(more familiar to others)


