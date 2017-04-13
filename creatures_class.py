from random import *
from randomizer import name_creator

class creature:
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

    def num_of_legs(self, symmetry): #requires symmetry for number of legs
        if symmetry == "bilateral":
            bnum = randint(1, 100)
            if bnum <=35:
                self.num_of_legs = 2
                return self.num_of_legs
            elif bnum > 35 and bnum <= 70:
                self.num_of_legs = 4
                return self.num_of_legs
            elif bnum > 70 and bnum <= 95:
                self.num_of_legs = 8
                return self.num_of_legs
            else:
                self.num_of_legs = 6
                return self.num_of_legs
        elif symmetry == "radial":
            rnum = randint(1, 100)
            if rnum <= 90:
                self.num_of_legs = 0
                return self.num_of_legs
            if rnum > 90 and rnum <= 95:
                self.num_of_legs = 1
                return self.num_of_legs
        else:
            self.num_of_legs = "n/a"
            return self.num_of_legs

    def intelligence(self, symmetry):
        self.inum = randrange(1,101)
        return self.inum

    def sentience(self, intelligence):
        if intelligence < 40:
            self.sentience = "none"
            return self.sentience
        elif intelligence >= 40 and intelligence < 60:
            self.sentience = "low"
            return self.sentience
        elif intelligence >= 60 and intelligence < 70:
            self.sentience = "medium"
            return self.sentience
        elif intelligence >= 70 and intelligence < 90:
            self.sentience = "high"
            return self.sentience
        else:
            self.sentience = "ascended superbeing"
            return self.sentience

class person(creature): #considering removing this.
    #default person class; to be a subclass of creature
    #def __init__(self):
    person_name = name_creator()
    number_of_legs = 2 #class-level attribute


def creatures_text():
    c = creature()
    creatures_text = (
    '''Name: {} \nSymmetry: {} \nNumber of Legs: {} \nIntelligence: {}/100
    Sentience: {}'''
    .format(c.name(),
            c.symmetry(), #0
            c.num_of_legs(c.symmetry),
            c.intelligence(c.symmetry),
            c.sentience(c.inum)))

    print(creatures_text)


creatures_text() #for testing the text
"""
Figured it out on my break here at Lowe's.
It would seem that in this case, the
person_name var takes in the x var from
main.py. I still have a lot to learn, but
I'm making a little progress.
"""
