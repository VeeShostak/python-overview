# A decorator is just a function that gets called before another function
# can pass in users permissions to decorator, if no match, fonts show admin page,
# insert elements to db that match certain criteria

import functools  # function tools

# define decartotor
def my_decorator(f):
    @functools.wraps(f)
    def function_that_runs_f():
        print("Hello!")
        f()
        print("After!")
    return function_that_runs_f

# apply the defined decorator
@my_decorator
def my_function():
    print("I'm in the function.")

my_function()


### ====================


def my_decorator(f):
    @functools.wraps(f)
    def function_that_runs_f(*args, **kwargs):
        print("Hello!")
        f(*args, **kwargs)
        print("After!")
    return function_that_runs_f

# apply the defined decorator
@my_decorator
def my_function(arg1, arg2):
    print(arg1 + arg2)

my_function(56, 89)



### =============
# morre complex. decorator accept arguments itself

def decorator_arguments(number):
    def my_decorator(f):
        @functools.wraps(f)
        def function_that_runs_f(*args, **kwargs):
            print("Hello!")
            if number == 56:
                print("Not Running!")
            else:
                f(*args, **kwargs)
            print("After")
        return function_that_runs_f
    return my_decorator

# apply the defined decorator
@decorator_arguments(56)
def my_function(x,y):
    print(x+y)

my_function(5, 10)
