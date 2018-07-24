# Declare a variable and initialize it
f = 0
print(f)
f = "abc"
print(f)
# redeclaring the variable works.

#However, variables of different types cannot be combined
#print("This is a string" + 12) #won't work! Note it WILL work in JS.
#Python is strongly typed, JS is weakly typed

#Global vs local variables in functions

def someFunction():
    f = "def"
    print(f)

someFunction() # will print "def" - function has own local copy
print(f) # will be "abc"

def someFunction2():
    global f
    f = "def"
    print(f)

someFunction2() # "def"
print(f) # "def"


