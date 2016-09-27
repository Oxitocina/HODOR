# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:42:53 2016

@author: isidoro
"""

"""This is a function for reading the Licenses from a csv files"""
import csv
import Person

def readLicenses(file):
    
    licensedPeople = {}
    with open(file, 'rb') as fLicenses:
        reader = csv.reader(fLicenses)
        rowNum = 0
        for row in reader:
            if rowNum != 0:
                colNum = 0
                personData = []
                for col in row:
                    if colNum != 0 and colNum != 11:
                        personData.append(col)
                    colNum += 1
                """This last part needs to be fixed, aparently unpacking doesn't work"""
                licensedPeople[personData[0]]=Person.Person(*personData)
                
            rowNum += 1
                
    return licensedPeople


def readParameters(file):
    
    parameters = {}
    with open(file, 'rb') as fParameters:
        reader = csv.reader(fParameters)
        rowNum = 0
        for row in reader:
            colNum = 0
            codParameter=""
            valuesParameter=[]
            for col in row:
                if colNum == 0:
                    codParameter = col
                else:
                    valuesParameter.append(col)
                colNum += 1
            parameters[codParameter]=valuesParameter
            rowNum += 1
            
    return parameters
            
            