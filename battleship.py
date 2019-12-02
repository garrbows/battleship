coordDict = {    
            0:'a',
            1:'b',
            2:'c',
            3:'d',
            4:'e',
            5:'f',
            6:'g',
            7:'h',
            8:'i',
            9:'j',
}

opponents = [
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
            ]

yours = [
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.','.','.'],
            ]

def print_boards():
		
		#prints out layout of chessboard before every move

		print('player 2')
		for i in range(len(opponents)): 
			print(coordDict[i]+"    "+'   '.join(opponents[i]))
		print("     "+"   ".join([str(i) for i in range(10)]))

		print('player 1')
		for i in range(len(yours)):
			print(coordDict[i]+"    "+'   '.join(yours[i]))    
		print("     "+"   ".join([str(i) for i in range(10)]))

def get_tile(board,location):
	return board[location[1]][location[0]]

def set_tile(board,location,char):
	board[location[1]][location[0]] = char

def place_ship(board,location_origin,length,vertical):
    #location: tuple of coordinates of top of ship
    #length: int to represent length of ship
    #vertical: bool is true if ship is vertical
    #place_ship returns False if placement is invalid

	#place_ship will place partial ships if they leave the board boundaries

	x = 0
	y = 0

	location = location_origin
    
	for i in range(length):
		location = (location_origin[0]+x,location_origin[1]+y)
		try:
			set_tile(board,location,"*")
		except:
			print("Failed to place ship")
			return False
		if vertical:
			y += 1
		else:
			x += 1
		
	return False


rows = 10
columns = 10
place_ship(yours,(3,5),4,False)
print_boards()



























