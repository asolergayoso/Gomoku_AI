#!/usr/bin/python

import os
import sys
from sys import maxsize

##==========================================================================================
## GLOBAL VARIABLES

depth = 225 #number of boxes on the table 15^15
global_table = []  #list to maintain the position of tha table
groupname = "WeWillSee"
turnFile = groupname + ".go"
letters = {}   #converts letters to numbers

##==========================================================================================
##OBJECTS

class Node():
    def __init__(self, depth, player):
        self.depth = depth #depth at which the node is at in tree
        self.value = 0  #initialises to zero 
        self.player = player  #0 = opponent, 1 = our agent
        self.table = [] #
        self.children = []	#link nodes to the nodes

#Rushdi likes big dicks
class TableBox:
    def __init__(self, posX, posY, occupied):
        self.posX = posX
        self.posY = posY
        self.occupied = 0 # 0 = empty, -1 = opponent, 1 = our player

#=============================================================================================
# #MINIMAX ALGORITHM
# #Position Evaualtion Function to determine if the possible position in the best one to take
def pos_eval():
    pass

# This function is the min-max algorithm
#function for minmax algorithm
def minmax():
    pass

def max_value():
	if(node.depth == 0):
		return node.value()
	v = -maxsize
	for (node.value && node.move) in currentnode.children():
	    v = max(min_value(node.children.move))
	return v

def min_value():
	if(node.depth == 0):
		return node.value()
	v = maxsize
	for (node.value && node.move) in currentnode.children():
	v = min(max_value(node.children.value))
	return v

##============================================================================================
##FUNCTIONS

#This function makes an empty board
def init_table():
    for v in range(1, 15):
        for h in range(1, 15):
            global_table.append(TableBox(h, v, 0))

def move(x, y, player):
    global_table.append(TableBox(x, y, player))   #updates global table
    if player:
        file = open("move_file", 'w')
        for n in letters:
            if letters[n] == y:
             file.writelines([groupname, ' ', n, ' ', str(x)])
             file.close()

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

    init_table()  ##creates an empty table
    ascii = 65   #initialises ascii counter
    for i in range(1,15):
        letters[chr(ascii)] = i     #assigns value to dictionary
        ascii = ascii + 1      # incrememts the ascii counter

    while(True):
        # if not our turn and no end_game, then do nothing
        while wait_for_turn() and check_end():
            pass

        # breaks the while loop if game ends
        if check_end() == False:
            print ("Game has ended")
            break


        #parsing the the move_file, reads the opponent's move
        file = open("move_file",'r')

        for line in file:
            wordlist = line.split()

        print(wordlist)

        current_state = Node(depth, 0)   #root node of tree
        current_state.table = global_table



        move(3, 3, 1)

        #minimax(current_state)

    return


if __name__ == "__main__": main()
