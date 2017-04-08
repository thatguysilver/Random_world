from random import *
from randomizer import name_creator


population = 10 #randrange(100, 1000)

for x in range(0, population):
    x = name_creator()
    print(x)

#Barebones foundation for future project: Each generated name will
    #be assigned to a class as a variable and a list of attributes will
    #be randomly generated for it.
