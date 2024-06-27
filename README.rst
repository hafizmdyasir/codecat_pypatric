======
README
======


PyPaTriC
========

This is a helper package for writing input decks for the particle tracking code known as PaTriC (https://github.com/hafizmdyasir/PaTriC). Contents include ``classes.py``, ``keys.py``, and ``units.py``.

classes.py
----------
The ``classes.py`` file contains various classes that can be used as helpers for declaring the initial positions and velocities of particles, as well as some basic electric and magnetic field geometries. PaTriC ships with support for a few predefined options like uniformly placing particles, randomly distributing particles, among other things. These can be requested via the classes defined here.

For electric and magnetic fields, common classes like ``Static``, ``SinField``, ``GaussField``, etc. are defined here while separate files exist for specific geometries like ``Coil``, ``Dipole`` etc.


keys.py
-------
The input deck is defined using four dictionaries, namely, ``Control``, ``Particle``, ``Fields``, and ``Output``. The keys used to define them are special and are stored in this file. This minimises errors and mitigates unexpected behaviour.

units.py
--------
The ``units.py`` file contains various functions that can be used to convert between different units. Furthermore, a few helper constants to quickly convert length and time into micro, nano, and other units are also defined.


Usage
=====
You can either download the package from its GitHub repository, or using pip. The syntax for the latter is ``pip install codecat_pypatric``. For a detailed guide, refer to the documentation at https://www.github.com/hafizmdyasir/PaTriC.

Once installed, import everything from ``pypatric.keys`` and ``pypatric.classes`` to get started with the bare minimum. Creating the input deck is explained in the documentation for PaTriC. Optionally, you can import ``pypatric.units`` for some unit conversions and manipulations.