#!/usr/bin/python

import os
import sys

groupname = "WeWillSee"
turnFile = groupname + ".go"
table = [[]]  #create a table

class Current_state:
    def __init__(self, position):
        self.position = position
        self.nextMoves = []

class Location:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY


#This function check if the game ended
def check_end():
    for f in os.listdir('.'):
         if f == "end_game":
             return False
    return True



#tells us if it's our turn
def wait_for_turn():
    for f in os.listdir('.'):
        if f == (turnFile):
            return False         #our turn
    return True                 #not our turn



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


