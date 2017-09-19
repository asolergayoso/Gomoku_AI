#!/usr/bin/python

import os
import sys
from sys import maxsize

##==========================================================================================
## GLOBAL VARIABLES
groupname = "WeWillSee"
turnFile = groupname + ".go"


##==========================================================================================
##OBJECTS
class Node():
    def __init__(self, depth, player, value = 0):
        self.depth = depth
        self.value = value
        self.player = player
        self.table = []
        self.children = []

class Table:
    def __init__(self, posX, posY, occupied):
        self.posX = posX
        self.posY = posY
        self.occupied = 0 # 0 = empty, -1 = opponent, 1 = our player

##============================================================================================
#This function check if the game ended
def check_end():
    for f in os.listdir('.'):
         if f == "end_game":
             return False
    return True



#wait_for_turn() tells us if it's our turn
def wait_for_turn():
    for f in os.listdir('.'):
        if f == (turnFile):
            return False         #our turn
    return True                 #not our turn


##=============================================================================================
#MAIN FUNCTION
def main():

    # if not our turn and no end_game, then do nothing
    while wait_for_turn() and check_end():
        pass

    # returns if game ends
    if check_end() == False:
        print ("Game has ended")
        return


    #parsing the the move_file, reads the oponent's move
    file = open("move_file" ,'r')
    for line in file:
        wordlist = line.split()



    print (wordlist)



if __name__ == "__main__": main()


