# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:52:34 2016

@author: isidoro
"""

import csv
import os

def writeIndRank(name, rank_obj, conf):
    
    with open(os.path.join(os.getcwd(), name, name + '_ind.csv'), 'wb') as rank_file:
        
        wr = csv.writer(rank_file)
        headers = conf.cabecera_ranking_individual[0:12] + conf.carreras + conf.cabecera_ranking_individual[12:]
        wr.writerow(headers)
        
        for category in rank_obj.data_ind:
            data = {}
            for person in category:
                data[rank_obj.positions_ind[person]] = [rank_obj.positions_ind[person], person] + category[person]            
            
            for i in range(1, len(data) + 1):
                wr.writerow(data[i])

def writeClubRank(name, rank_obj, conf):
    
    with open(os.path.join(os.getcwd(), name, name + '_club.csv'), 'wb') as rank_file:
        
        wr = csv.writer(rank_file)
        headers = conf.cabecera_ranking_clubes[0:5] + conf.carreras
        wr.writerow(headers)
        
        for division in rank_obj.data_club:
            data = {}
            for club in division:
                data[rank_obj.positions_club[club]] = [rank_obj.positions_club[club], club] + division[club]            
            
            for i in range(1, len(data)):
                wr.writerow(data[i])
                

        
        