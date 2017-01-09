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
def readLicenses(file_path):
    
    licensedPeople = {}
    with open(file_path, 'rb') as fLicenses:
        reader = csv.reader(fLicenses)
        row_num = 0
        for row in reader:
            if row_num != 0:
                col_num = 0
                personData = []
                person = ''
                for col in row:
                    if col_num == 1:
                        person = col
                        personData.append(col.strip())
                        col_num += 1
                        continue
                    if col_num != 0 and col_num != 11:
                        personData.append(col.strip())
                    col_num += 1
                #TODO: This last part needs to be fixed, aparently unpacking doesn't work
                licensedPeople[person]=Person.Person(*personData)
                
            row_num += 1
                
    return licensedPeople



#Reads the configuration parameters file
def readParameters(file_name):
    
    parameters = {}
    with open(file_name, 'rb') as f_parameters:
        reader = csv.reader(f_parameters)
        for row in reader:
            col_num = 0
            cod_parameter=""
            values_parameter=[]
            for col in row:
                if col == None or col == '' or col[0] == '#':
                    continue #Every row starting with that symbol is considered a comment
                if col == "str" or col == "int" or col == "float" or col == "date":
                    continue #No need to know the type of the parameter here
                if col_num == 0:
                    cod_parameter = col.strip()
                else:
                    #if col_num % 2 == 0:#non-even columns especify the type of the previous data, not usefull in this module
                        values_parameter.append(col.strip())
                col_num += 1
            parameters[cod_parameter]=values_parameter
    conf_obj = ConfParameters.ConfParameters(parameters)
    return conf_obj
    



#Reads the categories file
def readCategories(file_name):

    categories = {}
    with open (file_name, 'rb') as fCategories:
        reader = csv.reader(fCategories)
        row_num = 0
        for row in reader:
            if row_num == 0: #First row is just the headers
                row_num += 1
                continue
            category_data = []
            
            for col in row:
                
                category_data.append(col.strip())
            
            row_num += 1   
            category = Category.Category(category_data)
            categories[category.name] = category
        
    return categories
            

#Reads the files with the results of each race.            
def readResults(file_name):
    
    results = {}
    with open (file_name, 'rb') as f_results:
        reader = csv.reader(f_results)
        row_num = 0
        
        for row in reader:
            if row_num == 0: #First row is just the headers
                row_num += 1
                continue
            if row[5] == '' or row[5] == None:
                Logger.logError(row[1] + ' ' + row[0] + ' ha competido sin tener licencia.', 1)
                row_num += 1
                continue
            result = []
            person = ""
            col_num = 0
            
            for col in row:
                if col_num == 5:
                    person = col.strip()
                if col_num in [2,3,4,6,7]:
                    result.append(col.strip())
                col_num += 1


            results[person] = result
            row_num += 1

    return results
        
        
#Reads the files with the organizers of each race
def readOrganizers(file_name):
    organizers = {}
    with open (file_name, 'rb') as fOrganizers:
        reader = csv.reader(fOrganizers)
        row_num = 0
        for row in reader:
            if row_num == 0: #First row is just the headers
                row_num += 1
                continue
            orgType = ""
            id = ""
            col_num = 0
            
            for col in row:
                
                if col_num == 0 and col != "":
                    id = col.strip()
                if col_num == 1 and id == "":
                    id = col.strip()
                if col_num == 2:
                    orgType = col.strip()
                col_num += 1
            organizers[id] = orgType
            row_num += 1
            
    return organizers
    

#Reads the rank files for updating or showing them.
def readRank(name):
    
    data_list_ind = []
    data_list_group = []
    
    with open (os.path.join(os.getcwd(), name, name + '_ind.csv'), 'rb') as f_rank:
        reader = csv.reader(f_rank)
        row_num = 0
        for row in reader:
            if row_num == 0 or row[0] == '': #First row is just the headers
                row_num += 1
                continue
            data_row = []
            
            for col in row:
                data_row.append(col.strip())
            
            data_list_ind.append(data_row)
            row_num += 1
    
    with open (os.path.join(os.getcwd(), name, name + '_club.csv'), 'rb') as f_rank:
        reader = csv.reader(f_rank)
        row_num = 0
        for row in reader:
            if row_num == 0 or row[0] == '': #First row is just the headers
                row_num += 1
                continue
            data_row = []
            
            for col in row:
                data_row.append(col.strip())
            
            data_list_group.append(data_row)
            row_num += 1
    
    result = Rank.Rank(data_list_ind, data_list_group, None, None, None)
    return result
    
def readPrevClubFile(file_name):
    clubs_data = []
    with open (file_name, 'rb') as fClubs:
        reader = csv.reader(fClubs)
        row_num = 0
        for row in reader:
            if row_num == 0 or row[0] == '': #First row is just the headers
                row_num += 1
                continue
            
            data_row = []
            if len(row) == 2:
                data_row.append(0)
                data_row.append(row[0].strip())
                data_row.append(row[1].strip())
                #TODO for variance in number of races
                for i in range (0,25):
                    data_row.append(0)
            else:
                data_row.append(0)
                data_row.append(row[1].strip())
                data_row.append(row[2].strip())
                #TODO for variance in number of races
                for i in range (0,25):
                    data_row.append(0)
            clubs_data.append(data_row)
    return clubs_data
                
            