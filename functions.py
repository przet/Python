#define a basic function
def func1():
    print("function1")

func1()
print (func1()) # this will return both "function1" and none - none as the return value of the function is not
                # a value, so print of this void will print the string representation of that concept - "none"
print (func1)   # No parentheses on function, so we are printing the function definition itself - we get a memory
                # address, showing that a function is just an object, and hence can be passed around and used as
                # a paramater
