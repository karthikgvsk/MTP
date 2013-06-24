# INTELLIGENT WATER DROPS ALGORITHM
import random, math
from random import choice
debug_file = open("iwd.out", 'w')

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
# a parts set, useful
global parts_set
parts_set = set()
for i in range(no_of_parts):
    parts_set.add(i)


# parameters for velocity updating
global a_v, b_v, c_v
a_v = 1
b_v = 0.01
c_v = 1

# parameters for soil updating
global a_s, b_s, c_s 
a_s = 1
b_s = 0.01
c_s = 1

# initial velocity
global init_vel, initsoil
init_vel = 1
init_soil = 10 # initialize the soil on every path by this amount

# best tour is T_b
global T_b, len_best_tour
T_b = []
len_best_tour = float("inf")#len(T_b)

# maximum number of iterations
iter_max = int(raw_input("No of iterations > "))

## some other constants given in the algo
global e_v, rho
e_v = 0.0001
rho = 0.1

## SOIL MATRIX
# soil matrix is a aquare matrix
# which contains soil in edge from node i to node j
global soil_matrix
soil_matrix = []
for i in range(no_of_nodes):
    l = []
    for j in range(no_of_nodes):
        l.append(init_soil)
    soil_matrix.append(l)

# defining IWD class
class iwd(object):
    # initializing the nodes and parts list and also
    # water drop's velocity and soil amount
    def __init__(self):
        self.visited_nodes = []
        self.visited_parts = []
        self.velocity = init_vel
        self.soil = init_soil
        self.tour_length = 0
        self.best_tour = []
        self.best_tour_length = float("inf")

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

    def get_last_node(self):
        if len(self.visited_nodes) > 0:
            return self.visited_nodes[-1]
        else:
            return None

    def get_velocity(self):
        return self.velocity
    def get_soil(self):
        return self.soil

    def set_velocity(self, vel):
        self.velocity = vel
    def set_soil(self, new_soil):
        self.soil = new_soil

    def get_tour_length(self):
        return self.tour_length
    def set_tour_length(self, new_length):
        self.tour_length = new_length

    def set_best_tour(self, new_tour):
        self.best_tour = new_tour
    def set_best_tour_length(self, new_length):
        self.best_tour_length = new_length

    def get_best_tour(self):
        return self.best_tour
    def get_best_tour_length(self):
        return self.best_tour_length

    def clean(self):
        self.visited_nodes = []
        self.visited_parts = []
        self.velocity = init_vel
        self.soil = init_soil
        self.tour_length = 0
# some useful functions
# getting the direction from number
def getDir(dir_no, positive):
    if positive:
        return dir_no + 1
    else:
        return -(dir_no + 1)

# from a given node obtain the row number in the soil matrix
# this can also be applied to get the column number
# in directions
# +1 -> 0, -1 -> 1, +2 -> 2, ..... 
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

# definition of the probability given in the paper
def get_probable_node(prev_node, next_node_list, visited_parts):
    e_s = 0.01 # as given in the paper
    prev_row_no = soil_row_no(prev_node)
    soil_list = []
    
    for node in next_node_list:
        row_no = soil_row_no(node)
        soil_list.append(soil_matrix[prev_row_no][row_no])
    
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
    for node, prob in zip(next_node_list, p_list):
        cumulative_prob += prob
        if x < cumulative_prob:
            break
    return node, prob, p_list 

# create the array of water drops
# first get the possible nodes list
# for that we define a function
def get_next_possible_nodes(used_parts):
    possible_nodes_list = []
    # iterating over all the parts
    for part_no in range(no_of_parts):
        if not used_parts.__contains__(part_no): #if used_parts.count(part_no) == 0:
            for dir_no in range(no_of_dirs):
                pos_dir_truth = True
                neg_dir_truth = True
                for check_part in range(no_of_parts):
                    if (not used_parts.__contains__(check_part)) and (not part_no == check_part):
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


water_drop_list = []
for i in range(no_of_iwds):
    new_water_drop = iwd()
    water_drop_list.append(new_water_drop)

# THE LOOP!
iter_no = 1
while iter_no <= iter_max:
    # some debug statements
    print "-----------------------"
    print "iter no : %d" % iter_no
    print "The initial iwds are:"

    debug_file.write("---------------\n")
    debug_file.write("iter no: %d \n" % iter_no)

    # initialize the water drops

    init_nodes = get_next_possible_nodes([])
    for water_drop in water_drop_list:
        node = choice(init_nodes)
        water_drop.add_node(node)
        print water_drop.get_nodes_list(), water_drop.get_parts_list()
    # DEBUG
    print "----"

    # the list that sees whether a water drop has completed its tour
    tour_complete = [False] * len(water_drop_list)
    all_iwds_completed_tour = False

    while not all_iwds_completed_tour:
        drop_no = 0
        for water_drop in water_drop_list:
            # getting the next feasible part
            if not tour_complete[drop_no]:
                print "---------------------"
                parts_visited = water_drop.get_parts_list()
                next_poss_nodes = get_next_possible_nodes(parts_visited)

                # criterion for checking if a tour is complete
                # check whether if no next nodes are possible
                # or all the parts are already visited
                if len(next_poss_nodes) == 0 or set(parts_visited) == parts_set:
                    tour_complete[drop_no] = True
                else:
                    present_node = water_drop.get_last_node()
                    visited_parts = water_drop.get_parts_list()
                    next_node, next_node_prob, prob_list = get_probable_node(present_node, next_poss_nodes, visited_parts)

                    

                    ### some debug statements
                    print "------"
                    print "water drop number: %d" % drop_no
                    print "presently used nodes: "
                    print water_drop.get_nodes_list()
                    print "possible next nodes: "
                    print next_poss_nodes
                    print "probabilities associated: "
                    prob_list = ["%.3f" % x for x in prob_list]
                    print prob_list
                    print "node selected: "
                    print next_node, "%.3f" % next_node_prob
                    # writing to a file
                    debug_file.write("-----\n")
                    debug_file.write("water drop number: %d \n" % drop_no)
                    debug_file.write("presently used nodes: \n")
                    debug_file.write(str(water_drop.get_nodes_list()) + "\n")
                    debug_file.write("presently used parts: \n")
                    debug_file.write(str(water_drop.get_parts_list()) + "\n")
                    debug_file.write("possible next nodes\n")
                    debug_file.write(str(next_poss_nodes) + "\n")
                    debug_file.write("probabilities associated: \n")
                    debug_file.write(str(prob_list) + "\n")
                    debug_file.write("node_selected: \n")
                    debug_file.write(str(next_node) + " " + "%.3f \n" % next_node_prob)
                    debug_file.write("\n\n" + str(soil_matrix) + "\n\n")
                    ###



                    # adding the node to the water drop nodes list
                    # updating the tour length
                    water_drop.add_node(next_node)
                    # updating the tour length
                    pres_dir = present_node[1]
                    next_dir = next_node[1]
                    if pres_dir != next_dir:
                        tour_len = water_drop.get_tour_length()
                        tour_len = tour_len + 1
                        water_drop.set_tour_length(tour_len)

                    # the soil row and column number for the next calculations
                    pres_soil_row = soil_row_no(present_node)
                    next_soil_row = soil_row_no(next_node)

                    # updating the velocity of the water drop
                    pres_vel = water_drop.get_velocity()
                    frac = a_v / (b_v + c_v * soil_matrix[pres_soil_row][next_soil_row])
                    next_vel = pres_vel + frac
                    water_drop.set_velocity(next_vel)

                    # updating the soil amounts in the matrix and the water drop
                    # calculating the cost
                    cost = 0.02
                    pres_dir = present_node[1]
                    next_dir - next_node[1]
                    if pres_dir != next_dir:
                        cost = cost * 5

                    time = cost / max(e_v, next_vel)
                    # delta soil, change in soil in the path
                    soil_added = a_s / (b_s + c_s * time)
                    print "soil, soil_added: "

                    # matrix soil update
                    pres_soil = soil_matrix[pres_soil_row][next_soil_row]
                    soil_matrix[pres_soil_row][next_soil_row] = ((1 - rho) * pres_soil) - (rho * soil_added)
                    print pres_soil, soil_added

                    # water drop soil update
                    iwd_soil = water_drop.get_soil()
                    water_drop.set_soil(iwd_soil + soil_added)

            
            drop_no = drop_no + 1

        print "---------------\n\n"
        debug_file.write("---------------\n\n\n\n")

        all_iwds_completed_tour = True
        for tour in tour_complete:
            if not tour:
                all_iwds_completed_tour = False

    # calculating the minimum tour and updating the global minimum tour
    min_tour = float("inf")
    for water_drop in water_drop_list:
        tour_len = water_drop.get_tour_length()
        if min_tour > tour_len:
            min_tour = tour_len

    # updating the soils on the min tour paths
    
    for water_drop in water_drop_list:
        tour_len = water_drop.get_tour_length()
        if min_tour == tour_len:
            water_drop_soil = water_drop.get_soil()
            print "water drop soil: %d " % water_drop_soil
            path = water_drop.get_nodes_list()
            path_len = len(path)
            start_node = path[0]
            for i in range(1, path_len):
                next_node = path[i]
                
                soil_pres_dir = soil_row_no(start_node)
                soil_next_dir = soil_row_no(next_node)
                soil_amt = soil_matrix[soil_pres_dir][soil_next_dir]
                soil_add_amt = 2 * water_drop_soil / (iter_no * (iter_no + 1))

                soil_matrix[pres_soil_row][next_soil_row] = (1 - rho) * soil_amt + rho * soil_add_amt
    



    # printing the sequence created
    debug_file.write("\n----------------------\n")
    debug_file.write("present sequences:\n")
    for i in range(len(water_drop_list)):
        water_drop = water_drop_list[i]
        sequence = water_drop.get_nodes_list()
        debug_file.write("water drop %d: \n" % i)
        debug_file.write(str(sequence) + "\n")

    # updating the best tours of water, and cleaning up the water drop
    for water_drop in water_drop_list:
        tour_len = water_drop.get_tour_length()
        best_tour_len = water_drop.get_best_tour_length()
        if tour_len < best_tour_len:
            nodes_list = water_drop.get_nodes_list()
            water_drop.set_best_tour(nodes_list)
            water_drop.set_best_tour_length(tour_len)

        water_drop.clean()

    #if iter_no == iter_max:

    print "----------------------"
    print "Best sequences obtained :"
    debug_file.write("\n\n--------------\n")
    debug_file.write("Best sequences obtained\n")
    
    for i in range(len(water_drop_list)):
        water_drop = water_drop_list[i]
        
        print "water drop: %d" % i
        debug_file.write("water drop: %d" %i)
        
        best_tour = water_drop.get_best_tour()
        best_tour_len = water_drop.get_best_tour_length()
        
        print best_tour, best_tour_len
        debug_file.write(str(best_tour))
        debug_file.write(str(best_tour_len))
        debug_file.write("\n\n")

    #print soil_matrix
    #debug_file.write(str(soil_matrix))

    iter_no = iter_no + 1
    print "-----------------------\n"
    debug_file.write("--------------------\n\n")
