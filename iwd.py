# INTELLIGENT WATER DROPS ALGORITHM
import random, math
from random import choice

# the example Disassembly Matrix
global DM
DM = [
     [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0], 
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
     [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

## parameters
# static parameters

# take number of parts and directions from DM
global no_of_parts, no_of_dirs, no_of_nodes, no_of_iwds
no_of_parts = len(DM) # Keep these properties dependent so that changes can be easily made
no_of_dirs = len(DM[1]) / len(DM) # ---------------do----------------#

no_of_nodes = 2 * no_of_dirs * no_of_parts 
no_of_iwds = no_of_parts # equal to number of parts

# parameters for velocity updating
global a_v, b_v, c_v
a_v = 1000
b_v = 0.01
c_v = 1

# parameters for soil updating
global a_s, b_s, c_s 
a_s = 1000
b_s = 0.01
c_s = 1

# initial velocity
global init_vel, initsoil
init_vel = 100
init_soil = 1000 # initialize the soil on every path by this amount

# best tour is T_b
global T_b, len_best_tour
T_b = []
len_best_tour = float("inf")#len(T_b)

# maximum number of iterations
iter_max = 100

# defining IWD class
class iwd(object):
    # initializing the nodes and parts list and also
    # water drop's velocity and soil amount
    def __init__(self):
        self.visited_nodes = []
        self.visited_parts = []
        self.velocity = init_vel
        self.soil = init_soil

    # adding a node and a part number to the list
    # node is an ordered pair of part no. and dir
    # so node[0] is to be added to part list
    def add_node(self, node):
        self.visited_nodes.append(node)
        self.visited_parts.append(node[0])

    def get_nodes_list(self):
        return self.visited_nodes

    def get_parts_list(self):
        return self.visited_parts

    def get_no_parts(self):
        return len(self.visited_parts) 

# some useful functions
# getting the direction from number
def getDir(dir_no, positive):
    if positive:
        return dir_no + 1
    else:
        return -(dir_no + 1)

# definition of the probability given in the paper
def node_prob(node_1, node_2):
    



# create the array of water drops
# first get the possible nodes list
# for that we define a function
def get_next_possible_nodes(used_parts):
    possible_nodes_list = []
    # iterating over all the parts
    for part_no in range(no_of_parts):
        if used_parts.count(part_no) == 0:
            for dir_no in range(no_of_dirs):
                pos_dir_truth = True
                neg_dir_truth = True
                for check_part in range(no_of_parts):
                    if used_parts.count(check_part) == 0:
                        # checking in +k direction 
                        #if already obstructing, skip
                        if pos_dir_truth:
                            row_no = part_no
                            col_no = check_part * no_of_dirs + dir_no
                            if DM[row_no][col_no] == 1:
                                pos_dir_truth = False
                        # checking in -k direction
                        if neg_dir_truth:
                            row_no = check_part
                            col_no = part_no * no_of_dirs + dir_no
                            if DM[row_no][col_no] == 1:
                                neg_dir_truth = False
                if pos_dir_truth:
                    possible_nodes_list.append((part_no, getDir(dir_no, True)))
                if neg_dir_truth:
                    possible_nodes_list.append((part_no, getDir(dir_no, False)))

    return possible_nodes_list

# procedure starts from here
# initialization of the water drops at their start
# print statements embedded in the block here for debug
print "The initial iwds are:"
init_nodes = get_next_possible_nodes([])
water_drop_list = []
for i in range(no_of_iwds):
    new_water_drop = iwd()
    node = choice(init_nodes)
    new_water_drop.add_node(node)
    water_drop_list.append(new_water_drop)

    print new_water_drop.get_nodes_list(), new_water_drop.get_parts_list()
# DEBUG
print "----"

iter_no = 1
while iter_no <= iter_max:
    for water_drop in water_drop_list:
        parts_visited = water_drop.get_parts_list()
        next_poss_nodes = get_next_possible_nodes(parts_visited)



    iter = iter + 1
