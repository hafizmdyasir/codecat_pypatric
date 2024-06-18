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




# INTEGRATORS
BORIS = 0
VAY = 1
HIGUERA_CARY = 2

# DIRECTIONS
X = 1
Y = 2
Z = 3


def validate_deck(control: dict, particle: dict, fields:dict, output: dict):
    '''
    Pass the dicts you have declared to this function to ensure all required parameters are provided.
    '''
    # Step 1: Validate control dict. All keys are required.
    given_keys = control.keys()
    required_keys = set([TIME_STEP, NUM_ITERS, INTEGRATOR, READOUT_FREQ])
    missing_keys = required_keys - set(given_keys)
    if len(missing_keys) > 0:
        raise KeyError(f'Missing control keys: {missing_keys}')
    
    # Step 2: Validate particle dict. Mass and Charge are necessary, Positions and velocity can be provided in one of two ways.
    given_keys = particle.keys()
    if (MASS not in given_keys):
        raise KeyError(f'Missing particle key: MASS')
    
    if (CHARGE not in given_keys):
        raise KeyError(f'Missing particle key: CHARGE')
    
    if INITIAL_POSITION not in given_keys:
        raise KeyError(f'Missing particle keys related to initial position.')
    
    if INITIAL_VELOCITY not in given_keys:
        raise KeyError(f'Missing particle keys related to initial velocity.')
    
    # Step 3: Validate field dict.
    given_keys = fields.keys()
    if E_FIELD not in given_keys:
        raise KeyError(f'Missing field keys related to electric field.')
    
    if B_FIELD not in given_keys:
        raise KeyError(f'Missing field keys related to magnetic field.')
    

    # Step 4: Validate output dict.
    if FILENAME not in output.keys():
        raise KeyError(f'Missing output key: FILENAME')