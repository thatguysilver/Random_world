from random import *
from randomizer import name_creator
from person_class import creature, person


population = 10 #randrange(100, 1000)
def creature_pop_generator():
    '''generates the number and
    types of creatures'''
    for x in range(0,9): #range #of creature types
        x = creature()
        print(x.num_of_legs)



def pop_generator(): #Generates people by calling the person_class
    for x in range(0, population):
        x = name_creator() #sets x equal to a string of gibberish.
        name = person(x) #establishes a variable here.
        print(name.person_name) #prints the name.
        print(name.number_of_legs) #prints a class-level variable for SnGs

pop_generator()
creature_pop_generator()
#Barebones foundation for future project: Each generated name will
    #be assigned to a class as a variable and a list of attributes will
    #be randomly generated for it.
