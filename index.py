#import
import os 
import time 
import random 

#define board
board= [""," "," "," "," "," "," "," "," "," "]


def print_board() :
	print('   |   |   ')
	print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
	print('   |   |   ')
	print('---|---|---')
	print('   |   |   ')
	print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
	print('   |   |   ')
	print('---|---|---')
	print('   |   |   ')
	print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
	print('   |   |   ')

def is_winner(board, player):

	if  (board[1]==player and board[2]==player and board[3]==player) or \
		(board[4]==player and board[5]==player and board[6]==player) or \
		(board[7]==player and board[8]==player and board[9]==player) or \
		(board[1]==player and board[4]==player and board[7]==player) or \
		(board[2]==player and board[5]==player and board[8]==player) or \
		(board[3]==player and board[6]==player and board[9]==player) or \
		(board[1]==player and board[5]==player and board[9]==player) or \
		(board[7]==player and board[5]==player and board[3]==player) :
		return True	
	else :
		return False	

def is_board_full(board) :	
		#check for a tie 
	if " " in board :
		return False
	else :
		return True

def get_computer_move(board, player) :

	if player=='O':
		opponent= 'X'
	else:
		opponent='O'	
	
	# # #Check Column win

	# for i in [1,2,3] :
	# 	if board[i]==player and board[i+3]==player and board[i+6]==" " :
	# 		return i+6
	# 	if board[i+6]==player and board[i+3]==player and board[i]==" " :
	# 		return i
	# 	if board[i]==player and board[i+6]==player and board[i+3]==" " :
	# 		return i+3
	# #Check for Row 
	
	# for i in [1,4,7] :
	# 	if board[i]==player and board[i+1]==player and board[i+2]==" " :
	# 		return i+2
	# 	if board[i+2]==player and board[i+1]==player and board[i]==" " :
	# 		return i
	# 	if board[i]==player and board[i+2]==player and board[i+1]==" " :
	# 		return i+1

	# #Check for dilgonal

#Check if next move is a win for player
	#Instead of checking each and column we can iterate from 1 to 9 and check whether that move will result in a win or not

	for i in range(1,10) : 
		if board[i]==" ":
			board[i]= player
			if is_winner(board, player):
				return i
			else :
				board[i]=" "

#Check if next move is a win for opponent
	for i in range(1,10) : 
		if board[i]==" ":
			board[i]= opponent
			if is_winner(board, opponent):
				return i
			else :
				board[i]=" "


	#if center is empty choose it  
	if board[5]==" " :
		return 5

	move= random.randint(1,9)
	while(board[move]!=" ") :
		move= random.randint(1,9)
	return move			


while True :
	os.system("cls")
	print_board()

	#For Player X
	choice = input("Choose an empty space for X : ")
	choice = int(choice)

	#check id space is empty or not
	while board[choice]!=' ':
		print("It's filled, choose some other space")
		time.sleep(1)
		os.system("cls")
		print_board()
		choice = input("Choose an empty space for X : ")
		choice = int(choice)
		
	board[choice]='X'	

	os.system("cls")
	print_board()	

	#check for X Win
		
	if is_winner(board,"X"):

		os.system("cls")
		print_board()
		print("Congrats. Player X, You win! ")
		break

	if is_board_full(board) : 	
		print("TIE")
		break	

#For computer as Player O (sSingke Player Mode)
	choice= get_computer_move(board,'O')


#For Player O (In two player MODE)
	# choice = input("Choose an empty space for O : ")
	# choice = int(choice)
	#check if space is empty or not
	# while board[choice]!=" ":
	# 	print("It's filled, choose some other space")
	# 	time.sleep(1)
	# 	os.system("cls")
	# 	print_board()
	# 	choice = input("Choose an empty space for O : ")
	# 	choice = int(choice)

	board[choice]='O'	

	#check for O Win
		
	if	is_winner(board,'O'):
		os.system("cls")
		print_board()
		print("Congrats. Player O, You win! ")
		break	


	if is_board_full(board): 	
		print("TIE")
		break	


