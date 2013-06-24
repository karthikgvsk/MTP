### AN ANT COLONY BASED OPTIMIZATION APPROACH 
### FOR ASSEMBLY PROCESS PLANNING

#importing random module
import random

# Disassembly Matrix
# example 1
"""
DM = [[0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0], 
	  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	  [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
	  [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]
"""

"""
# exmaple 2
DM = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1], 
	  [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
	  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
	  [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]]
"""
# example 3
DM = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]

### HELPER FUNCTIONS AND OBJECTS 

# defining the Ant class, which gets the feasible sequences
class Ant(object):
	def __init__(self):
		# each ant has two properties:
		# 1. nodes that it visited called nodes_list
		# 2. parts that is visited called parts_list
		self.nodesList = []
		self.partsList = set()

	# method to add a node to the ant's node list
	# both nodes_list and parts_list are modified
	def addNode(self, Node):
		self.nodesList.append(Node)
		self.partsList.add(Node[0])

# function to get the direction name from direction number
def getDir(num):
	if num == 1:
		return "x"
	elif num == -1:
		return "-x"
	elif num == 2:
		return "y"
	elif num == -2:
		return "-y"
	elif num == 3:
		return "z"
	elif num == -3:
		return "-z"

# from the direction name or the value associated with the name (like +x = +1, -x = -1...), 
# get the absolute valuew of direction 
# mostly for usage in getting row and col numbers of pheromone matrix
def getTransDir(k):
	if k == 1 or k == 'x':
		return 0
	if k == -1 or k == '-x':
		return 1
	if k == 2 or k == 'y':
		return 2
	if k == -2 or k == '-y':
		return 3
	if k == 3 or k == 'z':
		return 4
	if k == -3 or k == '-z':
		return 5

# given the node and number of directions considered in the example, 
# returns the index of DM
def getIndex(node, d):
	i = node[0]
	k = node[1]
	return i * d + getTransDir(k)
	
# from a given list of next possible DO's with associated probabilities, 
# it returns a random node
def genRandomDO(probabilityList):
	# sorting the list according to probabilities
	# procedure borrowed from internet
	l = len(probabilityList)
	i = 0
	while i < l:
		j = i + 1
		while j < l:
			p1 = probabilityList[i]
			p2 = probabilityList[j]
			if p1[-1] > p2[-1]:
				temp = probabilityList[i]
				probabilityList[i] = probabilityList[j]
				probabilityList[j] = temp
			j = j + 1
		i = i + 1
		
	# getting the random element
	totals = []
	running_total = 0
	for w in probabilityList:
		running_total = running_total + w[-1]
		totals.append(running_total)
	
	rnd = random.random() * running_total
	for i, total in enumerate(totals):
		if rnd < total:
			return probabilityList[i]

### PARAMETERS ###
#number of parts
n = len(DM)
#number of directions
d = len(DM[1]) / len(DM)
#print n, d
# total cycles
NCmax = 100
# initial pheronome value
t0 = 1
# importance factor
beta = 0.8 
# evaporation parameters
rho = 0.1
gamma = 0.1
# constant Q (given 1 for an example in paper)
Q = 1.1

# part list
partsList = set()
i = 0
while i < n:
	partsList.add(i)
	i = i + 1


# Pheromone matrix
PM = []
i = 0
while i < 2 * d * n:
	l = []
	j = 0
	while j < 2 * d * n:
		l.append(t0)
		j = j + 1
	PM.append(l)
	i = i + 1

## generating the initial feasible DOs(disassembly operations)
initDOlist = []
# iterating over each component
for i in range(n):
	for k in range(d):
		# +k direction
		truth = True
		j = 0
		stop = False
		while j < n and not stop:
		# As in the article, 
		# I(i, j, k) = DM[i][j * d + k]
			if DM[i][j * d + k] != 0:
				truth = False
				stop = True
			j = j + 1
		if(truth and not stop):
			initDOlist.append((i, k + 1))

		# -k direction
		truth = True
		j = 0
		stop = False
		while j < n and not stop:
		# As in the article, 
		# I(j, i, k) = DM[j][i * d + k]
			if DM[j][i * d + k] != 0:
				truth = False
				stop = True
			j = j + 1
		if(truth and not stop):
			initDOlist.append((i, -(k + 1)))



# number of ants
na = len(initDOlist)

bestSeqList = [None] * na

### MAIN LOOP ###
#cycle counter setting
NC = 1
#print NC
# create ants with the above list
NCmax = int(raw_input("enter no. of iterations > "));
while NC < NCmax:
	#print "+++++++++++++++++++++++++++++++++++"
	#print "ITERATION :", NC
	#print "---------------------------"
	# generating the ant list
	# adding the initial ants
	acount = 0
	antList = [None] * na
	while acount < na:
		antList[acount] = Ant()
		Node = initDOlist[acount]
		antList[acount].addNode(Node)
		acount = acount + 1

	# iterating over the antlist until the paths for all ants are done
	compTour = [False] * na
	stop = False
	while not stop:
	
		## iterator over the ant list to determine its next node and updating stuff..
		i = 0
		while i < len(antList):
			if antList[i].partsList == partsList or len(antList[i].partsList) == n:
				compTour[i] = True
			else:
				ant = antList[i]
				prevParts = ant.partsList
				# generating candidate list of ant (next possible node)
				# generate the feasible list of parts (remaining parts)
				feasibleList = []
				for part in partsList:
					if not prevParts.__contains__(part):
						feasibleList.append(part)
				#print i, ant.partsList, feasibleList
				if len(feasibleList) == 0:
					compTour[i] = True
				else:
				
					# generating the next DOs possible in the remaining parts
					feasDOList = []
					for p in feasibleList:
						# +k direction
						for k in range(d):
							# +k direction
							truth = True
							stop = False
							for q in feasibleList:
								if DM[p][q * d + k] != 0:
									truth = False
									Stop = True
						
							if truth and not stop:
								feasDOList.append((p, k+1))

						# -k direction
						for k in range(d):
							truth = True
							stop = False
							for q in feasibleList:
								if DM[q][p * d + k] != 0:
									truth = False
									Stop = True
							
							if truth and not stop:
								feasDOList.append((p, -(k + 1)))
					
					if len(feasDOList) == 0:
						compTour[i] = True
					else:
						antNodes = antList[i].nodesList
						lastNode = antNodes[-1]
						lnRowNum = getIndex(lastNode, d)
						
						# the code for random picking of the next DO based on its probability
						probabilityList = []
						for DO in feasDOList:
							preRowNum = getIndex(DO, d)
					
							###
							# calculating the probability
							eeta = 1
							# eeta factor reduces if directions are unequal
							if lastNode[1] != DO[1]:
								eeta = 0.2
							prob = PM[lnRowNum][preRowNum] * (eeta ** beta)
							###

							probabilityList.append((lnRowNum, preRowNum, DO[0], DO[1], prob))
				
						nextNode = genRandomDO(probabilityList)
						#print "ant: ", i, ", node chosen: ", nextNode
						nextDO = (nextNode[2], nextNode[3])
						antList[i].addNode(nextDO)

						# updating the pheromone matrix locally
						lrn = nextNode[0]
						nrn = nextNode[1]
						PM[lrn][nrn] = (1 - rho) * PM[lrn][nrn] + (rho * t0)
						#print PM[lrn][nrn]


			i = i + 1

		## Stopping the loop on the "ants list iteration until path completion"
		truth = True
		for tour in compTour:
			if tour == False:
				truth = False

		if truth:
			stop = True
		# debugging
		#print compTour
		
		#stop = True	

	# every ant in antlist has completed its journey, now updating the pheromone globally
	### Determining the iteration best(min reorientations) sequences
	na = len(antList)
	i = 0
	minChanges = 2 * n
	while i < na:
		ant = antList[i]
		DOList = ant.nodesList
		count = 0
		j = 1
		while j < len(DOList):
			prevDO = DOList[j - 1]
			presDO = DOList[j]
			if prevDO[-1] != presDO[-1]:
				count = count + 1	
			j = j + 1
			
		#print "ant:", i, "dir changes:", count
		
		### updating the best sequence list:
		
		if bestSeqList[i] == None:
			DOSeq = ant.nodesList
			bestSeqList[i] = (DOSeq, count)
		else:
			lastSeq = bestSeqList[i]
			if lastSeq[-1] > count:
				DOSeq = ant.nodesList
				bestSeqList[i] = (DOSeq, count)
		###
		
		
 		if minChanges > count:
			minChanges = count
		
		i = i + 1
	###
	
	### determining the number of ants with iteration best sequences
	i = 0
	antCount = 0
	while i < na:
		ant = antList[i]
		DOList = ant.nodesList
		count = 0
		j = 1
		while j < len(DOList):
			prevDO = DOList[j - 1]
			presDO = DOList[j]
			if prevDO[-1] != presDO[-1]:
				count = count + 1	
			j = j + 1
		if minChanges == count:
			antCount = antCount + 1

		i = i + 1
	###
	
	### basic evaporation update of PM
	i = 0
	while i < 2 * d * n:
		j = 0
		while j < 2 * d * n:
			PM[i][j] = (1 - gamma) * PM[i][j]
			j = j + 1
		i = i + 1
		
	### adding to PM the DO's of iteration best sequences
	i = 0
	while i < na:
		ant = antList[i]
		DOList = ant.nodesList
		count = 0
		j = 1
		while j < len(DOList):
			prevDO = DOList[j - 1]
			presDO = DOList[j]
			if prevDO[-1] != presDO[-1]:
				count = count + 1	
			j = j + 1
		if minChanges == count:
			#print "ant:", i, "has minimum DO changes of ", count
			#print "antCount : ", antCount
			#print "added probability: ", (antCount) * (Q / (minChanges + 1))
			j = 0
			while j < len(DOList) - 1:
				
				presDO = DOList[j]
				nextDO = DOList[j + 1]
				presRowNum = getIndex(presDO, d)
				nextRowNum = getIndex(nextDO, d)
				#print "updating element: ", presRowNum, nextRowNum
				PM[presRowNum][nextRowNum] = PM[presRowNum][nextRowNum] + antCount * Q / (minChanges + 1)
				j = j + 1
				
		i = i + 1
	###
		
	NC = NC + 1
	i = 0
	while i < 2 * d * n:
		j = 0
		s = ""
		while j < 2 * d * n:
			s = s + " " + "%.2f" % PM[i][j]   #str(int(PM[i][j]))
			j = j + 1
		#print s
		i = i + 1
	#print "++++++++++++++++++++++++++++++"
	#print "++++++++++++++++++++++++++++++"
	
#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

i = 0
while i < len(bestSeqList):
	seq = bestSeqList[i]
	print "ant: ", i, " bestSeq: ", bestSeqList[i]
	i = i + 1
