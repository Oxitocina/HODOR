# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:34:26 2016

@author: isidoro
"""

import operator
import os

import InputReaders
import OutputWriters
import Rank

class Logic:
    
    def __init__(self):
        
        self.configParameters = None
        self.licenses = None
        self.categories = None
        self.current_ranking = None
    
    
    def setConfigParams(self, configParams):
        self.configParameters = InputReaders.readParameters(configParams)
        
    def setLicenses(self, licenses):
        self.licenses = InputReaders.readLicenses(licenses)
        
    def setCategories(self, categories):
        self.categories = InputReaders.readCategories(categories)
    
    def openRanking(self, rankName):
        #TODO: do readRanks, set the parameters needed...
        self.current_ranking = InputReaders.readRank(rankName)
        self.current_ranking.setConfigParams(self.configParameters)
        self.current_ranking.setCategories(self.categories)
        self.current_ranking.setLicenses(self.licenses)
        
    def createRanking(self, rankName, clubFile):
        
        if not os.path.exists(os.path.join(os.getcwd(), rankName)):
            os.makedirs(os.path.join(os.getcwd(), rankName))
        else:
            return False
        club_data = InputReaders.readPrevClubFile(clubFile)
        newRanking = Rank.Rank([], club_data, self.configParameters, self.categories, self.licenses)
        OutputWriters.writeIndRank(os.path.join(os.getcwd(), rankName, rankName + '_ind.csv'), newRanking , self.configParameters)
        OutputWriters.writeClubRank(os.path.join(os.getcwd(), rankName, rankName + '_club.csv'), newRanking , self.configParameters)
        self.current_ranking = newRanking
        return True
        
    def updateIndRanking(self, results_file_name, race_name, is_international, counts_for_groups):
        
        results = InputReaders.readResults(results_file_name)
        
        self.current_ranking.addResults(self.checkCategoriesAge(results),race_name, is_international, counts_for_groups)
        self.orderRank()
        OutputWriters.writeIndRank(self.current_ranking)
        OutputWriters.writeClubRank(self.current_ranking)
        
    
    def addOrganizers(self, org_file_name, race_name):
        return
    
    def orderRank(self):
        #TODO: Ordenar el de grupos
        lic_points = {}
        category_counter = 0 #Pa'que?
        for category in self.current_ranking.data_ind:
            for person in category:
                lic_points[person] = self.current_ranking.data_ind[category].get(person)[5] #creates a dicctionary lic_number:points
            
            counter = 1
            while (len(lic_points)>0):
                
                next_person = max(lic_points.iteritems(), key=operator.itemgetter(1))[0]
                self.current_ranking.positions_ind[next_person] = counter
                lic_points.pop(next_person)
                counter += 1
            category_counter += 1
    
    #TODO: log output with discarded
    def checkCategoriesAge(self, results):
        newResults = dict(results)
        for person in newResults:
            
            category_runned = self.categories[results[person][2]]
            person_age = self.ageChecker(self.licenses[person].birthdate, self.configParameters.fecha_actual)
            #if category_runned.gender != 'unisex' and category_runned.gender != self.licenses[person].
            if category_runned.limit_symbol == '<=':
                if person_age > category_runned.age_limit:
                    del newResults[person]
            if category_runned.limit_symbol == '>=':
                if person_age < category_runned.age_limit:
                    del newResults[person]
            min_license_required = category_runned.license_type
            person_license_type = self.licenses[person].idType
            for licType in self.configParameters.licencias:
                if licType == person_license_type:
                    break
                if licType == min_license_required:
                    del newResults[person]
        return newResults

    def ageChecker(self, birthdate, actualdate):
        
        birthdate = birthdate.split('/')
        actualdate = actualdate.split('/')
        return int(actualdate[2])-int(birthdate[2])
        
            
            
        
            
            
            