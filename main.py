from random import *
from sys import argv #necessary for writing to file
from randomizer import name_creator
from creatures_class import creature, person
import os

class continent:
    '''data structure for generated continent'''
    name = name_creator()
    land_area = str(randrange(1000, 10000000))
    population_density = randrange(10, 20000)
    population = population_density*int(land_area) #determines a realistic pop



def creature_pop_generator():
    '''generates the number and
    types of creatures'''
    #for x in range(0,9): #range #of creature types
    x =  creature()
    print(x.num_of_legs())
# Problem: We are printing the pointer location.


def pop_generator():
    '''Generates people by calling the person class'''
    population = 1 #soon to be referring to class continent.
    for x in range(0, population): #This will change.
        x = name_creator() #sets x equal to a string of gibberish.
        name = person(x) #establishes a variable here.
        print(name.person_name) #prints the name.
        print(name.number_of_legs) #prints a class-level variable for SnGs

def executor():
    '''actually writes the program. Document write abilities
    forthcoming'''
    contname = continent()
    size = continent()
    human_pop = continent()
    text = ("""This is the land of {0}. It is {1} square kilometers.
          {2} people live in {0}."""
          .format(contname.name, size.land_area,
          human_pop.population))
    '''raw output; not in final product'''
    world_directory = r'{}'.format(contname.name) #sets variable
    if not os.path.exists(world_directory): #Ensures that path doesn't exist yet
        os.makedirs(world_directory)
        testtext = open('{}/testtext'.format(world_directory), 'w+')
        #for i in range(0, 10):
            #inhabitants = name_creator()
        testtext.write(text)

executor()



#Barebones foundation for future project: Each generated name will
    #be assigned to a class as a variable and a list of attributes will
    #be randomly generated for it.
