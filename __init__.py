#!/bin/env python
# coding=UTF-8

'''
DESCRIPTION

    PDBTools

    Collection of modules for PDB file parsing, linear algebra calculations and
    structure modify.
    See README file for full description and examples.

VERSION

    2.10.0

LATEST UPDATE

    2018.11.23

'''

# Six
import six

# Parser API
from .PDBParser import Load

# Math Util
from .MathUtil import Dis, Norm, CalcVectorAngle, CalcRotationMatrix, \
    CalcRotationMatrixByTwoVector, CalcDihedralAngle, CalcSuperimposeRotationMatrix

# Struct Class
if six.PY2:
    from .StructClass_py2 import C_ProteinStruct, C_ChainStruct, C_ResidueStruct, C_AtomStruct
else:
    from .StructClass import C_ProteinStruct, C_ChainStruct, C_ResidueStruct, C_AtomStruct

# Const
from .StructConst import RESIDUE_NAME_THREE_TO_ONE_DICT, RESIDUE_NAME_ONE_TO_THREE_DICT

# Struct Util
from .StructUtil import Dumpl