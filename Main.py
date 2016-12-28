# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:34:26 2016

@author: isidoro
"""
import InputReaders
class Main:
    
    def __init__(self,configFile):
        
        self.configParameters = InputReaders.readParameters(configFile)