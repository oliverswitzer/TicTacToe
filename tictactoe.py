#Oliver's Tic Tac Toe game in Python


class Board:

board = [0, 1, 2,
		 3, 4, 5,
		 6, 7, 8]

	def showBoard():
		print board[0] + "|" + board[1] + "|" + board[2]
		print "-" * 9
		print board[3] + "|" + board[4] + "|" + board[5]
		print "-" * 9
		print board[6] + "|" + board[7] + "|" + board[8]
		
