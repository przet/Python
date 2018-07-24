#define a basic function
def func1():
    print("function1")

func1()
print (func1()) # this will return both "function1" and none - none as the return value of the function is not
                # a value, so print of this void will print the string representation of that concept - "none"
print (func1)   # No parentheses on function, so we are printing the function definition itself - we get a memory
                # address, showing that a function is just an object, and hence can be passed around and used as
                # a paramater

# Function with args
def func2(arg1, arg2):
    print(arg1," ", arg2)

# Function that returns a value
def my_cube(x):
    return x*x*x

func2(10,20)
func2(10,"Hello!")
print (func2(10,20)) # remember, will be 10, <space>, 20 and none.
print(my_cube(3)) # this will NOT return 27 and 27, as one could conclude falsely by incorrectly reasoning from the
                  # above examples. my_cube(x) has no print statement, so alone, when called, noting will print out
                  # but it returns a value, which we then can (have to) print to see it on the console
