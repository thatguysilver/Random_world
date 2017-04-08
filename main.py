from random import *
from randomizer import name_creator
from person_class import *


population = 10 #randrange(100, 1000)
def pop_generator():
    for x in range(0, population):
        x = name_creator()
        name = person(x)
        print(name.person_name)
        print(name.number_of_legs)

pop_generator()
#Barebones foundation for future project: Each generated name will
    #be assigned to a class as a variable and a list of attributes will
    #be randomly generated for it.
