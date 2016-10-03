from random import randint
n = 8
grid = [[0 for x in range(n)] for y in range(n)]
coordinates = []
def initVal():
	for i in range (0,n):
		for j in range (0,n):
			grid[i][j]=0;
	while len(coordinates) > 0 : coordinates.pop()
	for i in range (0,n):
		temp = randint(0,n-1)
		grid[temp][i] = 1
		coordinates.append(temp)
	presHeur = calcHeur()
	for i in range (0,n):
		print grid[i]
	print "Heuritic value: ",presHeur
	print('\n')
	return presHeur
def calcHeur():
	heuristic = 0
	for i in range (0,n):
		for j in range (0,n):
			if (i!=j):
				if (coordinates[i]==coordinates[j]):
						heuristic=heuristic+1
				elif (abs(i-j)==abs(coordinates[i]-coordinates[j])):
					heuristic=heuristic+1
	return heuristic/2
def makeMoveSteepest(presHeur,searchCost):
	mini = presHeur
	best_space = []
	comp_space = []
	for i in range(0,n):
		comp_space.append([])
	for i in range (0,n):
		for j in range (0,n):
			if grid[j][i]==0:
				searchCost=searchCost+1
				grid[coordinates[i]][i]=0
				grid[j][i]=1
				temp_coord = coordinates[i]
				coordinates[i]=j
				temp = calcHeur()
				if(mini>temp):
					mini=temp
				comp_space[i].append(temp);
				coordinates[i]=temp_coord
				grid[coordinates[i]][i]=1
				grid[j][i]=0
			else:
				comp_space[i].append(presHeur);
	if (mini == presHeur):
		return mini,searchCost
	else:
		index=0
		presHeur=mini
		for i in range (0,n):
			for j in range (0,n):
				if (comp_space[i][j]==mini):
					best_space.append([])
					best_space[index].append(i)
					best_space[index].append(j)
					index=index+1
		newIndex = randint(0,index-1)
		colIndex = best_space[newIndex][0]
		rowIndex = best_space[newIndex][1]
		grid[rowIndex][colIndex]=1
		grid[coordinates[colIndex]][colIndex]=0
		coordinates[colIndex]=rowIndex
		return mini,searchCost
def makeMoveSimple(presHeur,searchCost):
	mini = presHeur
	mark_vis = []
	for i in range (0,n):
		for j in range (0,n):
			mark_vis.append([j,i])
	while mark_vis:
		randIndex = randint(0,len(mark_vis)-1)
		i = mark_vis[randIndex][1]
		j = mark_vis[randIndex][0]
		if grid[j][i]==0:
			searchCost=searchCost+1
			grid[coordinates[i]][i]=0
			grid[j][i]=1
			temp_coord = coordinates[i]
			coordinates[i]=j
			temp = calcHeur()
			if(temp<mini):
				mini=temp
				return mini,searchCost
			else:
				coordinates[i]=temp_coord
				grid[coordinates[i]][i]=1
				grid[j][i]=0
				del mark_vis[randIndex]
		else:
			del mark_vis[randIndex]
	return mini,searchCost
def withRandomRestart():
	option = input("Choose Option: 1 - Simple Hill Climbing , 2 - Steepest Hill Climbing: ")
	restartCount = 0
	presHeur = initVal()
	searchCost = 0
	while(True):
		if option == 1:
			presHeurNew,searchCost=makeMoveSimple(presHeur,searchCost)
		else:
			presHeurNew,searchCost=makeMoveSteepest(presHeur,searchCost)
		if (presHeurNew == 0):
			for i in range (0,n):
				print grid[i]
			print "Heuristic value: ",presHeurNew
			print('\n')
			print 'total number of places checked (including restarts): ',
			print searchCost
			print 'total number of restarts: ',
			print restartCount
			break
		elif(presHeurNew==presHeur):
			print 'Restart'
			restartCount=restartCount+1
			if(restartCount<=8):
				presHeur = initVal()
			else:
				for i in range (0,n):
					print grid[i]
				print "Heuristic value: ",presHeurNew
				print('\n')
				print 'total number of places checked (including restarts): ',
				print searchCost
				print 'total number of restarts: ',
				print restartCount-1
				break
		else:
			presHeur=presHeurNew
			for i in range (0,n):
				print grid[i]
			print "Heuristic value: ",presHeurNew
			print('\n')	
def withoutRandomRestart():
	option = input("Choose Option: 1 - Simple Hill Climbing , 2 - Steepest Hill Climbing: ")
	restartCount = 0
	presHeur = initVal()
	searchCost = 0
	while(True):
		if option == 1:
			presHeurNew,searchCost=makeMoveSimple(presHeur,searchCost)
		else:
			presHeurNew,searchCost=makeMoveSteepest(presHeur,searchCost)
		if (presHeurNew == 0 or presHeurNew==presHeur):
			for i in range (0,n):
				print grid[i]
			print "Heuristic value: ",presHeurNew
			print('\n')
			print 'total number of places checked (including restarts): ',
			print searchCost
			print 'total number of restarts: ',
			print restartCount
			break
		else:
			presHeur=presHeurNew
			for i in range (0,n):
				print grid[i]
			print "Heuristic value: ",presHeur
			print('\n')
option = input("Choose Option: 1 - With Random Restart , 2 - Without Random Restart: ")
if option == 1:
	withRandomRestart()
else:
	withoutRandomRestart()