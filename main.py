from random import * #apparently this format is bad. Whoops.
from sys import argv #necessary for writing to file
from randomizer import name_creator
from creatures_class import creatures_text
from magic_system import magic_text
from intro import intro_text, i # i is the object that belongs to class Intro
import os

def creature_pop_generator(): #may be deleted; I can't see a reason for this to exist.
    '''generates the number and
    types of creatures'''
    #for x in range(0,9): #range #of creature types
    x =  creature()
    print(x.num_of_legs())
# Problem: We are printing the pointer location.




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

            {0} \n {1} \n {2}'''
            .format(

            intro_text(),
            magic_text(),
            creatures_text())

             + r'''

            \end {document}'''

            )



x = Generators()
#x.intro_generator()
#x.creatures_generator()         #These three for testing
#x.magic_generator()
x.book_generator()

os.system('''pdflatex /home/thatguysilver/py_projects/Random_world/{0}/Book.tex'''.format(x.world_directory))
