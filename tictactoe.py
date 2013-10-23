# Oliver's Tic Tac Toe game in Python
# For Flatiron Fellowship Application

# Contact:
# Oliver Switzer
# oliverswitzer@gmail.com
# 347-581-1089


import random
import time 

class Board:

	moves = 0   # moves counter
	board = [0, 1, 2,   #initalize board list
			 3, 4, 5,
			 6, 7, 8]

	def welcome(self):
		print
		print "Welcome! Care for a game of Tic Tac Toe?"

	def show_board(self):   #this function prints out the board
		print 
		print self.board[0],"|",self.board[1],"|",self.board[2]
		print "-" * 9
		print self.board[3],"|",self.board[4],"|",self.board[5]
		print "-" * 9
		print self.board[6],"|",self.board[7],"|",self.board[8]
		print

	def player_move(self):

		playersMove = True  #while it is human player's turn
		while playersMove:  #run this loop
			print # for extra space
			try:  # Try block used to create cases where user input should raise an error
				move_number = int(raw_input("Choose a number on the board to place your x: ")) #take user input and convert to int type
			except ValueError:  #if a valueerror is returned want to tell the user to enter an integer
				print
				print "*** Please enter a single, integer value ***" 
				continue
			if move_number < 0 or move_number > 8:  #if number is not in this range an error message is displayed. Players move is still true
				print
				print "*** Please choose a number between 0 and 8 ***"
			elif self.board[move_number] != 'x' and self.board[move_number] != 'o':   #if spot is not already taken by an x or an o
				self.board[move_number] = 'x'  #place your x on a numbered spot on the board
				playersMove = False  #human players turn is now over
			else:    #if the user chooses a spot that already has an x or an o in it
				print
				print "*** This spot is already taken! ***"

	def computer_move(self):
		random.seed()  # a random generator
		comp_move_numb = random.randint(0,8)   #selects a random number form 0-8 for computer move
		
		computersMove = True #while it is computer player's turn
		while computersMove:  #run this loop
			if self.board[comp_move_numb] != 'x' and self.board[comp_move_numb] != 'o':  #if spot is not already taken by an x or an o
				self.board[comp_move_numb] = 'o'  #place computers mark in that spot
				computersMove = False    #it is no longer the computer's turn
			else:
				computersMove = True   #it is still the computers turn
				comp_move_numb = random.randint(0,8)   # computer must choose a different place to place its mark

	def lineWin_test(self, symb, pos1, pos2, pos3):
		if self.board[pos1] == symb and self.board[pos2] == symb and self.board[pos3] == symb:  #if 'o' or 'x' (designated via symb variable) is found in these three positions
			return True    																#return true

	def checkWin(self, symb):   #this checks all possible ways to win the game. Takes symb as input either 'x' or 'o'
		if self.lineWin_test(symb, 0, 1, 2): #check horiz lines
			return True
		if self.lineWin_test(symb, 3, 4, 5):
			return True
		if self.lineWin_test(symb, 6, 7, 8):
			return True
		##
		if self.lineWin_test(symb, 0, 4, 8): #check diag lines
			return True
		if self.lineWin_test(symb, 6, 4, 2):
			return True
		##
		if self.lineWin_test(symb, 0, 3, 6):  #check vert lines
			return True
		if self.lineWin_test(symb, 1, 4, 7):
			return True
		if self.lineWin_test(symb, 2, 5, 8):
			return True
		##


		
if __name__ == "__main__":
	new_board = Board()   #instantiate new board from Board class

	new_board.welcome()   #welcome player
	new_board.show_board()   #show the board

	running = True  # set our while loop logic to true

	while running: 
		new_board.player_move()   #human player is prompted to make move
		time.sleep(1)
	 	new_board.show_board()	 #board is shown
	 	new_board.moves += 1	 #indicate 1 move has been made
	 	print "Number of moves: ", new_board.moves  #display total number of moves
	 	print

	 	if new_board.checkWin('x') == True:   #check to see if human player has won using checkWin function with 'x' as input
	 		time.sleep(0.5)
	 		print
	 		print "Player x wins :)"
			print	
	 		time.sleep(0.5)
	 		break  #stop running the while loop

	 	if new_board.moves == 9:    #if the number of moves made is 9 and no one has won, then the game is over.
	 		print
	 		print "*Yawn* nobody wins. Game Over, try again."
	 		time.sleep(0.5)
	 		break  #stop running the while loop


	 	time.sleep(1)  
	 	print "Computer's Move:"   #indicate that it is computer's move
	 	time.sleep(1)

	 	new_board.computer_move()   #computer makes move
	 	time.sleep(0.5)
	 	new_board.show_board()      #show board again
	 	new_board.moves += 1		# add 1 to moves
	 	print "Number of moves: ", new_board.moves  #display numb of moves
	 	print

	 	if new_board.checkWin('o') == True:   #check to see if computer has one. Input 'o' as symbol to check on board
	 		time.sleep(0.5)
	 		print
	 		print "Player x loses :("
	 		print
	 		time.sleep(0.5)
	 		break    #stop running the while loop

	 	if new_board.moves == 9: #if the number of moves made is 9 and no one has won, then the game is over.
	 		print
	 		print "*Yawn* nobody wins. Game Over, try again."
	 		time.sleep(0.5)
	 		break  #stop running the while loop


	




