#!/usr/bin/python

import os
import sys
#files = os.listdir('.') #contains all the files in current directory

groupname = "WeWillSee"
turnFile = groupname + ".go"
table = [[]]  #create a table

class Current_state:
    def __init__(self, position):
        self.position = position
        self.nextMoves = []

class Position:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY


#This function check if the game ended
def check_end():
    for f in files:
         if f == "end_game":
             return True
    return False



#tells us if it's our turn
def wait_for_turn():
    for f in os.listdir('.'):
        if f == (turnFile):
            return False         #our turn
    return True                 #not our turn



def main():

    print ("Hello World")
    wordlist = file.split()
    

    print ("its our turn")


if __name__ == "__main__": main()


