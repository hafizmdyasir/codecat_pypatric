======
README
======


PyPaTriC
========

This is a helper package for writing input decks for the particle tracking code known as PaTriC. Contents include ``classes.py``, ``keys.py``, and ``units.py``.

``classes.py``
--------------
The ``classes.py`` file contains various classes that can be used as helpers for declaring the initial positions and velocities of particles, as well as inbuilt electric and magnetic field geometries.

``keys.py``
-----------
You will find all the keys required to declare the input deck in this file.

``units.py``
------------
This file includes helper constants and functions for unit conversions.


Usage
=====
You can either download the package from its GitHub repository, or using pip. The syntax for the latter is ``pip install codecat_pypatric``.

Once installed, import everything from ``pypatric.keys`` and ``pypatric.classes`` to get started with the bare minimum. Creating the input deck is explained in the documentation for PaTriC. Optionally, you can import ``pypatric.units`` for some unit conversions and manipulations.