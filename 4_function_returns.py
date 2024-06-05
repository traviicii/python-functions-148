# the goal of many functions is to produce something
#-- take something in as an argument
#-- manipulate it/do something with it
#-- return the output

name = "Travis"

data = type(name) # Value is returned but not printed to the screen, so we don't get to see it
print(type(name)) # print() allows us to see/view the returned data from the function
print(data)
# simple function with return statement

def addition(a, b):
    return a + b

# def addition1(a, b): # this will do the same thing, the above is quicker to write
#     ans = a + b
#     return ans

total = addition(5,5)
print(total)

# also works
print(addition(10,10))

# answer = input("Say something :")

addition(10,20) # nothing prints to the screen because data is returned, but we haven't done anything with it
print(addition(10,20)) # here we're doing something with that data, printing it

# doubler function will take ina list of nums and double each num in the list, then return that list of doubled numbers

def doubler(nums):
    doubled_nums = []
    for num in nums:
        doubled_num = num * 2
        doubled_nums.append(doubled_num)
    
    return doubled_nums

my_nums = [1,2,3,4,5,6,7,8]
dnums = doubler(my_nums)
print(dnums)

#--- no return
def greet_card(name): # a function without a return statement by default returns a None value
    print(f"Have a nice day, {name}")

card_message = greet_card("Travis")
print(card_message) # we can see this None value here in this print statement

# user reliant function relies on a user for input