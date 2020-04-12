#!/usr/bin/env python
# Completed by :

# Alvin Poudel Sharma
# Id: 1001555230




# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    currentGame.aiPlay() # Make a move (only random is implemented)

    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, human_first):

    play = True
    ai = 0
    human = 0
    if human_first:
        human = 1
        ai =2
    else:
        human =2
        ai =1


    while(play):
        if currentGame.pieceCount == 42:  # Is the board full?
            print 'BOARD FULL\n\nGame Over!\n'
            sys.exit(0)

            # for a computer player justy calls the aiplay method
        if currentGame.currentTurn == ai:
            currentGame.aiPlay()
            print 'Game state after move:'
            currentGame.printGameBoard()
            currentGame.checkPieceCount()
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            currentGame.gameFile = open('computer.txt', 'w')
        # for a human player justy calls the humanplay method
        if currentGame.currentTurn == human:
            currentGame.humanPlay()
            print 'Game state after move:'
            currentGame.printGameBoard()
            currentGame.checkPieceCount()
            currentGame.countScore()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            currentGame.gameFile = open('human.txt', 'w')


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    depth = int(argv[4])
    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game
    currentGame.depth = depth

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        human_first = False
        turn = argv[3]
        outFile = 'blank'
        if turn == 'human-next':
            human_first = True
            outFile = 'human.txt'
        else:
            outFile = 'computer.txt'

        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        interactiveGame(currentGame, human_first) # Be sure to pass whatever else you need from the command line




    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



