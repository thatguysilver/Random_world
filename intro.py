'''
This will be the intro file; I'm going to begin
the long and irritating process of moving most of
the functions in main over here. Crossing my fingers
that I don't break this thing in the process.
Thank God for git.
'''
from random import *
from randomizer import name_creator

class intro():
    '''generates the intro text'''
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

def intro_text(): #creates the intro text to be written in main.py
    i = intro()
    text = (r'''
\documentclass{article}

\begin{document}''' + '''
Name = {}
Size: {} square kilometers
Population: {}  (population density = {})
'''.format(i.name,      #0
           i.land_area,
           i.population,
           i.population_density))
    return text + r'''

\end{document}'''

print(intro_text()) #for testing purposes only
