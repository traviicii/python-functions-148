# User Defined functions!!!!!!!

# They give us repeatable power!

# print('=' * 50)

# syntax
# def function_name():
#     code block to be executed on function call

# Simple functions

def divi():
    print('=' * 50)

divi()

def greeting():
    print("Hello there traveler!")

greeting()
greeting()
greeting()

#--- Functions with parameters
# establish a required variable/value for our function

def personal_greeting(name):
    print(f"Hello {name}, welcome to functions!")

personal_greeting("Jesmarie")
personal_greeting("Travis")
personal_greeting("Cole")
personal_greeting("Kevin")

personal_greeting(54793048)

# this functions accepts no parameter, and we ask the user for input inside of the function, this will only occur when the function is called
def whats_ur_name(): 
    thing = input("what's your name traveler? ")
    print(f"Let's welcome {thing}, the mysterious adventurer!")

# whats_ur_name()

# This funct requires a parameter, instead of asking the user for that data inside of the function, we're expecting it to be given to the function
def whats_ur_name2(thing):
    print(f"Let's welcome {thing}, the mysterious adventurer!")
    
# name = input("what's your name traveler? ")
# whats_ur_name2(name)

def greet(name):
    print(f"Helo, {name}!")

greet("Alice")
greet("James")

divi()

#---- more complex example


def class_info(instructor, students):
    print(f"This class is taught by {instructor}!")
    class_size = len(students)
    print(f"It has {class_size} students")
    for student in students:
        print(student)



ins = ["Travis", "Sarah", "Dylan", "Shoha"]
students_148 = ["Jason", "Eric", "Brad", "Dare", "Christy", "James", "Cole", "Jesmarie"]

class_info(ins, ["Jason", "Eric", "Brad", "Dare", "Christy", "James", "Cole", "Jesmarie"])

divi()

class_info(students_148, ins)

