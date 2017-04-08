from word_blocks import blocks
"""
class gen_randomizer:
    #takes in some variables, decides what to do with them.
    def creature(self):
   """
from random import *

def name_creator(): #tests the blocks from word_blocks
    num_of_syl = randrange(2, 5)
    which_syl = blocks()
    if num_of_syl == 2:
        return "{}{}{}".format(which_syl.
                               first_syl[randrange(0, len(which_syl.
                                                          first_syl))],
                               which_syl.
                               consonant[randrange(0, len(which_syl.
                                                          consonant))],
                               which_syl.last_syl[randrange(0, len(which_syl.
                                                         last_syl))])

    elif num_of_syl == 3:
        return "{}{}{}{}".format(which_syl.
                               first_syl[randrange(0, len(which_syl.
                                                          first_syl))],
                               which_syl.
                               middle_syl[randrange(0, len(which_syl.middle_syl))],
                               which_syl.
                               consonant[randrange(0, len(which_syl.
                                                          consonant))],
                               which_syl.last_syl[randrange(0, len(which_syl.
                                                         last_syl))])
    elif num_of_syl == 4:
        return "{}{}{}{}{}".format(which_syl.
                               first_syl[randrange(0, len(which_syl.
                                                          first_syl))],
                               which_syl.
                               middle_syl[randrange(0, len(which_syl.middle_syl))],

                               which_syl.
                               middle_syl[randrange(0, len(which_syl.middle_syl))],
                               which_syl.
                               consonant[randrange(0, len(which_syl.
                                                          consonant))],
                               which_syl.last_syl[randrange(0, len(which_syl.
                                                         last_syl))])
print(name_creator())


#the purpose of this file is to see how different py files might
#work together and access each other. There will be another file
#that reads this one and calls the variables within.
