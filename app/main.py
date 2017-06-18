#! venv/bin/python3.6
from random import * #apparently this format is bad. Whoops.
from sys import argv #necessary for writing to file
from randomizer import name_creator
import os
from flask import render_template, Flask, send_file
from app import app

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

class MagicSystem:
    '''Randomly generates our world's magic system.'''

    def __init__(self):
        self.magic_nouns = ("the elements", "their ancestors", "nature spirits")
        self.magic_verbs = ("summon", "draw upon the power of", "harness")

        self.magic_verb = self.magic_verbs[randrange(0, len(self.magic_verbs))]
        self.magic_type = self.magic_nouns[randrange(0, len(self.magic_nouns))]

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

    def number_of_limbs(self, symmetry):
        '''Determines how many limbs our critter has.'''

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
        '''determines mass'''

        self.mass = str(randrange(1, 5000)) + " kg"
        return self.mass

    def intelligence(self, symmetry):
        '''Randomly generates intelligence'''

        self.inum = randrange(1,101)
        return self.inum

    def sentience(self, intelligence):
        '''Assumes that sentience and intelligence are weakly correllated'''

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
        '''Can it be domesticated?'''

        if temperament == "docile" and sentience == "low":
            self.domesticated = "Can be domesticated"
            return self.domesticated
        else:
            self.domesticated = "Not possible"
            return self.domesticated

i = Intro()       #
m = MagicSystem() #  
c = Creature()    #

def intro_text():
    '''Creates intro part of LaTeX document'''
    text = (r'''

\section*{Introduction}''' + '''
Name = {0}
Size: {1} square kilometers
Population: {2}  (population density = {3})

This is the land of {0}. {0} is a magical world, with powerful magical properties
based on {4}. For the
'''.format(i.name,                #0
           i.land_area,           #1
           i.population,          #2
           i.population_density,
           m.magic_type
           ))
    return text

def magic_text():

    text = (r'''
\section*{Magic}''' + '''
In the land of {0}, magic is based on the power of {1}. A powerful practitioner
can {2} {1}
    
'''.format(i.name,
           m.magic_type,
           m.magic_verb,
           m.magic_verbs[randrange(0, len(m.magic_nouns))]))

    return text

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


                       
def generate():
    path = os.path.dirname(os.path.realpath(__file__))
 


    if 'Book' in path:
        os.system('rm -r Book')
    else:
        pass
    
    if 'Book' not in path:

        os.system(f'mkdir app/Book')
        doc = open('app/Book/Book.tex', 'w+')
        doc.write(r'''
\documentclass{article}
          
\begin{document}''' + '''
               
{0} \n {1} \n {2}'''
.format(
    intro_text(),
    magic_text(),
    creatures_text()
                      
    +r'''
                    
    \end {document}'''
            
        ))
        
        
    

    else: 
        print('There\s already a book there.')


generate()
os.system(f'pdflatex -output-directory app/Book app/Book/Book.tex')

@app.route('/')
def go():
    return render_template('layout.html') 

@app.route('/download')
def download():
   

    return send_file('Book/Book.pdf',
            as_attachment = True)


