from randomizer import *

class creature:
    '''Everything that breathes is one of these.'''
    def num_of_legs(self):
        num = randint(1, 100)
        if num <=35:
            num = 2
            return num
        elif num > 35 and num <= 70:
            num = 4
            return num
        elif num > 70 and num <= 95:
            num = 8
            return num
        else:
            num = 6
            return num


class person(creature):
    #default person class; to be a subclass of creature
    def __init__(self, person_name):
        self.person_name = person_name
    number_of_legs = 2 #class-level attribute
"""
Figured it out on my break here at Lowe's.
It would seem that in this case, the
person_name var takes in the x var from
main.py. I still have a lot to learn, but
I'm making a little progress.
"""
