'''
DECK TOOLS.py
=============
Created: 03.07.2024

Copyright
Mohammad Yasir
Research Scholar, IIT-D

All rights reserved. No part of this code may be used, modified, shared, or reproduced in any form without express permission of its author.

DESCRIPTION
-----------
Tools to help write the deck
'''


from inspect import signature
from typing import Tuple

from electric import *
from magnetic import *
from classes import *
from keys import *


Control = {}
Particle = {}
Fields = {}
Output = {}


def createControl(
        timeStep: float, numiterations: int,
        integrator: int, readoutFreq: int):
    '''
    Create the control dict.
    Parameters:
        timeStep : float The time step dt.
        numiterations : int The number of iterations to run the program for.
        integrator : int The numerical integration method to use. Must be one of BORIS, VAY, or HIGUERA_CARY.
        readoutFreq : int The frequency at which to show a small output message. Zero or negative to turn off.
    '''

    # Validate inputs.
    if timeStep <= 0:
        raise ValueError('Time step must be a positive float.')
    if numiterations <= 0:
        raise ValueError('Number of iterations must be a positive integer.')
    if integrator not in [BORIS, VAY, HIGUERA_CARY]:
        raise ValueError(f'Invalid integrator. Must be one of BORIS, VAY, or HIGUERA_CARY.')

    global Control
    Control[TIME_STEP] = timeStep
    Control[NUM_ITERS] = numiterations
    Control[INTEGRATOR] = integrator
    Control[READOUT_FREQ] = readoutFreq



def createParticles(
        mass: float, charge: float, particleCount: int,
        initialPosition: Tuple,
        initialVelocity: Tuple):
    '''
    Create the particle dict.
    Parameters:
        mass : float The mass of the particle in multiple of electronic mass.
        charge : float The charge of the particle in multiples of fundamental charge.
        initialPosition : Tuple The initial position(s) of the particle(s)
        initialVelocity : Tuple The initial velocity(s) of the particle(s)
    '''

    # Validate inputs.
    if mass <= 0:
        raise ValueError('Mass must be a positive float.')
    if particleCount <= 0:
        raise ValueError('Particle count must be a positive integer.')
    if len(initialPosition) < 1:
        raise ValueError('Initial position must be a tuple with at least one element.')
    if len(initialVelocity) < 1:
        raise ValueError('Initial velocity must be a tuple with at least one element.')
    
    # Ensure that the initial positions provided are in correct format
    for r in initialPosition:
        if type(r) not in (Static, Uniform, Random):
            raise ValueError('Initial positions must be Static, Uniform, or Random objects.')
    
    for v in initialVelocity:
        if type(v) not in (Static, Uniform, Maxwellian):
            raise ValueError('Initial velocities must be Static, Uniform, or Maxwellian objects.')
        

    global Particle
    Particle[MASS] = mass
    Particle[CHARGE] = charge
    Particle[PARTICLE_COUNT] = particleCount
    Particle[INITIAL_POSITION] = initialPosition
    Particle[INITIAL_VELOCITY] = initialVelocity


def createFields(
        electricFields: Tuple | callable,
        magneticFields: Tuple | callable):
    '''
    Create the fields dict. 
    Parameters:
        electricFields : Tuple | callable The electric field(s). The total field 
        magneticFields : Tuple | callable The magnetic field(s)
    '''

    supportedEleFields = (Static, SinField, GaussField, PointCharge, ElectricDipole)
    supportedMagFields = (Static, SinField, GaussField, Wire, Coil)

    # Validate inputs.
    if isinstance(electricFields, Tuple):
        for e in electricFields:
            if type(e) not in supportedEleFields:
                raise ValueError(f'Electric fields must be one of {supportedEleFields}.')
    else:
        if len(signature(electricFields).parameters) != 4:
            raise ValueError('Electric field as a function must take four parameters: x, y, z, and t.')
    
    if isinstance(magneticFields, Tuple):
        for b in magneticFields:
            if type(b) not in supportedMagFields:
                raise ValueError(f'Magnetic fields must be one of {supportedMagFields}.')
    else:
        if len(signature(magneticFields).parameters) != 4:
            raise ValueError('Magnetic field as a function must take four parameters: x, y, z, and t.')
        
    global Fields
    Fields[E_FIELD] = electricFields
    Fields[B_FIELD] = magneticFields


def createOutput(
        fileName: str, filePath: str,
        fileHeaders: Tuple[str, ...], dumpInfoFile: bool, dumpVariables: Tuple[str, ...]):
    '''
    Create the output dict.
    Parameters:
        fileName : str The name of the output file.
        filePath : str The path to the output file.
        fileHeaders : Tuple[str,...] The headers to include in the info file.
        dumpInfoFile : bool Whether to dump info file.
        dumpVariables : Tuple[str,...] The variables to dump in the output file.
    '''

    # Validate inputs.
    supportedDumpVariables = (
        POS_X, POS_Y, POS_Z, 
        VEL_X, VEL_Y, VEL_Z, 
        E_FIELD_X, E_FIELD_Y, E_FIELD_Z,
        B_FIELD_X, B_FIELD_Y, B_FIELD_Z,
        GAMMA)

    if not fileName:
        raise ValueError('Output file name cannot be empty.')
    for v in dumpVariables:
        if v not in supportedDumpVariables:
            raise ValueError(f'Invalid dump variable. Must be one of {supportedDumpVariables}.')

    global Output
    Output[FILENAME] = fileName
    Output[FILEPATH] = filePath
    Output[FILE_HEADER] = fileHeaders
    Output[DUMP_INFO_FILE] = dumpInfoFile
    Output[DUMP_VARIABLES] = dumpVariables