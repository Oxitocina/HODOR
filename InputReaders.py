# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:42:53 2016

@author: isidoro
"""

"""This is a function for reading the Licenses from a csv files"""
import csv
import Person
import Category
import ConfParameters


#Reads the licenses file
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



#Reads the configuration parameters file
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
    



#Reads the categories file
def readCategories(file):

    categories = {}
    with open (file, 'rb') as fCategories:
        reader = csv.reader(fCategories)
        rowNum = 0
        for row in reader:
            if rowNum == 0: #First row is just the headers
                rowNum += 1
                continue
            category_data = []
            
            for col in row:
                
                category_data.append(col)
            
            rowNum += 1   
            category = Category.Category(category_data)
            categories[category.name] = category
        
    return categories
            
            


#Reads the files with the results of each race.            
def readResults(file):
    results = {}
    with open (file, 'rb') as fResults:
        reader = csv.reader(fResults)
        rowNum = 0
        for row in reader:
            if rowNum == 0: #First row is just the headers
                rowNum += 1
                continue
            result = []
            person = ""
            colNum = 0
            
            for col in row:
                
                if colNum == 5:
                    person = col
                if colNum in [2,4,6,7]:
                    result.append(col)
                colNum += 1


            results[person] = result
            rowNum += 1

    return results
        
        
#Reads the files with the organizers of each race
def readOrganizers(file):
    organizers = {}
    with open (file, 'rb') as fOrganizers:
        reader = csv.reader(fOrganizers)
        rowNum = 0
        for row in reader:
            if rowNum == 0: #First row is just the headers
                rowNum += 1
                continue
            orgType = ""
            id = ""
            colNum = 0
            
            for col in row:
                
                if colNum == 0 and col != "":
                    id = col
                if colNum == 1 and id == "":
                    id = col
                if colNum == 2:
                    orgType = col
                colNum += 1
            organizers[id] = orgType
            rowNum += 1
            
    return organizers