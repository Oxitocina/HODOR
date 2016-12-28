# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:20:04 2016

@author: isidoro
"""

import numpy
import operator

class Rank:
    
    def __init__(self, data_list_ind, data_list_club, configuration, categories, licenses):
        
        self.positions_ind = {}
        self.data_ind = []
        self.dictCateg = {} #correlates the category name with the index of the lists (positions and data) where that category participants are
        self.person_categ = {} #correlates person with the index of its category
        index_categ = 0
        for person in data_list_ind:
            self.positions_ind[person[1]] = person[0]
            if person[2] not in self.dictCateg.keys():
                self.dictCateg[person[2]] = index_categ
                self.data_ind.append({})
                index_categ += 1
            self.person_categ[person[1]] = self.dictCateg[person[2]]
            self.data_ind[self.dictCateg[person[2]]][person[1]] = person[2:]
         
        self.positions_club = {}
        self.data_club = [[],[],[]]
        self.club_division = {}
        for club in data_list_club:
            self.positions_club[club[1]] = club[0]
            self.data_club[club[2]-1][club[1]] = club[2:]
            self.club_division[club[1]] = club[2]
        
        self.configuration = configuration
        self.categories = categories
        self.licenses = licenses
    
    
    def setConfigParams(self, configParams):
        self.configuration = configParams
        
    def setLicenses(self, licenses):
        self.licenses = licenses
        
    def setCategories(self, categories):
        self.categories
    #What if this class contains the pair Individual-Groups
    def addResults(self, results, race_name, is_international, counts_for_groups):
                
        people_ordered_by_time = self.orderListByTime(results)
        
        dict_people_points = self.calculatePoints(people_ordered_by_time, results, is_international)
        
        self.storeClubPoints(dict_people_points)
        
        dict_people_valid_individual = self.checkCategories(dict_people_points, results)
        
        self.storeIndPoints(dict_people_valid_individual)
        
    
    def orderByCategory(self, results):  
        list_people_by_categories = []
        categories_index = {}
        index = 0;
        for person in results.keys():
            if results[person][2] in categories_index.keys():
                list_people_by_categories[categories_index[results[person][2]]].append(person)
            else:
                categories_index[results[person][2]] = index
                list_people_by_categories.append([person])
                index += 1
        
        return list_people_by_categories
                
    
    
    def orderListByTime(self, results):
        #Returns a list of lists that contains each participant that deserves points in time order inside each category
        list_people_by_categories = self.orderByCategory(results)
        ordered_people_by_time = []
        index = 0
        for category in list_people_by_categories:
            ordered_people_by_time.append([])
            for person in category:
                if ordered_people_by_time[index] == []:
                    ordered_people_by_time.append(person)
                else:
                    if results[person][3] != 0 or results[person][4] == 1:
                        continue
                    if results[person][4] != 0:
                        ordered_people_by_time[index].append(person)
                        continue
                    index2 = 0
                    for person2 in ordered_people_by_time[index]:
                        if results[person][0] < results[person2][0] or results[person2][4] != 0:
                            ordered_people_by_time[index].insert(index2, person)
                        index2 += 1
            index += 1
        return ordered_people_by_time
                    
    def calculatePoints(self, people_ordered, results, is_international):
        #Returns a dictionary that contains the carrelation between persons and the points obtained.
        dict_person_points = {}
        for category in people_ordered:
            index = 0
            winner = ""
            winner_points = 0
            if is_international:
                winner_points = self.configuration.puntos_ganador_inter
            else:
                winner_points = self.configuration.puntos_ganador_nac
            if self.categories[results[category[0]][2]].is_elite:
                winner_points = winner_points * self.configuration.coef_elite
            for person in category:
                if results[person][4] != 0:
                    dict_person_points[person] = self.configuration.puntos_penalizacion
                elif index == 0:
                    dict_person_points[person] = winner_points
                    winner = person
                else:
                    dict_person_points[person] = results[winner][0]/results[person][0] * winner_points
                
                index += 1
        return dict_person_points
        
    def checkCategories(self, dict_person_points, dict_results):
        #Checks if the category showed in the ranking is the same as the one they run in a race and
        #if they haven't run in any races, sets their category as the one in this race
        dict_checked_categories = {}
        for person in dict_person_points.keys():
            actual_category = ""
            race_category = dict_results[person][1]
            for category in self.data_ind:
                if person in category.keys():
                    actual_category = category[person][0]
                    break
            if actual_category == "":
                self.includePerson(person, race_category)
                dict_checked_categories[person] = dict_person_points[person]
            else:
                if actual_category == race_category:
                    dict_checked_categories[person] = dict_person_points[person]
            
        return dict_checked_categories
        
    def storeIndPoints(self, dict_checked_categories, race_name):
        
        for person in dict_checked_categories.keys():
            self.data_ind[self.person_categ[person]][person][5] += dict_checked_categories[person]
            self.data_ind[self.person_categ[person]][person][6] += 1
            index = 10 #This is the index on the data for the first race
            for carrera in self.configuration.carreras:
                if carrera == race_name:
                    break
                index += 1
            self.data_ind[self.person_categ[person]][person][index] = dict_checked_categories[person]
            #TODO: Mirar lo de el parametro continuo/final
            self.data_ind[self.person_categ[person]][person][7] = self.calculateM1(person)
            self.data_ind[self.person_categ[person]][person][8] = self.calculateM2(person)
            self.data_ind[self.person_categ[person]][person][9] = self.calculateM3(person)
                
                
    def includePerson(self, lic_number, category):
        self.positions_ind[lic_number] = 0
        self.person_categ[lic_number] = self.dictCateg[category]
        person_data = []
        person_data.append(category)
        person_data.append(self.licenses[lic_number][1])
        person_data.append(self.licenses[lic_number][2])
        person_data.append(self.licenses[lic_number][3])
        person_data.append(self.licenses[lic_number][4])
        #TODO: Make valid if the number of races changes
        for i in range(0,len(self.configuration.carreras)):
            person_data.append(0)
        person_data.append(self.licenses[lic_number][1])
        person_data.append(self.licenses[lic_number][2])
        person_data.append(self.licenses[lic_number][3])
        self.data_ind[self.dictCateg[category]][lic_number] = person_data
        
    
    def calculateM1(self, person):
        max_scores = []
        for i in range(0, self.configuration.num_carreras_media):
            max_scores.append(0)
        #TODO: FIx for variable number of races
        for i in range(10, len(self.configuration.carreras) + 10):
            if self.data_ind[self.person_categ[person]][person][i] > min(max_scores):
                max_scores[max_scores.index(min(max_scores))] = self.data_ind[self.person_categ[person]][person][i]
        return numpy.mean(max_scores)
        
    def calculateM2(self, person):
        scores = []
        #TODO: FIx for variable number of races
        for i in range(10, len(self.configuration.carreras) + 10):
            if self.data_ind[self.person_categ[person]][person][i] > self.configuration.putos_penalizacion:
                scores.append(self.data_ind[self.person_categ[person]][person][i])
        return numpy.mean(scores)
        
    def calculateM3(self, person):
        scores = []
        #TODO: FIx for variable number of races
        for i in range(10, len(self.configuration.carreras) + 10):
            if self.data_ind[self.person_categ[person]][person][i] > 0:
                scores.append(self.data_ind[self.person_categ[person]][person][i])
        return numpy.mean(scores)
    
    def storeClubPoints(self, dict_person_points, race_name, results):
        people_by_categories = self.orderByCategory(results)
        new_points = dict_person_points
        for category in people_by_categories:
            
            category_name = results[category[0]][2]
            
            for person in category:
                new_points[person] = new_points[person] * self.categories[category_name].coef_club
            
            dict_people_by_club = self.orderByClub(category)
            
            for club in dict_people_by_club.keys():
                n_people_counts = self.configuration.num_max_corredores[self.configuration.tipos_categoria_ranking_clubes.index(self.categories[category_name].category_type_club)]
                people_points_club = {}
                for person in dict_people_by_club[club]:
                    people_points_club[person] = new_points[person]
                people_that_counts = []
                while len(people_that_counts) < n_people_counts:
                    people_that_counts.append(max(people_points_club.iteritems(), key=operator.itemgetter(1))[0])
                    #TODO: si hay menos personas q n_people_counts
                for person in people_that_counts:
                    self.data_club[self.club_division[club]][club][1] += new_points[person]
                    index = 3 + self.configuration.carreras.index(race_name)
                    self.data_club[self.club_division[club]][club][index] += new_points[person]
                self.data_club[self.club_division[club]][club][2] = self.calculateMClub(club)
            
    def orderByClub(self, list_of_people):
        
        dict_people_by_club = {}
        for person in list_of_people:
            if self.licenses[person].club in dict_people_by_club.keys():
                dict_people_by_club[self.licenses[person].club].append(person)
            else:
                dict_people_by_club[self.licenses[person].club] = [person]
        
        return dict_people_by_club
            
    def calculateMClub(self, club):
        scores = []
        #TODO: FIx for variable number of races
        for i in range(3,len(self.configuration.carreras) + 3):
            if self.data_club[self.club_division[club]][club][i] > 0:
                scores.append(self.data_club[self.club_division[club]][club][i])
        return numpy.mean(scores)
        
        
    def returnData(self):#usar yield para devolver linea por linea?
        return           
