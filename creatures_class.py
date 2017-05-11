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

class person(Creature): #considering removing this.
    #default person class; to be a subclass of creature
    #def __init__(self):
    person_name = name_creator()
    number_of_limbs = 2 #class-level attribute


def creatures_text():
    text = r'\section*{Menagerie}'
    for i in range(8):

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
    c = ''       #Necessary so we can reinstantiate a new critter each time


print(creatures_text()) #for testing the text
