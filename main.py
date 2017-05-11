'''#! :/usr/bin/python3'''
#EXPERIMENTAL CONTENT DISREGARD
from random import * #apparently this format is bad. Whoops.
from sys import argv #necessary for writing to file
from randomizer import name_creator
from creatures_class import creatures_text
from magic_system import magic_text
#from intro import intro_text #i # i is the object that belongs to class Intro
import os

def creature_pop_generator(): #may be deleted; I can't see a reason for this to exist.
    '''generates the number and
    types of creatures'''
    #for x in range(0,9): #range #of creature types
    x =  creature()
    print(x.num_of_legs())
# Problem: We are printing the pointer location.

class Intro():
    '''generates the Intro text'''
    def __init__(self):
        self.name = name_creator()
        self.land_area = str(randrange(1000, 10000000))
        self.population_density = randrange(10, 20000)
        self.population = self.population_density*int(self.land_area)
        self.num_of_governments = randrange(1, 20) #arbitrary number; requires research

    def pop_generator(self):
        '''Generates people by calling the person class'''
        self.population = 10 #soon to be referring to class continent.
        for x in range(0, self.population): #This will change.
            x = name_creator() #sets x equal to a string of gibberish.
            name = person(x) #establishes a variable here.
            return name.person_name #prints the name.
            #print(name.number_of_legs) #prints a class-level variable for SnGs


def intro_text():
    '''Creates intro part of LaTeX document'''
    text = (r'''

\section*{Introduction}''' + '''
Name = {0}
Size: {1} square kilometers
Population: {2}  (population density = {3})

This is the land of {0}. {0} is a magical world, with powerful magical properties
based on PLACEHOLDER. For the
'''.format(i.name,                #0
           i.land_area,           #1
           i.population,          #2
           i.population_density,  #3
           ))
    return text
i = Intro()

class Generators(): #Consider nixing this in favor of a function.
    '''actually writes the program.'''

    world_directory = r'{}'.format(i.name) #sets variable

    def intro_generator(self):

        if not os.path.exists(self.world_directory):
            os.makedirs("/home/thatguysilver/py_projects/Random_world/{}"
            .format(self.world_directory))
            intro = open('/home/thatguysilver/py_projects/Random_world/{}/Introduction.tex'.format(self.world_directory), 'w+')
            intro.write(intro_text())


    def census_generator(self): #SCHEDULED FOR DEMOLITION
        '''#this feature will probably be nixed. It's not interesting.'''
        census = open('{}/Census.tex'.format(self.world_directory), 'w+')
        census.write(pop_census_text)
        for i in range(1, 10): #human_pop.population):
            census.write("\n" + "{}".format(self.name_creator()))

    def book_generator(self): #TO REPLACE ALL OTHER GENERATORS
        '''Replaces the above generators, making one function generate an entire book.'''

        if not os.path.exists(self.world_directory):
            os.makedirs("/home/thatguysilver/py_projects/Random_world/{}"
            .format(self.world_directory))

            doc = open('/home/thatguysilver/py_projects/Random_world/{}/Book.tex'
            .format(self.world_directory), 'w+')

            doc.write(r'''
            \documentclass{article}

            \begin{document}''' + '''

            {0} '''#\n {1} \n {2}'''
            .format(

            intro_text()
            #magic_text(),
            #creatures_text())

             + r'''

            \end {document}'''

            ))



x = Generators()
#x.intro_generator()
#x.creatures_generator()         #These three for testing
#x.magic_generator()
x.book_generator()

os.system('''pdflatex /home/thatguysilver/py_projects/Random_world/{0}/Book.tex'''.format(x.world_directory))
