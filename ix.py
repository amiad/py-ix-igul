#!/usr/bin/env python
import re
class Board:
	__empty=9
	def __init__(self):
		self.board=[]
		for i in range(3):
			self.board.append([])
			for j in range(3):
				self.board[i].append('')

	def set_cell(self,sign,x,y):
		if not self.get_cell(x,y):
			self.board[x][y]=sign
			self.__empty-=1
			return True;
		else:
			return False

	def get_cell(self,x,y):
		return self.board[x][y] if self.board[x][y] else False

	def print(self):
		for x in range(3):
			line=""
			for j in range(3):
				cell=self.get_cell(x,j)
				cell=str(cell if cell else ' ')
				det='|' if j<2 else ''
				line+=cell+det
			print(line)
			if x<2: print('-----')
	def __is_full(self):
		return self.__empty==0
	def __who_win(self):
		for i in range(3):
			if self.get_cell(i,0)==self.get_cell(i,1) and self.get_cell(i,1)==self.get_cell(i,2): #row
				 return self.get_cell(i,0)
			if self.get_cell(0,i)==self.get_cell(1,i) and self.get_cell(1,i)==self.get_cell(2,i): #column
				return self.get_cell(0,i)
		if self.get_cell(0,0)==self.get_cell(1,1) and self.get_cell(1,1)==self.get_cell(2,2) \
		or self.get_cell(0,2)==self.get_cell(1,1) and self.get_cell(1,1)==self.get_cell(2,0):
			return self.get_cell(1,1)
		return False
	def is_finish(self):
		if self.__is_full(): return 'xo'
		else: return self.__who_win()

class Player:
	def __init__(self,sign):
		if sign!='x' and sign!='o': 
			raise NameError('SignPlayerWrong')
		self.sign=sign
	def do_turn(self,board):
			cell=self.__ask_turn()
			while board.get_cell(*cell): #if the cell is full
				print('The cell is full, try again!')
				cell=self.__ask_turn()
			return cell
	def __ask_turn(self):
		xy=''
		while not re.match('^[1-3] [1-3]$',xy):
			xy=input('Enter x&y of cell that you want to put sign on its:')
		x,y=xy.split()
		return int(x)-1,int(y)-1

class Manager:
	def __init__(self):
		self.x=Player('x')
		self.o=Player('o')
		self.board=Board()
	def start_game(self):
		has_finish=False
		cur_player=self.x
		while not has_finish:
			cell=cur_player.do_turn(self.board)
			self.board.set_cell(cur_player.sign,*cell)
			self.board.print()
			winner=self.board.is_finish()
			if winner:
				print('The game finished!')
				print('The winner is '+winner if winner!='xo' else 'Nobody win')
				return
			cur_player=self.o if cur_player==self.x else self.x


m=Manager()
m.start_game()
