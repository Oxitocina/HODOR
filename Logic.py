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
import Logger

class Logic:
    
    def __init__(self):
        
        self.config_parameters = None
        self.licenses = None
        self.categories = None
        self.current_ranking = None
        self.current_ranking_name = None
    
    
    def setConfigParams(self, config_params):
        self.config_parameters = InputReaders.readParameters(config_params)
        
    def setLicenses(self, licenses):
        self.licenses = InputReaders.readLicenses(licenses)
        
    def setCategories(self, categories):
        self.categories = InputReaders.readCategories(categories)
    
    def openRanking(self, rank_name):
        self.current_ranking = InputReaders.readRank(rank_name)
        self.current_ranking_name = rank_name
        self.current_ranking.setConfigParams(self.config_parameters)
        self.current_ranking.setCategories(self.categories)
        self.current_ranking.setLicenses(self.licenses)
        
    def createRanking(self, rank_name, club_file):
        
        if not os.path.exists(os.path.join(os.getcwd(), rank_name)):
            os.makedirs(os.path.join(os.getcwd(), rank_name))
        else:
            return False
        club_data = InputReaders.readPrevClubFile(club_file)
        new_ranking = Rank.Rank([], club_data, self.config_parameters, self.categories, self.licenses)
        OutputWriters.writeIndRank(os.path.join(os.getcwd(), rank_name, 
                                                rank_name + '_ind.csv'), new_ranking , self.config_parameters)
        OutputWriters.writeClubRank(os.path.join(os.getcwd(), rank_name,
                                                 rank_name + '_club.csv'), new_ranking , self.config_parameters)
        self.current_ranking = new_ranking
        self.current_ranking_name = rank_name
        return True
        
    def updateRanking(self, results_file, race_name, is_international, counts_for_groups):
        
        results = InputReaders.readResults(results_file)
        
        self.current_ranking.addResults(self.checkCategoriesAge(results),race_name, is_international, counts_for_groups)
        self.orderRank()
        OutputWriters.writeIndRank(self.current_ranking_name, self.current_ranking, self.config_parameters)
        OutputWriters.writeClubRank(self.current_ranking_name, self.current_ranking, self.config_parameters)
        
    
    def addOrganizers(self, org_file, race_name):
        return
    
    def orderRank(self):
        #TODO: Ordenar el de grupos
        lic_points = {}
        category_counter = 0 #Pa'que?
        for category in self.current_ranking.data_ind:
            for person in category.keys():
                lic_points[person] = self.current_ranking.data_ind[self.current_ranking.person_categ[person]][person][5] #creates a dicctionary lic_number:points
            
            counter = 1
            while (len(lic_points)>0):
                
                next_person = max(lic_points.iteritems(), key=operator.itemgetter(1))[0]
                self.current_ranking.positions_ind[next_person] = counter
                lic_points.pop(next_person)
                counter += 1
            category_counter += 1
    
    #TODO: log output with discarded
    def checkCategoriesAge(self, results):
        
        new_results = dict(results)
        for person in dict(results):
            if results[person][2] not in self.categories.keys():
                Logger.logError(self.licenses[person].name + ' ' + self.licenses[person].surname1 +
                                ' participa en categoria desconocida: '+ results[person][2], 2)
                del new_results[person]
                continue
            category_runned = self.categories[results[person][2]]
            person_age = self.ageChecker(self.licenses[person].birthdate, self.config_parameters.fecha_actual)
            #if category_runned.gender != 'unisex' and category_runned.gender != self.licenses[person].
            if category_runned.limit_symbol == '<=':
                if int(person_age) > int(category_runned.age_limit):
                    Logger.logError(self.licenses[person].name + ' ' + self.licenses[person].surname1 +
                                    ' no cumple los requisitos de edad de la categoria.', 1)
                    del new_results[person]
                    continue
            if category_runned.limit_symbol == '>=':
                if int(person_age) < int(category_runned.age_limit):
                    Logger.logError(self.licenses[person].name + ' ' + self.licenses[person].surname1 +
                                    ' no cumple los requisitos de edad de la categoria.', 1)
                    del new_results[person]
                    continue
            min_license_required = category_runned.license_type
            person_license_type = self.licenses[person].idType
            for lic_type in self.config_parameters.licencias:
                if lic_type == person_license_type:
                    break
                if lic_type == min_license_required:
                    Logger.logError(self.licenses[person].name + ' ' + self.licenses[person].surname1 +
                                    ' no cumple los requisitos de licecia de la categoria.', 1)
                    del new_results[person]
                    continue
        return new_results


    def ageChecker(self, birthdate, actual_date):
        
        birthdate = birthdate.split('/')
        actual_date = actual_date.split('/')
        return int(actual_date[2])-int(birthdate[2])
        
            
            
        
            
            
            