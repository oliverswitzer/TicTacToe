#Oliver's Tic Tac Toe game in Python


class Board:

	board = [0, 1, 2,
			 3, 4, 5,
			 6, 7, 8]

	def __init__(self):
		print
		print "Welcome! Care for a game of Tic Tac Toe?"
		print 
		print self.board[0],"|",self.board[1],"|",self.board[2]
		print "-" * 9
		print self.board[3],"|",self.board[4],"|",self.board[5]
		print "-" * 9
		print self.board[6],"|",self.board[7],"|",self.board[8]
		print
		
if __name__ == "__main__":
	NewBoard = Board()

	running = True
	# while running: 
	# 	inp = int(raw_input("Choose a number on the board to place your x: ")