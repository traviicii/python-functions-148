# in python we have two kinds of scope. Global Scope, and Local Scope

# The scope determines what variables are accessible

# Global Scope is anywhere outside of your functions

# Global Variable
x = 7 # Variables defined in global scope can be accessed anywhere in your code
a = "Words"
alist = ["item1", 'itme2', 'item3']

if x:
    print(x)

# Local Scope is created inside of function

def local_func():
    y = 7 # Local variable, only accessible inside of this function

    print(x)

local_func()
print(y)