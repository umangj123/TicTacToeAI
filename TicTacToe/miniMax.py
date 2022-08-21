from collections import deque
import time
import sys
from heapq import heappop, heappush
import random
minValue = -100
maxValue = 1000

def swap(state, pos1,letter):
    return state[:pos1] + letter[0] + state[pos1 + 1:]


def play(board):
    computer = True
    empty = True
    print("Current Board:")
    print_puzzle(3, board)
    for i in board:
        if i != ".":
            empty = False
    if empty:
        order = input("Who will play first? (Player or AI)")
        if order == "Player":
            computer = False
            computer_letter = "O"
            player_letter = "X"
        else:
            computer_letter = "X"
            player_letter = "O"
    else:
        x = 0
        o = 0
        for i in board:
            if i == "X":
                x += 1
            elif i == "O":
                o += 1
        if x > o:
            computer_letter = "O"
            player_letter = "X"
        else:
            computer_letter = "X"
            player_letter = "O"
    while goal_test(board) == 2:
        if computer:
            boards, indexes = get_possible_moves(board,computer_letter)
            count = 0
            my_choice_result = -10 if computer_letter == "X" else 10
            score = 99999
            index = 0
            for i in boards:
                if computer_letter == "X":
                    score = mini(i)
                else:
                    score = maxx(i)
                if (score == -1 and computer_letter == "X") or (score == 1 and computer_letter == "O"):
                    print("Moving at", indexes[count], "results in a loss")
                elif score == 0:
                    print("Moving at", indexes[count], "results in a tie")
                elif (score == 1 and computer_letter == "X") or (score == -1 and computer_letter == "O"):
                    print("Moving at", indexes[count], "results in a win")
                if (computer_letter == "X" and score > my_choice_result) or (
                        computer_letter == "O" and score < my_choice_result):
                    my_choice_result = score
                    index = indexes[count]
                count += 1
            print()
            print("I choose space", index)
            board = swap(board, index, computer_letter)
            print()
            print("Current Board:")
            print_puzzle(3,board)
            print()
            computer = False

        else:
            boards2, indexes2 = get_possible_moves(board, player_letter)
            print("You can move to any of these spaces", indexes2)
            val = input("Where would you like to go")
            board = swap(board, int(val), player_letter)
            print()
            print("Current Board:")
            print_puzzle(3,board)
            print()
            computer = True
    if(goal_test(board)==1 and computer_letter =="X") or (goal_test(board) == -1 and computer_letter =="O"):
        print("I win!")
    elif(goal_test(board)== -1 and player_letter=="O") or (goal_test(board) == 1 and player_letter == "X"):
        print("You Win!")
    else:
        print("Tie Game")


def goal_test(board): #1 means x won -1 means y won and 0 means tie
    if (board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[0] == "O" and board[1] == "O" and board[2] == "O"):
        if board[0]=="X":
            return 1
        else:
            return -1

    elif (board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[0] == "O" and board[3] == "O" and board[6] == "O"):
        if board[0]=="X":
            return 1
        else:
            return -1

    elif (board[3] == "X" and board[4] == "X" and board[5] == "X") or (board[3] == "O" and board[4] == "O" and board[5] == "O"):
        if board[3]=="X":
            return 1
        else:
            return -1
    elif (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[1] == "O" and board[4] == "O" and board[7] == "O"):
        if board[1]=="X":
            return 1
        else:
            return -1
    elif (board[6] == "X" and board[7] == "X" and board[8] == "X") or (board[6] == "O" and board[7] == "O" and board[8] == "O"):
        if board[6] == "X":
            return 1
        else:
            return -1
    elif (board[2] == "X" and board[5] == "X" and board[8] == "X") or (board[2] == "O" and board[5] == "O" and board[8] == "O"):
        if board[2]=="X":
            return 1
        else:
            return -1

    elif (board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[0] == "O" and board[4] == "O" and board[8] == "O"):
        if board[0]=="X":
            return 1
        else:
            return -1
    elif (board[2] == "X" and board[4] == "X" and board[6] == "X") or (board[2] == "O" and board[4] == "O" and board[6] == "O"):
        if board[2]=="X":
            return 1
        else:
            return -1
    elif "." not in board:
        return 0
    return 2


def print_puzzle(board_size, order):
    count = 0
    for i in range(board_size):
        for j in range(board_size):
            print(order[count], end=" ")
            count += 1
        print()
    print()


def get_possible_moves(board,letter):
    storage = []
    new_boards = []
    for i in range(9):
        if board[i] == ".":
            storage.append(i)
    #print(storage)
    for i in storage:
        y = board[:int(i)] + letter[0] + board[int(i+1):]
        #print(y)
        new_boards.append(y)
    return new_boards, storage


def maxx(board):
    y = goal_test(board)
    if y!=2:
        return y
    possible, not_needed = get_possible_moves(board, "X")
    maxValue = -10
    for i in possible:
        z = mini(i)
        if maxValue < z:
            maxValue = z
    return maxValue


def mini(board):
    y = goal_test(board)
    if y!=2:
        return y
    possible, not_needed = get_possible_moves(board, "O")
    minValue = 10
    for i in possible:
        z = maxx(i)
        if z < minValue:
            minValue = z
    return minValue

# min(list_of_maxes)
# max(list_of_mins)
#
# funcs = [min, max]
# funcs[board.count('.') % 2](list_of_vals)


def negamax2(board):
    y = goal_test(board)
    if y!=2:
        return y
    count = 0
    for i in board:
        if i == '.':
            count +=1
    token = " "
    if (count % 2) == 0:
        token = "O"
    else:
        token = "X"
    possible, not_needed = get_possible_moves(board,token)
    for i in possible:
        z = negamax2(i)
        if token == "X":
            if z > maxValue:
                maxValue = z;
        else:
            if z < minValue:
                minValue = z


def negamax(board,player):
    state = goal_test2(board,player)
    if state != 2: #game is over if not = 2
        return state
    possible_moves, unused = get_possible_moves(board, player)
    if(player=="X"):
        player2 = "O"
    else:
        player2 = "X"
    moveValues = []
    for i in possible_moves:
        val = -negamax(i, player2) #changing perspective
        moveValues.append(val)
    #print(moveValues)
    y = max(moveValues) #negamax is maximizing and accounting for change
    return y


def goal_test2(board,player): #1 means x won -1 means y won and 0 means tie
    if board[0] == board[1] == board[2] != '.':
        if board[0] == player:
            return 1
        else:
            return -1

    elif board[0] == board[3] == board[6] != ".":
        if board[0] == player:
            return 1
        else:
            return -1

    elif board[3] == board[4] == board[5] != ".":
        if board[3] == player:
            return 1
        else:
            return -1
    elif board[1] == board[4] == board[7] != ".":
        if board[1] == player:
            return 1
        else:
            return -1
    elif board[6] == board[7] == board[8] != ".":
        if board[6] == player:
            return 1
        else:
            return -1
    elif board[2] == board[5] == board[8] != ".":
        if board[2]== player:
            return 1
        else:
            return -1

    elif board[0] == board[4] == board[8] != ".":
        if board[0] == player:
            return 1
        else:
            return -1
    elif board[2] == board[4] == board[6] != ".":
        if board[2] == player:
            return 1
        else:
            return -1
    elif "." not in board:
        return 0
    return 2


def playnega(board):
    computer = True
    empty = True
    print("Current Board:")
    print_puzzle(3, board)
    for i in board:
        if i != ".":
            empty = False
    if empty:
        order = input("Who will play first? (Player or AI)")
        if order == "Player":
            computer = False
            computer_letter = "O"
            player_letter = "X"
        else:
            computer_letter = "X"
            player_letter = "O"
    else:
        x = 0
        o = 0
        for i in board:
            if i == "X":
                x += 1
            elif i == "O":
                o += 1
        if x > o:
            computer_letter = "O"
            player_letter = "X"
        else:
            computer_letter = "X"
            player_letter = "O"
    while goal_test2(board, 'X') == 2: #game not over
        if computer:
            boards, indexes = get_possible_moves(board,computer_letter)
            count = 0
            my_choice_result = -10 #if computer_letter == "X" else 10
            score = 99999
            index = 0
            for i in boards:
                if computer_letter == "X":
                    score = -negamax(i,"O") # don't forget to negate this too
                else:
                    score = -negamax(i,"X")
                if score == -1:
                    print("Moving at", indexes[count], "results in a loss")
                elif score == 0:
                    print("Moving at", indexes[count], "results in a tie")
                elif score == 1:
                    print("Moving at", indexes[count], "results in a win")
                # always maximize score
                if score > my_choice_result:
                    my_choice_result = score
                    index = indexes[count]
                count += 1
            print()
            print("I choose space", index)
            board = swap(board, index, computer_letter)
            print()
            print("Current Board:")
            print_puzzle(3,board)
            print()
            computer = False

        else:
            boards2, indexes2 = get_possible_moves(board, player_letter)
            print("You can move to any of these spaces", indexes2)
            val = input("Where would you like to go")
            board = swap(board, int(val), player_letter)
            print()
            print("Current Board:")
            print_puzzle(3,board)
            print()
            computer = True
    if(goal_test(board)==1 and computer_letter =="X") or (goal_test(board) == -1 and computer_letter =="O"):
        print("I win!")
    elif(goal_test(board)== -1 and player_letter=="O") or (goal_test(board) == 1 and player_letter == "X"):
        print("You Win!")
    else:
        print("Tie Game")


w = sys.argv[1]
playnega(w)
