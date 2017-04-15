from random import * #apparently this format is bad. Whoops.
from sys import argv #necessary for writing to file
from randomizer import name_creator
from creatures_class import creatures_text
from magic_system import magic_text
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
    population = 10 #soon to be referring to class continent.
    for x in range(0, population): #This will change.
        x = name_creator() #sets x equal to a string of gibberish.
        name = person(x) #establishes a variable here.
        return name.person_name #prints the name.
        #print(name.number_of_legs) #prints a class-level variable for SnGs

class generators():
    '''actually writes the program.'''

    contname = continent()
    size = continent()
    human_pop = continent() #calls continent() to generate a population number

    intro_text = ("""This is the land of {0}. It is {1} square kilometers.
                  {2} people live in {0}."""
                 .format(contname.name, size.land_area,
                 human_pop.population))

    #magic_text = magic_text()

    #pop_census_text = ("{} people live in {}. Their names are:"
    #                  .format(human_pop.population, contname.name,))



    world_directory = r'{}'.format(contname.name) #sets variable

    def intro_generator(self):

        if not os.path.exists(self.world_directory):
            os.makedirs(self.world_directory)
            intro = open('{}/Introduction.tex'.format(self.world_directory), 'w+')
            intro.write(self.intro_text)


    def census_generator(self):
        '''#this feature will probably be nixed. It's not interesting.'''
        census = open('{}/Census.tex'.format(self.world_directory), 'w+')
        census.write(pop_census_text)
        for i in range(1, 10): #human_pop.population):
            census.write("\n" + "{}".format(self.name_creator()))

    def creatures_generator(self):
        '''will generate a menagerie of 6-10 (tbd) creatures and their properties.'''

        creatures = open('{}/Creatures.tex'.format(self.world_directory), 'w+')
        creatures.write('{}'.format(creatures_text()))

    def magic_generator(self):
        '''will generate a magic system for the continent.'''
        m = open('{}/Magic System.tex'.format(self.world_directory), 'w+')
        m.write('{}'.format(magic_text()))

x = generators()
x.intro_generator()
x.creatures_generator()
x.magic_generator()
#Barebones foundation for future project: Each generated name will
    #be assigned to a class as a variable and a list of attributes will
    #be randomly generated for it.
