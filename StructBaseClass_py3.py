#!/bin/env python
# coding=UTF-8

'''
    StructBaseClass
    ===============
        Struct base class define (in Python 3).
'''

# Import Python Lib
from abc import ABC, abstractmethod

################################################################################
# Struct Class Base (Python 3)
################################################################################

class __StructBase(ABC):

    @abstractmethod
    def Copy(self):

        raise NotImplementedError


    @abstractmethod
    def Dumps(self):

        raise NotImplementedError


    def Dump(self, dumpFileName, fileMode = 'w'):

        with open(dumpFileName, fileMode) as fo:
            fo.write(self.Dumps())