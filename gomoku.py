#!/usr/bin/python

import os
import sys
from sys import maxsize

##==========================================================================================
## GLOBAL VARIABLES

depth = 225  # number of boxes on the table 15^15
global_table = [[-1] * 15 for _ in range(15)]  # list to maintain the position of tha table, initialized to empty values
ascii = 65  # initialises ascii counter
groupname = "WeWillSee"
turnFile = groupname + ".go"
letters = {}  # converts letters to numbers


##==========================================================================================
##OBJECTS

class Node():
    def __init__(self, depth, player):
        self.depth = depth  # depth at which the node is at in tree
        self.player = player  # 0 = opponent, 1 = our agent
        self.lastX = 0
        self.lastY = 0
        self.table = [[-1] * 15 for _ in range(15)]  # to keep track of all the possible moves
        self.children = []  # link nodes to the nodes
        self.utility = self.getValue()  # initialises to zero
        # self.CreateChildren()

    def CreateChildren(self):
        if self.depth > 0:
            for v in range(len(self.table)):
                for h in range(len(self.table)):
                    if self.table[v][h] == -1:
                        new = Node(self.depth - 1, not self.player)
                        new.table = self.table
                        new.table[v][h] = self.player
                        new.lastX = h
                        new.lastY = v
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
        self.occupied = occupied  # -1 = empty, 0 = opponent, 1 = our player


# =============================================================================================
#
## THE FOLLOWING FUNCTIONS WILL DETERMINE IF THERE ARE 5 ADJACENT PIECES, EITHER DIAGONALLY VERTICALLY OR HORIZONTALLY
def checkHorizontal(table, last_moveX, last_moveY, player):
    counter = 1
    cX = 1
    while (cX < 5 and counter <= 5):
        if last_moveX + cX < 14:
            if table[last_moveX + cX][last_moveY] == player:
                counter = counter + 1

        if last_moveX - cX > 0:
            if table[last_moveX - cX][last_moveY] == player:
                counter = counter + 1
        cX += 1

    return counter == 5


def checkVertical(table, last_moveX, last_moveY, player):
    counter = 1
    cY = 1
    while cY < 5 and counter <= 5:
        if last_moveY + cY < 15:
            if table[last_moveX][last_moveY + cY] == player:
                counter = counter + 1

        if last_moveY - cY > 0:
            if table[last_moveX][last_moveY - cY] == player:
                counter = counter + 1
        cY += 1

    return counter == 5


def checkDiagonal(table, last_moveX, last_moveY, player):
    counter = 1
    cY = 1
    cX = 1
    while cY < 5 and cX < 5 and counter <= 5:
        # diagonal up right
        if last_moveX + cX < 15 and last_moveY - cY >= 0:
            if table[last_moveX + cX][last_moveY - cY] == player:
                counter = counter + 1
        # diagonal down left
        elif last_moveX - cX >= 0 and last_moveY + cY < 15:
            if table[last_moveX - cX][last_moveY + cY] == player:
                counter = counter + 1
        # diagonal down right
        elif last_moveX + cX < 15 and last_moveY + cY < 15:
            if table[last_moveX + cX][last_moveY + cY] == player:
                counter = counter + 1
        # diagonal down left
        elif last_moveX - cX >= 0 and last_moveY - cY >= 0:
            if table[last_moveX - cX][last_moveY - cY] == player:
                counter = counter + 1

        cY += 1
        cX += 1

    return counter == 5


## This function is supposed to find if the state is a win a loose or a draw
def TerminalTest(n):
    # check if max wins
    if (checkDiagonal(n.table, n.lastX, n.lastY, 1) or checkHorizontal(n.table, n.lastX, n.lastY, 1) or checkVertical(
            n.table, n.lastX, n.lastY, 1)):
        n.utility = 1
        return True
    # check if min wins
    # elif(checkDiagonal(n.table,n.lastX,n.lastY,0) or checkHorizontal(n.table,n.lastX,n.lastY,0) or checkVertical(n.table,n.lastX,n.lastY,0)):
    elif checkHorizontal(n.table, n.lastX, n.lastY, 0) or checkVertical(n.table, n.lastX, n.lastY, 0):
        n.utility = -1
        return True
    # no winner or game is over
    elif (n.depth == 0):
        n.utility = 0
        return True
    else:
        return False


# ===========================================================================================
# MINIMAX ALGORITHM
# This function is the min-max algorithm

# returns a minimax value 0 for no utility, 1 for max utility, -1 for min ustility

def minimax(state):
    optimal = min_value(state)
    for child in state.children:
        if child.utility == optimal:
            print (child.lastX)
            result = [child.lastX, child.lastY]
            # result[0] = child.lastX
            # result[1] = Child.lastY
            return result


def max_value(state):
    # state.CreateChildren()
    if (TerminalTest(state)):
        return state.utility
    state.utility = -maxsize
    state.CreateChildren()
    for child in state.children:
        optimal = min_value(child)
        if (optimal >= state.utility):
            state.utility = optimal
    # utility = max(min_value(child))
    return state.utility


def min_value(state):
    # state.CreateChildren()
    if (TerminalTest(state)):
        return state.utility
    state.utility = maxsize
    state.CreateChildren()
    for child in state.children:
        optimal = max_value(child)
        if optimal <= state.utility:
            state.utility = optimal
    # utility = min(max_value(node.children.value))
    return state.utility


# ##################################################################
# #FUNCTIONS

def write_move(x, y):
    global_table[x][y] = 1  # updates global table
    file = open("move_file", 'w')
    for n in letters:
        if letters[n] == y:
            file.writelines([groupname, ' ', n, ' ', str(x)])
            file.close()


# This function check if the game ended
def check_end():
    for f in os.listdir('.'):
        if f == "end_game":
            return False
    return True


# wait_for_turn() tells us if it's our turn
def wait_for_turn():
    for f in os.listdir('.'):
        if f == (turnFile):
            return False  # our turn
    return True  # not our turn


# Evaluation function
# takes in a node and a considered spot
# returns a heuristic value for given node
# if chain of three in a row found, block, otherwise, attack
# if agent is player two and it is the agents first turn, always play on top of opponents move
# don't consider squares more than 2 units away from the closest piece
def eval_func(n, x, y):
    pass


##=============================================================================================
# MAIN FUNCTION
def main():
    global ascii
    global depth

    for i in range(15):
        letters[chr(ascii)] = i  # assigns value to dictionary
        ascii = ascii + 1  # incrememts the ascii counter

    while (True):
        # if not our turn and no end_game, then do nothing
        while wait_for_turn() and check_end():
            pass

        # breaks the while loop if game ends
        if check_end() == False:
            print ("Game has ended")
            break

        # parsing the the move_file, reads the opponent's move
        file = open("move_file", 'r')
        for line in file:
            opponent_move = line.split()

        print(opponent_move)

        if not opponent_move:
            current_state = Node(depth, 1)  # root node of tree
            current_state.table = global_table
        else:
            depth = depth - 1
            global_table[letters[opponent_move[1]]][
                int(opponent_move[2]) - 1] = 0;  # enemy move ###############.occupied
            current_state = Node(depth, 1)  # root node of tree
            current_state.table = global_table

        for v in range(len(global_table)):
            for h in range(len(global_table)):

                print ((current_state.table[v][h]), end=" ")

                print (current_state.table[v][h]),  # end=" "

            print ("")

            # current_state.CreateChildren()
            # print ("child.lastX = " + str(current_state.children[1].lastX))

        best_move = []
        best_move = minimax(current_state)
        print (best_move)
        write_move(best_move[0], best_move[1])

        depth = depth - 1

        print ("finished moving")

    return


if __name__ == "__main__": main()
