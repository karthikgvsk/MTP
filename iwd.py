# INTELLIGENT WATER DROPS ALGORITHM
import random, math

# the example Disassembly Matrix
DM = [
     [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0], 
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
     [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

## parameters
# static parameters
no_of_parts = 4
no_of_nodes = 6 * 4
no_of_iwds = 4 # equal to number of parts

# parameters for velocity updating
a_v = 1000
b_v = 0.01
c_v = 1

# parameters for soil updating 
a_s = 1000
b_s = 0.01
c_s = 1

# initial velocity
global init_vel = 100
init_soil = 1000 # initialize the soil on every path by this amount

# best tour
T_b = []
len_best_tour = inf#len(T_b)

# maximum number of iterations
iter_max = 100

# defining IWD class
class iwd(object):
    def __init__(self):
        this.visited_nodes = []
        this.visited_parts = []
        this.velocity = init_vel 
