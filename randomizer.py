from word_blocks import Blocks
from random import *

def name_creator(): #Generic; will be altered and cloned and altered later.
    '''all names must include a bottom and top range for number of blocks.'''

    num_of_syl = randrange(2, 5)
    which_syl = Blocks()
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





#the purpose of this file is to see how different py files might
#work together and access each other. There will be another file
#that reads this one and calls the variables within.
