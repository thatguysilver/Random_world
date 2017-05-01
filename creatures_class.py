from random import *
from randomizer import name_creator

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
            if bnum <=5:
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
            return self.sentience_list[randint(0, 2)]
        elif intelligence > 90:
            self.sentience = "ascended superbeing"
            return self.sentience

class person(Creature): #considering removing this.
    #default person class; to be a subclass of creature
    #def __init__(self):
    person_name = name_creator()
    number_of_limbs = 2 #class-level attribute


def creatures_text():
    c = Creature()
    creatures_text = ('''

Name: {} \\\\Symmetry: {} \\\\Number of Limbs: {}
\\\\Intelligence: {}/100
Sentience: {} \\\\Mass: {}'''
        .format(c.name(),
        c.symmetry(), #0
        c.number_of_limbs(c.symmetry),
        c.intelligence(c.symmetry),
        c.sentience(c.inum),
        c.mass()))+ r'''

\end {document}'''


    return creatures_text


print(creatures_text()) #for testing the text
"""
Figured it out on my break here at Lowe's.
It would seem that in this case, the
person_name var takes in the x var from
main.py. I still have a lot to learn, but
I'm making a little progress.
"""
