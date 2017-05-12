
from random import *
from randomizer import name_creator

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

i = Intro()
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



print(intro_text()) #for testing purposes only
