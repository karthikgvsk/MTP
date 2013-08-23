# IWD ALGORITHM FOR ASSEMBLY SEQUENCE PLANNING PROBLEM
# ASSEMBLY (NOT DISASSEMBLY) IS USED

import random, math
from random import choice

### parameters


# disassembly matrix

DM = [
     [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0], 
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
     [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

"""
DM = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]
"""


# precedence matrix
PM = [
	 [0, 0, 0, 1], 
	 [0, 0, 0, 1], 
	 [0, 0, 0, 1], 
	 [0, 0, 0, 0]
	 ]

"""
PM = [
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	 ]
"""

# contact matrix



global no_of_parts, no_of_dirs, no_of_nodes
no_of_parts = len(DM)
no_of_dirs = len(DM[1]) / len(DM)
no_of_nodes = 2 * no_of_dirs * no_of_parts

# parts set
global parts_set
parts_set = set()
for i in range(no_of_parts):
	parts_set.add(i)



## static parameters

# velocity updating
global a_v, b_v, c_v, init_vel
a_v = 1
b_v = 0.01
c_v = 1
#initial velocity
# should be tuned by user
init_vel = 200

# soil updating
global a_s, b_s, c_s, p_n, p_iwd, init_soil
a_s = 1
b_s = 0.01
c_s = 1
# local soil updating parameter
p_n = 0.1
# global soil updating parameter
p_iwd = 0.1
#initial amount of soil 
#user selected, as given in the paper
#should be tuned experimentally
init_soil = 1000

# some other parameters
global e_s
e_s = 0.01 # as given in the paper

no_water_drops = no_of_parts

# cost parateters
min_cost = 2
max_cost = 10



# soil matrix
global SM
SM = []
for i in range(no_of_nodes):
	l = []
	for j in range(no_of_nodes):
		l.append(init_soil)
	SM.append(l)

#print SM


def soil_row_no(node):
    part_no = node[0]
    dir_no = node[1]
    sum1 = part_no * 2 * no_of_dirs
    sum2 = 0
    if dir_no == 1:
        sum2 = 0
    if dir_no == -1:
        sum2 = 1
    if dir_no == 2:
        sum2 = 2
    if dir_no == -2:
        sum2 = 3
    if dir_no == 3:
        sum2 = 4
    if dir_no == -3:
        sum2 = 5

    return sum1 + sum2




## dynamic parameters
# water drop object
class iwd(object):
	def __init__(self):
		self.nodes = []
		self.parts = []
		self.velocity = init_vel
		self.soil = 0.0
		self.best_seq = []
		self.best_len = float("inf")


	def tour_completed(self):
		return (set(self.parts) == parts_set)

	
	# THE MAJOR METHOD, ADDING A NODE TO THE WATER DROP
	def add_next_node(self):
		next_poss_nodes = []
		for i in range(no_of_parts):
			if not self.parts.__contains__(i):
				for d in range(no_of_dirs):
					pos_dir_poss = True
					neg_dir_poss = True
					# iterating over all the parts
					# next part should not interfere with already assembled parts
					# and next part should not have the 
					# requirement of presence another unassembled part in the assembly
					for j in range(no_of_parts):
						# is j is in assembled parts list, 
						# check for interference
						if self.parts.__contains__(j):
							row = i
							col = j * no_of_dirs + d
							if DM[row][col] == 1:
								#print i, j, d + 1, "interference"
								pos_dir_poss = False

							row = j
							col = i * no_of_dirs + d
							if DM[row][col] == 1:
								#print i, j, -(d + 1), "interference"
								neg_dir_poss = False
						# else if j is in remaining parts, 
						# check for precedence
						
						else:

							row = i
							col = j
							if PM[row][col] == 1:
								#print i, j, "precedence"
								pos_dir_poss = False
								neg_dir_poss = False
						
					if pos_dir_poss:
						next_poss_nodes.append((i, -1 * (d + 1)))
					if neg_dir_poss:
						next_poss_nodes.append((i, (d + 1)))

		#print "next poss nodes: ", next_poss_nodes
		if len(next_poss_nodes) > 0:		
			if len(self.nodes) == 0:
				node = random.choice(next_poss_nodes)
				self.nodes.append(node)
				self.parts.append(node[0])
			else:
				# implement random functionality
				prev_node = self.nodes[-1]
				prev_row_no = prev_node[1]
				soil_list = []
				for node in next_poss_nodes:
					row_no = soil_row_no(node)
					soil_list.append(SM[prev_row_no][row_no])

				# g function (as given in the paper)
				g_list = soil_list
				if min(soil_list) < 0:
					temp = min(soil_list)
					g_list = [(x - temp) for x in g_list]

				# f function (as given in the paper)
				f_list = [(1 / (e_s + x)) for x in g_list]

				# p function (probability list) (as given in the paper)
				temp = sum(f_list)
				p_list = [(x / temp) for x in f_list]

				# the approach for obtaining ramdom DO from a list with given probabilities
				x = random.uniform(0, 1)
				cumulative_prob = 0.0
				for node, prob in zip(next_poss_nodes, p_list):
					cumulative_prob += prob
					if x < cumulative_prob:
						break

				# appending the probable node and probable part
				self.nodes.append(node)
				self.parts.append(node[0])

				# updating the velocity ans soil amounts
				
				# velocity updating
				row = soil_row_no(prev_node)
				col = soil_row_no(node)
				soil_amt = SM[row][col]
				frac = a_v / (b_v + c_v * (soil_amt ** 2))
				self.velocity = self.velocity + frac 
				
				# soil updating
				dist = min_cost
				if not (prev_node[1] == node[-1]):
					dist = max_cost
				time = dist / self.velocity

				frac_soil = a_s / (b_s + c_s * (time ** 2))

				# updating soil matrix
				SM[row][col] = (1 - p_n) * SM[row][col] - p_n * frac_soil
				#print "soil updated: ", SM[row][col]
				self.soil = self.soil + frac_soil

				return node, prob, p_list

			# there are possible nodes sti
			return True
		else:
			return False



	def clean(self):
		self.nodes = []
		self.parts = []
		self.velocity = init_vel
		self.soil = 0.0



# creating a list of water drops
water_drop_list = []
for i in range(no_of_parts):
	water_drop = iwd()
	#water_drop.add_next_node()
	water_drop_list.append(water_drop)





iter_max = int(raw_input("Number of iterations > "))
iter_no = 1
while iter_no <= iter_max:

	tour_complete = [False]

	while tour_complete.__contains__(False):
		#print SM
		tour_complete = []
		for water_drop in water_drop_list:
			#print "\n---"
			truth = water_drop.add_next_node()
			if (not truth) or water_drop.tour_completed():
				tour_complete.append(True)
			else:
				tour_complete.append(False)
			#print "nodes: ", water_drop.nodes
			#print "----\n"


	# updating the values for the present iteration
	no_of_changes = []
	for water_drop in water_drop_list:
		changes = 0
		if set(water_drop.parts) == parts_set:
			for i in range(1, len(water_drop.nodes)):
				prev_node = water_drop.nodes[i - 1]
				node = water_drop.nodes[i]
				if prev_node[1] != node[1]:
					changes = changes + 1
		else:
			changes = no_of_parts
		no_of_changes.append(changes)

	_min = min(no_of_changes)
	for water_drop in water_drop_list:
		if set(water_drop.parts) == parts_set:
			changes = 0
			for i in range(1, len(water_drop.nodes)):
				prev_node = water_drop.nodes[i - 1]
				node = water_drop.nodes[i]
				if prev_node[1] != node[1]:
					changes = changes + 1

			# updating the best sequence of the water drop
			prev_len = water_drop.best_len
			if prev_len > changes:
				water_drop.best_len = changes
				water_drop.best_seq = water_drop.nodes

			if _min == changes:
				# is this node contains iteration best sequence, make the relavant changes

				# updating the soils
				for i in range(1, len(water_drop.nodes)):
					prev_node = water_drop.nodes[i-1]
					node = water_drop.nodes[i]

					row = soil_row_no(prev_node)
					col = soil_row_no(node)


					SM[row][col] = (1 + p_iwd) * SM[row][col] - p_iwd * (1 / (len(water_drop.nodes) - 1)) * water_drop.soil

	i = 0

	print "Iteration : ", iter_no
	for water_drop in water_drop_list:
		print "---"
		print "node: ", i
		print "\npresent seq : ", water_drop.nodes, len(water_drop.nodes)
		print "\nbest seq: ", water_drop.best_seq, water_drop.best_len
		print "---\n"
		water_drop.clean()
		i = i + 1
	print "========\n\n"
	
	iter_no = iter_no + 1;