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
