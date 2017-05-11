'''#! :/usr/bin/python3'''
from random import * #apparently this format is bad. Whoops.
from sys import argv #necessary for writing to file
from randomizer import name_creator
from magic_system import magic_text
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

class Creature:
    '''Everything that breathes is one of these.'''

    def name(self):
        self.name = name_creator()
        return self.name

    def symmetry(self):
        num = randint(1, 100)
        if num <= 1:
            self.symmetry = "none (amorphous)"
            return self.symmetry
        elif num > 1 and num <= 20:
            self.spokes_num = randrange(1, 8, 2)
            self.symmetry = "radial"
            return self.symmetry

        elif num > 20 and num <= 100:
            self.symmetry = "bilateral"
            return self.symmetry

    def number_of_limbs(self, symmetry): #requires symmetry for Number of Limbs
        if symmetry == "bilateral":
            bnum = randint(1, 100)
            if bnum <= 5:
                self.number_of_limbs = 0
                return self.number_of_limbs
            elif bnum > 5 and bnum <= 35:
                self.number_of_limbs = 2
            elif bnum > 35 and bnum <= 70:
                self.number_of_limbs = 4
                return self.number_of_limbs
            elif bnum > 70 and bnum <= 95:
                self.number_of_limbs = 8
                return self.number_of_limbs
            else:
                self.number_of_limbs = 6
                return self.number_of_limbs
        elif symmetry == "radial":
            rnum = randint(1, 100)
            if rnum <= 90:
                self.number_of_limbs = 0
                return self.number_of_limbs
            if rnum > 90 and rnum <= 95:
                self.number_of_limbs = 1
                return self.number_of_limbs
        else:
            self.number_of_limbs = "n/a"
            return self.number_of_limbs

    def mass(self):
        self.mass = str(randrange(1, 5000)) + " kg"
        return self.mass

    def intelligence(self, symmetry):
        self.inum = randrange(1,101)
        return self.inum

    def sentience(self, intelligence):
        if intelligence < 40:
            self.sentience = "none"
            return self.sentience
        elif intelligence >= 40 and intelligence <= 90:
            self.sentience_list = ["low", "moderate", "high (human-like)"]
            self.sentience =  self.sentience_list[randint(0, 2)]
            return self.sentience
        elif intelligence > 90:
            self.sentience = "ascended superbeing"
            return self.sentience

    def temperament(self, inum):
        '''purely reactive, fearful, docile, territorial, or
        compulsively aggressive?'''

        if inum < 20:
            self.temperament = "purely reactive"
            return self.temperament
        else:
            self.tnum = randrange(1,101)
            if self.tnum < 25:
                self.temperament = "docile"
                return self.temperament
            elif self.tnum >= 25 and self.tnum < 50:
                self.temperament = "territorial"
                return self.temperament
            elif self.tnum >= 50 and self.tnum < 75:
                self.temperament = "aggressive"
                return self.temperament
            elif self.tnum >= 75:
                self.temperament = "easily frightened"
                return self.temperament

    def domesticated(self, sentience, temperament):
        if temperament == "docile" and sentience == "low":
            self.domesticated = "Can be domesticated"
            return self.domesticated
        else:
            self.domesticated = "Not possible"
            return self.domesticated

def creatures_text():
    text = r'\section*{Menagerie}' + '''

In the land of {}  contains many interesting creatures. Here are a few of
the creatures you could run into on your travels.'''.format(i.name)
    for j in range(8):

        c = Creature()
        text += ('''
Name: {0} \\\\Symmetry: {1} \\\\Number of Limbs: {2}
\\\\Intelligence: {3}/100
\\\\Sentience: {4} \\\\Mass: {5} \\\\Temperament: {6}
\\\\Domesticated: {7}
\\newline
'''

        .format(
        c.name(),                                   #0
        c.symmetry(),                               #1
        c.number_of_limbs(c.symmetry),              #2
        c.intelligence(c.symmetry),                 #3
        c.sentience(c.inum),                        #4
        c.mass(),                                   #5
        c.temperament(c.inum),                      #6
        c.domesticated(c.sentience, c.temperament)) #7
        )
    return text
i = Intro()
c = Creature()
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

            {0} \n {1} '''#\n {2}'''
            .format(

            intro_text(),
            #magic_text(),
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
