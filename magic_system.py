#magic types
from random import *
from randomizer import name_creator

class MagicSystem:

    magic_nouns = ("the elements", "their ancestors", "nature spirits")
    magic_verbs = ("summon", "draw upon the power of", "harness")




a = MagicSystem()



def magic_text():
    m = MagicSystem()
    text = ('''
In the land of {0}, magic is based on the power of {1}. A powerful practitioner
can {2} {1}
                  '''.format(
                  "PLACEHOLDER",
                  m.magic_nouns[randrange(0, len(m.magic_nouns))],
                  m.magic_verbs[randrange(0, len(m.magic_nouns))]))

    print(text) #tbd
    return text

magic_text()
'''
spitballing here: Gotta brainstorm about magic systems now.

Based on:
elements
human objects
things found in nature

Performed by (verb)ing (DO)

verbs:
control
harness
summon the power of
'''
