my_variable = 'hello'
my_list_variable = ['hello', 'hi', 'nice to meet you'] # list
my_tuple_variable = ('hello', 'hi', 'nice to meet you') # tuple list (immutable, cannot be changed cant append)
my_set_variable = {'hello', 'hi', 'nice to meet you'} # set collection of unique and unordered elements


print(my_list_variable)
print(my_tuple_variable)
print(my_set_variable)

my_short_tuple_variable = ("hello",)
another_short_tuple_variable = "hello",

print(my_list_variable[0])
print(my_tuple_variable[0])
#print(my_set_variable[0])  # This won't work, because there is no order in a set. Which one is element 0?

my_list_variable.append('another string')
print(my_list_variable)

#my_tuple_variable.append('a string')  # This won't work, because tuple is immuatble a tuple is not a list.
my_tuple_variable = my_tuple_variable + ("a string",)
print(my_tuple_variable)
#my_tuple_variable[0] = 'can I change this?'  # No, you can't # cannoy change tuple it's immutable

my_set_variable.add('hello')
print(my_set_variable)
my_set_variable.add('hello')
print(my_set_variable)





# ======================

# Create a NEW Tuple by adding two tuples (my_tuple_variable reassigned new tuple)
print(my_tuple_variable)
my_tuple_variable = my_tuple_variable + (100,) # comma makes it a tuple (for 1 element its needed)
print(my_tuple_variable)


###### Set Operations

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print(set_one.intersection(set_two))  # {1, 3, 5} # elements that are in both, no duplicates

print({1, 2}.union({2, 3}))  # {1, 2, 3} all elements that are the same in both, no duplicates

print({1, 2, 3, 4}.difference({2, 4}))  # {1, 3}


