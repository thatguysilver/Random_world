from randomizer import *

class creature:
    '''Everything that breathes is one of these.'''
    def num_of_legs(self, num_of_legs = ):
        self.num_of_legs = num_of_legs
        num_of_legs = random.randint(1, 100)
        if num_of_legs <=35:
            return 2
        if num_of_legs <=70 and > 35:
            return 4
        if num_of_legs <=95 and > 70:
            return 8
        if num_of_legs <=100 and > 95:
            return 6


class person(creature):
    '''default person class; to be a subclass of creature
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
