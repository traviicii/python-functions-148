# Different types of parameters

# Basic parameters : assume their value from arguments passed into the defined function

def name_printer(first, middle, last):
    print(f"Hello {first} {middle} {last}.")

#--- Position Arguments : the position of the argument determines which parameter it becomes the value of in our function
name_printer("Travis", "Cline", "Peck")
name_printer("Peck", "Travis", "Cline")

#--- Keyword Arguments : We can explicitly state which parameter takes which value
name_printer(last= "Peck", first= "Travis", middle= "Cline")

#--- Default Parameters : Give a parameter a default value if none is passed into the function

def greeting(name= "World"):
    print(f"Hello, {name}!")

greeting()
greeting("Christy")

def tomb_stone(birth, death= "TBD"):
    print(f"This person live from {birth} to {death}")

tomb_stone('10-09-1991') # if we don't pass an argument here, the default is "TBD"
tomb_stone('10-09-1991', '6-04-2024')


def divi():
    print('=' * 50)

divi()

#--- *args : unknown number of arguments, brought into the function as a tuple

def vet_hands(staff, *vols):
    print(f"On staff today we have {staff[0]} and {staff[1]}!")
    if vols:
        print("They will be assisted by the following volunteers:")
        for vol in vols:
            print(vol)

vet_hands(["Dr. Adam", "Dr. Jones"], 'Dylan', "Travis", "Grace", "Josh", "Walter", "Phillip")


#--- **kwargs : unkown amount of keyword arguments, brought into the function as a Dictionary

def routine(**daily_events):
    print(daily_events)

routine(morning = "I wake up, brush my teeth, and have breakfast", mid_morning= "Walk my dog", afternoon= "Grading and prepping for class", evening= "in class", dinner_time= "Time to eat", night= "Go to sleep")