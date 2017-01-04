# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:42:53 2016

@author: isidoro
"""

"""This is a function for reading the Licenses from a csv files"""
import csv
import os
import Logger
import Person
import Category
import Rank
import ConfParameters

#TODO: make this into a class with at least configParameters as an attribute
#Reads the licenses file
def readLicenses(file_name):
    
    licensedPeople = {}
    with open(file_name, 'rb') as fLicenses:
        reader = csv.reader(fLicenses)
        rowNum = 0
        for row in reader:
            if rowNum != 0:
                colNum = 0
                personData = []
                person = ''
                for col in row:
                    if colNum == 1:
                        person = col
                        colNum += 1
                        continue
                    if colNum != 0 and colNum != 11:
                        personData.append(col)
                    colNum += 1
                #TODO: This last part needs to be fixed, aparently unpacking doesn't work
                licensedPeople[person]=Person.Person(*personData)
                
            rowNum += 1
                
    return licensedPeople



#Reads the configuration parameters file
def readParameters(file_name):
    
    parameters = {}
    with open(file_name, 'rb') as fParameters:
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
def readCategories(file_name):

    categories = {}
    with open (file_name, 'rb') as fCategories:
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
def readResults(file_name):
    results = {}
    with open (file_name, 'rb') as fResults:
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
                    if col == '' or col == None:
                        Logger.logError(row[1] + ' ' + row[0] + ' ha competido sin tener licencia.', 1)
                    else:
                        person = col
                if colNum in [2,3,4,6,7]:
                    result.append(col)
                colNum += 1


            results[person] = result
            rowNum += 1

    return results
        
        
#Reads the files with the organizers of each race
def readOrganizers(file_name):
    organizers = {}
    with open (file_name, 'rb') as fOrganizers:
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
    

#Reads the rank files for updating or showing them.
def readRank(name):
    data_list_ind = []
    data_list_group = []
    #with open (os.path.join(os.getcwd(), name, name + '_ind.csv'), 'rb') as fRank:
    with open (name + '_ind.csv', 'rb') as fRank:
        reader = csv.reader(fRank)
        rowNum = 0
        for row in reader:
            if rowNum == 0 or row[0] == '': #First row is just the headers
                rowNum += 1
                continue
            data_row = []
            
            for col in row:
                data_row.append(col)
            
            data_list_ind.append(data_row)
            rowNum += 1
    
    #with open (os.path.join(os.getcwd(), name, name + '_club.csv'), 'rb') as fRank:
    with open (name + '_club.csv', 'rb') as fRank:
        reader = csv.reader(fRank)
        rowNum = 0
        for row in reader:
            if rowNum == 0 or row[0] == '': #First row is just the headers
                rowNum += 1
                continue
            data_row = []
            
            for col in row:
                data_row.append(col)
            
            data_list_group.append(data_row)
            rowNum += 1
    
    result = Rank.Rank(data_list_ind, data_list_group, None, None, None)
    return result
    
def readPrevClubFile(self, file_name):
    clubs_data = []
    with open (file_name, 'rb') as fClubs:
        reader = csv.reader(fClubs)
        rowNum = 0
        for row in reader:
            if rowNum == 0 or row[0] == '': #First row is just the headers
                rowNum += 1
                continue
            
            data_row = []
            if len(row) == 2:
                data_row.append(0)
                data_row.append(row[0])
                data_row.append(row[1])
                #TODO for variance in number of races
                for i in range (0,25):
                    data_row.append(0)
            else:
                data_row.append(0)
                data_row.append(row[1])
                data_row.append(row[2])
                #TODO for variance in number of races
                for i in range (0,25):
                    data_row.append(0)
            clubs_data.append(data_row)
    return clubs_data
                
            