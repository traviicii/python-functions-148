# Built in functions

# print() : prints data to the screen so it is visible to the user

print("string1", 'string2', sep='============')

# \n : new line character

print('string1\n\n\n')
print("We're here now")

print('string1', end=' ')
print("We're here now")


# \t : tab special character

print("this is\t\t", 'separated')

# \\ : backslash character adds a backslash

print('this string should now have a backslash\\')

# String concatenation
words = " add"
print("We can" + words + " strings together")

# Formatted strings

name = 'Alice'
age = 30

# using .format()
print("Name: {}, Age: {}".format(name, age))

# Modern formatted string
print(f"Name: {name}, Age: {age}")


# input() : used to take user input 

# name = input("what is your name? ")
# print(f"Hello, {name}")

# type() : can be used to return the data type of data stored in a variable
num = 10
print(type(num))

# len() : Returns the length of an iterable object
message = 'Hello'
print(len(message))

# isinstance(var, type) : check if a variable holds a specific data type, always returns a boolean value

num = 10
print(isinstance(num, int))

# abs() : returns absolute value
number = -5
print(abs(number))

# round() : rounds a number to the nearest integer or specified number of decimal places
# must be a decimal above .5, for ex 4.51, in order to round up

number = 4.567
print(round(number)) # output: 5
print(round(number, 2)) # output: 4.57

num2 = 4.5
print(round(num2)) # output: 4

num3 = 4.51 # output: 5
print(round(num3))

print(round(4.4)) # output: 4

# sum() : returns the sum of all items in a iterable

numbers = [1, 2, 3, 4]
print(sum(numbers)) # output: 10

# min() : returns the smallest value in an iterable
print(min(numbers)) # output: 1

# max() : returns the largest value in an iterable

print(max(numbers)) # output: 4

# pow(<num>, <to power of>) : returns the power of a number

print(pow(2, 3)) # output: 8

# divmod() : return a tuple containing the quotient and remainder

print(divmod(10, 3)) # output: (3,1)

#------------------

# int() : converts a value to an integer
print(int("10"))
# print(int("ten")) this would not work

# str() : converts a value to a string
print(str(10), type(str(10)))

# float() : converts a value toa float
print(float("10.5"))

# bool() : converts a value to a boolean
print(bool(0)) # output: False
print(bool(1)) # output: True
print(bool('')) # output: False
print(bool([])) # output: False

names = []
print(bool(names))

if names:
    print("Hey there are names in here")
else:
    print("Uh oh, no names in here yet")