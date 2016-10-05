# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:42:53 2016

@author: isidoro
"""

"""This is a function for reading the Licenses from a csv files"""
import csv
import Person
import ConfParameters

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
                if col == None or col == '' or col[0] == '#':
                    continue #Every row starting with that symbol is considered a comment
                if col == "str" or col == "int" or col == "float" or col == "date":
                    continue #No need to know the type of the parameter here
                if colNum == 0:
                    codParameter = col
                else:
                    #if colNum % 2 == 0:#non-even columns especify the type of the previous data, not usefull in this module
                        valuesParameter.append(col)
                colNum += 1
            parameters[codParameter]=valuesParameter
            rowNum += 1
    clase = ConfParameters.ConfParameters(parameters)
    return clase
            
            