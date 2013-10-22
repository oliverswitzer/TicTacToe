#Oliver's Tic Tac Toe game in Python

import random
import time 

class Board:

	board = [0, 1, 2,
			 3, 4, 5,
			 6, 7, 8]

	def welcome(self):
		print
		print "Welcome! Care for a game of Tic Tac Toe?"

	def show_board(self):
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
			print 			# for extra space
			move_number = int(raw_input("Choose a number on the board to place your x: "))  #take user input and convert to int type
			if self.board[move_number] != 'x' and self.board[move_number] != 'o':   #if spot is not already taken by an x or an o
				self.board[move_number] = 'x'  #place your x on a numbered spot on the board
				playersMove = False
			else: 
				print "This spot is already taken!"

	def computer_move(self):
		random.seed()  # a random generator
		comp_move_numb = random.randint(0,8)
		
		computersMove = True #while it is computer player's turn
		while computersMove:  #run this loop
			if self.board[comp_move_numb] != 'x' and self.board[comp_move_numb] != 'o':  #if spot is not already taken by an x or an o
				self.board[comp_move_numb] = 'o'  #place computers mark in that spot
				computersMove = False    #it is no longer the computer's turn
			else:
				computersMove = True   #it is still the computers turn
				comp_move_numb = random.randint(0,8)   # computer must choose a different place to place its mark

		
if __name__ == "__main__":
	new_board = Board()

	new_board.welcome()
	new_board.show_board()

	running = True

	while running: 
		new_board.player_move()
	 	new_board.show_board()
	 	time.sleep(1)
	 	print "Computer's Move:"
	 	# time.sleep(1)
	 	new_board.computer_move()
	 	new_board.show_board()


	




