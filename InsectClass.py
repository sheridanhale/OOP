import random

    #create a class for an insect object with 2 attributes and one method
    # , determine length of flight. Length flight should be a method that randomly assigns a number between 1 and 10miles,
    #Create a python program that will create an instance of the insect class
    #print out how many miles the insect can fly
class Insect:
    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.flight = 0

    def calc_flight(self):
         self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight