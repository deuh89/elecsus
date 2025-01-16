# Copyright 2017 J. Keaveney

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" 
Jones matrices for polarisers in x/y linear and l/r circular bases 

Taken from Mark Zentile's thesis, 2015

in x/y basis, x = (1,0), y = (0,1)
in l/r basis, l = (1,0), r = (0,1)

Last updated 2018-02-19 JK
"""
# py 2.7 compatibility
from __future__ import (division, print_function, absolute_import)


import numpy as np

# Horizontal polarisers (P_x)
HorizPol_xy = np.matrix([[1,0],[0,0]])
HorizPol_lr = 1./2 * np.matrix([[1,1],[1,1]])

# Vertical polarisers (P_y)
VertPol_xy = np.matrix([[0,0],[0,1]])
VertPol_lr = 1./2 * np.matrix([[1,-1],[-1,1]])

# Linear polarisers at plus 45 degrees wrt x-axis
LPol_P45_xy = 1./2 * np.matrix([[1,1],[1,1]])
LPol_P45_lr = 1./2 * np.matrix([[1,-1.j],[1.j,1]])

# Linear polarisers at minus 45 degrees wrt x-axis
LPol_M45_xy = 1./2 * np.matrix([[1,-1],[-1,1]])
LPol_M45_lr = 1./2 * np.matrix([[1,1.j],[-1.j,1]])

# Left Circular polariser (in circular basis only)
CPol_L_lr = np.matrix([[1,0],[0,0]])
CPol_R_lr = np.matrix([[0,0],[0,1]])
