#!/usr/bin/python

import os
import sys
from sys import maxsize

##==========================================================================================
## GLOBAL VARIABLES

depth = 225 #number of boxes on the table 15^15
global_table = [[-1] * 15]*15  #list to maintain the position of tha table, initialized to empty values
ascii = 65   #initialises ascii counter
groupname = "WeWillSee"
turnFile = groupname + ".go"
letters = {}   #converts letters to numbers

##==========================================================================================
##OBJECTS

class Node():
    def __init__(self, depth, player):
        self.depth = depth #depth at which the node is at in tree
        self.utility = maxsize  #initialises to zero
        self.player = player  #0 = opponent, 1 = our agent
        self.win
        self.table = [[]] #
        self.children = []	#link nodes to the nodes
        self.CreateChildren()

    def CreateChilderen(self):
        if self.depth >=0:
            for v in self.table:
                for h in self.table[v]:
                    if h.occupied == -1:
                        new = Node(self.depth -1, not self.player)
                        new.table = self.table
                        new.table[v][h].occupied = self.player
                        self.children.append(new)

    def getValue(self):
        if (self.player == 0):
            self.utility = -maxsize
        else:
            self.utility = maxsize



class TableBox:
    def __init__(self, occupied):
       # self.posX = posX
       # self.posY = posY
        self.occupied = occupied # -1 = empty, 0 = opponent, 1 = our player

#=============================================================================================
# #MINIMAX ALGORITHM
# #Position Evaualtion Function to determine if the possible position in the best one to take
def checkHorizontal(table, last_moveX, last_moveY, player):
    counter = 1
    cX = 1
    while (cX < 5 and counter <= 5):
        if last_moveX + cX < 14:
            if table[last_moveX + cX][last_moveY].occupied == player:
                counter = counter + 1

        if last_moveX - cX > 0:
            if table[last_moveX - cX][last_moveY].occupied == player:
                counter = counter + 1
        cX += 1

    return counter == 5

def checkVertical(table, last_moveX, last_moveY, player):
    counter = 1
    cY = 1
    while (cY <5 and counter <= 5):
        if last_moveX + cY < 14:
            if table[last_moveX][last_moveY + cY].occupied == player:
                counter = counter + 1

        if last_moveX - cY > 0:
            if table[last_moveX][last_moveY - cY].occupied == player:
                counter = counter + 1
        cY += 1

    return counter == 5



def checkDiagonal(table, last_moveX, last_moveY, player):
    counter = 1
    cY = 1
    cX = 1
    while (cY <5 and cX < 5 and counter <= 5):
        if last_moveX + cY < 14:
            if table[last_moveX + cX][last_moveY + cY].occupied == player:
                counter = counter + 1

        if last_moveX - cY > 0:
            if table[last_moveX - cX][last_moveY - cY].occupied == player:
                counter = counter + 1
        cY += 1
        cX += 1

    return counter == 5


# This function is the min-max algorithm
#function for minmax algorithm
# def minmax():
#     pass
#
# def max_value():
# 	if(node.depth == 0):
# 		return node.value()
# 	v = -maxsize
# 	for (node.value && node.move) in currentnode.children():
# 	    v = max(min_value(node.children.move))
# 	return v
#
# def min_value():
# 	if(node.depth == 0):
# 		return node.value()
# 	v = maxsize
# 	for (node.value && node.move) in currentnode.children():
# 	v = min(max_value(node.children.value))
# 	return v

##============================================================================================
##FUNCTIONS

#This function makes an empty board
# def init_table():
#     for v in range(15):
#         for h in range(15):
#             global_table[v][h] = TableBox(-1)



def move(x, y, player):
    global_table[x][y] = TableBox(player) #updates global table
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

    global ascii

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
            oponent_move = line.split()

        print(oponent_move)

        if not opponent_move:
            current_state = Node(depth, 1)  # root node of tree
            current_state.table = global_table
        else:
            global_table[letters[oponent_move[1]]][int(oponent_move[2])].occupied = 0;  #enemy move
            current_state = Node(depth - 1, 1)  # root node of tree
            current_state.table = global_table

        depth = depth - 1



        move(3, 3, 1)

        #minimax(current_state)

    return


if __name__ == "__main__": main()
