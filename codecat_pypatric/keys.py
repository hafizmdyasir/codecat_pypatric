'''
KEYS.py
=======
Created: 16.05.2024

Copyright
Mohammad Yasir
Research Scholar, IIT-D

All rights reserved. No part of this code may be used, modified, shared, or reproduced in any form without express permission of its author.

DESCRIPTION
-----------
Constant keys that can be used to define the config file for PaTriC. Also defines functions that can be used to validate the deck.
'''

# CONTROL KEYS
TIME_STEP = 'dt'
NUM_ITERS = 'num_iters'
INTEGRATOR = 'integerator'
READOUT_FREQ = 'readout_freq'


# PARTICLE KEYS
MASS = 'mass'
CHARGE = 'charge'
PARTICLE_COUNT = 'particle_count'
INITIAL_POSITION = 'initial_position'
INITIAL_VELOCITY = 'initial_velocity'


# FIELDS KEYS
E_FIELD = 'e_field'
B_FIELD = 'b_field'


#OUTPUT KEYS
FILENAME = 'f_name'
FILEPATH = 'f_path'
FILE_HEADER = 'f_header'
DUMP_VARIABLES = 'dump_variables'

# VARIABLE NAMES FOR DUMPING
POS_X = 'position_x'
POS_Y = 'position_y'
POS_Z = 'position_z'

VEL_X = 'velocity_x'
VEL_Y = 'velocity_y'
VEL_Z = 'velocity_z'

GAMMA = 'gamma'
# E_FIELD and B_FIELD are also accepted as dump variables.



# INTEGRATORS
BORIS = 0
VAY = 1
HIGUERA_CARY = 2

# DIRECTIONS
X = 1
Y = 2
Z = 3