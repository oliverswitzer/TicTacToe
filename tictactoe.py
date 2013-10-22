#Oliver's Tic Tac Toe game in Python


class Board:

	board = [0, 1, 2,
			 3, 4, 5,
			 6, 7, 8]

	def showBoard(self):
		print self.board[0],"|",self.board[1],"|",self.board[2]
		print "-" * 9
		print self.board[3],"|",self.board[4],"|",self.board[5]
		print "-" * 9
		print self.board[6],"|",self.board[7],"|",self.board[8]
		
if __name__ == "__main__":
	NewBoard = Board()

	NewBoard.showBoard()