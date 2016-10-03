from random import randint
import math
from copy import deepcopy
from operator import itemgetter

def boardPrint(board, N):
	root = int(math.sqrt(N))
	mstr = ""
	countx = 0
	county = 0
	for i in xrange(0,N):
		county+=1
		for j in xrange(0,N):
			countx += 1
			if(countx == root):
				countx = 0
				mstr = mstr + str(board[i][j]) + " | "
			else:
				mstr = mstr + str(board[i][j]) + " "
		mstr = mstr + "\n"
		if(county==root):
			county = 0
			mstr = mstr + "-----------------------"
			mstr = mstr + "\n"
	print (mstr)
def removeFromNeighbours(possible_values,n,chosenCell,present_value):
	positions_removed=[]
	root = int(math.sqrt(n))
	empty_domain = 0
	x = int(chosenCell[0]/root)
	y = int(chosenCell[1]/root)
	for i in xrange (0,n):
		j = chosenCell[1]
		if(i!=chosenCell[0] or j!=chosenCell[1]):
			if nonZeroLen(possible_values[i][j])!=0:
				if possible_values[i][j][present_value-1] != 0:
					positions_removed.append([i,j])
					possible_values[i][j][present_value-1] = 0
					if (nonZeroLen(possible_values[i][j])==0):
						empty_domain = 1

	for j in xrange (0,n):
		i = chosenCell[0]
		if(i!=chosenCell[0] or j!=chosenCell[1]):
			if nonZeroLen(possible_values[i][j])!=0:
				if possible_values[i][j][present_value-1] != 0:
					positions_removed.append([i,j])
					possible_values[i][j][present_value-1] = 0	
					if (nonZeroLen(possible_values[i][j])==0):
						empty_domain = 1
	for i in xrange (root*x,(root*x + root)):
		for j in xrange (root*y,(root*y + root)):
			if(i!=chosenCell[0] and j!=chosenCell[1]):
				if nonZeroLen(possible_values[i][j])!=0:
					if possible_values[i][j][present_value-1] != 0:
						positions_removed.append([i,j])
						possible_values[i][j][present_value-1] = 0
						if (nonZeroLen(possible_values[i][j])==0):
							empty_domain = 1
	cell_values = []
	for i in range (0,n):
		if(possible_values[chosenCell[0]][chosenCell[1]][i] != 0):
			cell_values.append(i+1)
			possible_values[chosenCell[0]][chosenCell[1]][i] = 0
	positions_removed.append(cell_values)
	positions_removed.append(empty_domain)
	return positions_removed
def addToNeighbours(possible_values,n,positions_removed,present_value,chosenCell):
	for i in xrange (0,len(positions_removed)-2):
		possible_values[positions_removed[i][0]][positions_removed[i][1]][present_value-1] = present_value
	for i in range(0,len(positions_removed[-2])):
		possible_values[chosenCell[0]][chosenCell[1]][positions_removed[-2][i]-1] = positions_removed[-2][i]
def checkValue(final_values,n,chosenCell,present_value):
	root = int(math.sqrt(n))
	x = int(chosenCell[0]/root)
	y = int(chosenCell[1]/root)
	found_val = 0
	for i in xrange (0,n):
		j = chosenCell[1]
		if(i!=chosenCell[0] or j!=chosenCell[1]):
			if(final_values[i][j]==present_value):
				found_val = 1
	for j in xrange (0,n):
		i = chosenCell[0]
		if(i!=chosenCell[0] or j!=chosenCell[1]):
			if(final_values[i][j]==present_value):
				found_val = 1
	for i in xrange (root*x,(root*x + root)):
		for j in xrange (root*y,(root*y + root)):
			if(i!=chosenCell[0] and j!=chosenCell[1]):
				if(final_values[i][j]==present_value):
					found_val = 1
	return found_val

def nonZeroLen(list):
	count = 0
	for i in xrange (0,len(list)):
		if list[i]!=0 and list[i]!=-1:
			count+=1
	return count

def maxDegreeHeur(possible_values,n):
	max_deg = -1
	root = int(math.sqrt(n))
	temp_deg = []
	for X in xrange (0,n):
		temp_deg.append([])
		for Y in xrange (0,n):
			deg = 0
			if(nonZeroLen(possible_values[X][Y])!=0):
				x = int(X/root)
				y = int(Y/root)
				for i in xrange (0,n):
					j = Y
					if (i!=X or j!=Y):
						if(nonZeroLen(possible_values[i][j])!=0):
							deg+=1
				for j in xrange (0,n):
					i = X
					if(i!=X or j!=Y):
						if(nonZeroLen(possible_values[i][j])!=0):
							deg+=1
				for i in xrange (root*x,(root*x + root)):
					for j in xrange (root*y,(root*y + root)):
						if(i!=X and j!=Y):
							if(nonZeroLen(possible_values[i][j])!=0):
								deg+=1
				temp_deg[X].append(deg)
				if max_deg < deg:
					max_deg = deg
			else:
				temp_deg[X].append(deg)
				if max_deg < deg:
					max_deg = deg
	max_deg_cells = []
	for i in xrange (0,n):
		for j in xrange (0,n):
			if(nonZeroLen(possible_values[i][j])!=0 and max_deg == temp_deg[i][j]):
				max_deg_cells.append([i,j])
	if len(max_deg_cells) == 0:
		return []
	else:
		#print "max-deg: ",max_deg
		index = randint(0,len(max_deg_cells)-1)
		#print "max-deg-var: ",max_deg_cells[index]
		return max_deg_cells[index]

def printposs(possible_values,n):
	for i in xrange(0,n):
		for j in xrange(0,n):
			print(nonZeroLen(possible_values[i][j])),
		print "\n"
def MRV(possible_values,n):
	min_count = 100005	
	for i in xrange (0,n):
		for j in xrange (0,n):
			length = nonZeroLen(possible_values[i][j])
			if (length != 0 and min_count > length):
				min_count = nonZeroLen(possible_values[i][j])
	min_count_cells = []
	for i in xrange (0,n):
		for j in xrange (0,n):
			if(min_count == nonZeroLen(possible_values[i][j])):
				min_count_cells.append([i,j])
	if len(min_count_cells) == 0:
		return []
	else:
		#print "min-no-of-unassigned-var: ",min_count
		index = randint(0,len(min_count_cells)-1)
		#print "min-unassigned-var: ",min_count_cells[index]
		#print possible_values[min_count_cells[index][0]][min_count_cells[index][1]]
		return min_count_cells[index]

def LCV(chosenCell,possible_values,n):
	root = int(math.sqrt(n))
	x = int(chosenCell[0]/root)
	y = int(chosenCell[1]/root)
	count_val = []
	for i in xrange (0,n):
		count_val.append([i+1,0])
	for i in xrange (0,n):
		j = chosenCell[1]
		if(i!=chosenCell[0] or j!=chosenCell[1]):
			for k in xrange (0,len(possible_values[i][j])):
				if(possible_values[i][j][k]!=0):
					count_val[possible_values[i][j][k]-1][1] += 1
	for j in xrange (0,n):
		i = chosenCell[0]
		if(i!=chosenCell[0] or j!=chosenCell[1]):
			for k in xrange (0,len(possible_values[i][j])):
				if(possible_values[i][j][k]!=0):
					count_val[possible_values[i][j][k]-1][1] += 1
	for i in xrange (root*x,(root*x + root)):
		for j in xrange (root*y,(root*y + root)):
			if(i!=chosenCell[0] and j!=chosenCell[1]):
				for k in xrange (0,len(possible_values[i][j])):
					if(possible_values[i][j][k]!=0):
						count_val[possible_values[i][j][k]-1][1] += 1
	return sorted(count_val, key=itemgetter(1))
def test(possible_values,n):
	for i in xrange (0,n):
		for j in xrange (0,n):
			for k in xrange (0,n):
				if(final_values[i][j]!=0):
					possible_values[i][j][k] = 0
				else:
					possible_values[i][j][k] = k+1

	root = int(math.sqrt(n))
	for X in xrange (0,n):
		for Y in xrange (0,n):
			if(final_values[X][Y]==0):
				x = int(X/root)
				y = int(Y/root)
				for i in xrange (0,n):
					j = Y
					if (i!=X or j!=Y):
						if(final_values[i][j]!=0):
							possible_values[i][j][k-1]=0
				for j in xrange (0,n):
					i = X
					if(i!=X or j!=Y):
						if(final_values[i][j]!=0):
							possible_values[i][j][k-1]=0
				for i in xrange (root*x,(root*x + root)):
					for j in xrange (root*y,(root*y + root)):
						if(i!=X and j!=Y):
							if(final_values[i][j]!=0):
								possible_values[i][j][k-1]=0
n = 9

possible_values = []
final_values = []
final_values_new = []

last_var_val_ordered = []
last_var = []
last_var_poss_val = []
removed_positions = []

option = input("Enter difficulty level: 1. Easy 2. Medium 3. Hard\n")
if option == 1:
	final_values = [[3, 9, 4, 1, 7, 2, 5, 8, 6], 
					 [1, 5, 0, 3, 8, 6, 0, 0, 9],
					 [0, 0, 6, 9, 4, 5, 7, 0, 3],
					 [5, 0, 8, 0, 9, 4, 0, 2, 1],
					 [0, 0, 1, 2, 6, 3, 8, 7, 5],
					 [7, 6, 0, 0, 5, 1, 0, 9, 0],
					 [0, 0, 3, 5, 2, 0, 0, 6, 7],
					 [6, 2, 0, 4, 0, 7, 0, 5, 8],
					 [0, 0, 0, 0, 1, 0, 4, 0, 2]]
elif option == 2:
	final_values = [[5,3,0,0,7,0,0,0,0],
					[6,0,0,1,9,5,0,0,0],
					[0,9,8,0,0,0,0,6,0],
					[8,0,0,0,6,0,0,0,3,],
					[4,0,0,8,0,3,0,0,1],
					[7,0,0,0,2,0,0,0,6],
					[0,6,0,0,0,0,2,8,0],
					[0,0,0,4,1,9,0,0,5],
					[0,0,0,0,8,0,0,7,9]]
elif option == 3:
	final_values = [[7, 0, 0, 0, 0, 0, 0, 0, 0],
              [6, 0, 0, 4, 1, 0, 2, 5, 0],
              [0, 1, 3, 0, 9, 5, 0, 0, 0],
              [8, 6, 0, 0, 0, 0, 0, 0, 0],
              [3, 0, 1, 0, 0, 0, 4, 0, 5],
              [0, 0, 0, 0, 0, 0, 0, 8, 6],
              [0, 0, 0, 8, 4, 0, 5, 3, 0],
              [0, 4, 2, 0, 3, 6, 0, 0, 7],
              [0, 0, 0, 0, 0, 0, 0, 0, 9]]
          
for i in xrange (0,n):
	possible_values.append([])
	for j in xrange (0,n):
		possible_values[i].append([])
		for k in xrange (0,n):
			if(final_values[i][j]!=0):
				possible_values[i][j].append(0)
			else:
				possible_values[i][j].append(k+1)

root = int(math.sqrt(n))
for X in xrange (0,n):
	for Y in xrange (0,n):
		if(final_values[X][Y]==0):
			x = int(X/root)
			y = int(Y/root)
			for i in xrange (0,n):
				j = Y
				if (i!=X or j!=Y):
					if(final_values[i][j]!=0):
						possible_values[i][j][k-1]=0
			for j in xrange (0,n):
				i = X
				if(i!=X or j!=Y):
					if(final_values[i][j]!=0):
						possible_values[i][j][k-1]=0
			for i in xrange (root*x,(root*x + root)):
				for j in xrange (root*y,(root*y + root)):
					if(i!=X and j!=Y):
						if(final_values[i][j]!=0):
							possible_values[i][j][k-1]=0
print "original puzzle"
boardPrint(final_values,n)
chosenCell = maxDegreeHeur(possible_values,n)
if len(chosenCell) == 0:
	print "solved puzzle"
	boardPrint(final_values,n)
	exit()
LCV_list = deepcopy(LCV(chosenCell,possible_values,n))
if len(LCV_list) == 0:
	print "solved puzzle"
	boardPrint(final_values,n)
	exit()
last_var_val_ordered.append(LCV_list)
last_var.append([chosenCell[0],chosenCell[1]])
last_var_poss_val.append(possible_values[chosenCell[0]][chosenCell[1]])
prev_val = final_values[chosenCell[0]][chosenCell[1]]
max_iter = 0
while(1):
	max_iter+=1
	num_of_iter = 0
	found = 1
	while(num_of_iter < len(LCV_list)):
		present_value = LCV_list[num_of_iter][0]
		found = checkValue(final_values,n,chosenCell,present_value)
		if found == 0 and present_value!=prev_val:
			removed_positions.append(removeFromNeighbours(possible_values,n,chosenCell,present_value))
			if(removed_positions[-1][-1]==1):
				addToNeighbours(possible_values,n,removed_positions[-1],final_values[chosenCell[0]][chosenCell[1]],chosenCell)
				del removed_positions[-1]
				found = 1
				num_of_iter+=1
			else:
				break
		else:
			num_of_iter+=1
	if(found == 1):
		#no possible value found, will backtrack now
		flag = 0
		while(1):
			del last_var_val_ordered[-1]
			del last_var[-1]
			del last_var_poss_val[-1]
			if flag == 1:
				del removed_positions[-1]
			else:
				flag = 1
			if len(last_var_val_ordered)==0:
				print "no soln, retry"
				exit()
			if len(last_var_val_ordered[-1])!=0:
				chosenCell[0] = last_var[-1][0]
				chosenCell[1] = last_var[-1][1]
				for i in range (0,len(last_var_val_ordered[-1])):
					if(last_var_val_ordered[-1][i][0] == final_values[chosenCell[0]][chosenCell[1]]):
						del last_var_val_ordered[-1][i]
						break
				LCV_list = deepcopy(last_var_val_ordered[-1])
				prev_val = final_values[chosenCell[0]][chosenCell[1]]
				final_values[chosenCell[0]][chosenCell[1]] = 0
				break	
	if(found == 0):
		final_values[chosenCell[0]][chosenCell[1]]=present_value
		chosenCell = deepcopy(MRV(possible_values,n))
		if len(chosenCell) == 0:
			flag = 0
			for i in range (0,n):
				for j in range (0,n):
					if(final_values[i][j]==0):
						flag = 1
			if (flag == 0):
				print "solved puzzle"
				boardPrint(final_values,n)
				exit()
			else:
				test(possible_values,n)
				chosenCell = deepcopy(MRV(possible_values,n))
		LCV_list = deepcopy(LCV(chosenCell,possible_values,n))
		if len(LCV_list) == 0:
			flag = 0
			for i in range (0,n):
				for j in range (0,n):
					if(final_values[i][j]==0):
						flag = 1
			if (flag == 0):
				print "solved puzzle"
				boardPrint(final_values,n)
				exit()
			else:
				test(possible_values,n)
				chosenCell = deepcopy(MRV(possible_values,n))
		last_var_val_ordered.append(LCV_list)
		last_var.append([chosenCell[0],chosenCell[1]])
		last_var_poss_val.append(possible_values[i][j])
		prev_val = final_values[chosenCell[0]][chosenCell[1]]