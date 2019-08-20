#!/bin/env python
# coding=UTF-8

'''
    StructBaseInterface
    ===================
        Class __StructBaseInterface define.
'''

# Import Python Lib
import sys

################################################################################
# Struct Base Class
################################################################################

if sys.version_info[0] == 3:

    from abc import ABC, abstractmethod

    class __StructBaseInterface(ABC):

        @abstractmethod
        def Copy(self):

            raise NotImplementedError


        @abstractmethod
        def Dumps(self):

            raise NotImplementedError


        def Dump(self, dumpFilePath, fileMode = 'w'):

            with open(dumpFilePath, fileMode) as fo:
                fo.write(self.Dumps())

            return self

else:

    from abc import ABCMeta, abstractmethod

    class __StructBaseInterface(object):

        __metaclass__ = ABCMeta

        @abstractmethod
        def Copy(self):

            raise NotImplementedError


        @abstractmethod
        def Dumps(self):

            raise NotImplementedError


        def Dump(self, dumpFilePath, fileMode = 'w'):

            with open(dumpFilePath, fileMode) as fo:
                fo.write(self.Dumps())

            return self