from randomizer import *

class creature:
    '''Everything that breathes is one of these.'''

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

    def num_of_legs(self, symmetry):
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



class person(creature):
    #default person class; to be a subclass of creature
    #def __init__(self):
    person_name = name_creator()
    number_of_legs = 2 #class-level attribute


def creatures_text():
    c = creature()
    creatures_text = ('''Symmetry: {} \nNumber of Legs: {}'''
                         .format(c.symmetry(), #0
                         c.num_of_legs(c.symmetry)))
    print(creatures_text)


creatures_text() #for testing the text
"""
Figured it out on my break here at Lowe's.
It would seem that in this case, the
person_name var takes in the x var from
main.py. I still have a lot to learn, but
I'm making a little progress.
"""
