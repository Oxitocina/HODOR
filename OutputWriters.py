# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:52:34 2016

@author: isidoro
"""

import csv


def writeIndRank(name, rankObj, conf):
    
    with open(name, 'wb') as rankFile:
        
        wr = csv.writer(rankFile)
        headers = conf.cabecera_ranking_individual[0:12]+conf.carreras+conf.cabecera_ranking_individual[12:]
        wr.writerow(headers)
        
        for category in rankObj.data_ind:
            data = {}
            for person in category:
                data[rankObj.positions_ind[person]] = [rankObj.positions_ind[person], person] + category[person]            
            
            for i in range(1, len(data)+1):
                wr.writerow(data[i])

def writeClubRank(name, rankObj, conf):
    
    with open(name + '.csv', 'wb') as rankFile:
        
        wr = csv.writer(rankFile)
        headers = conf.cabecera_ranking_individual[0:12]+conf.carreras+conf.cabecera_ranking_individual[12:]
        wr.writerow(headers)
        
        for division in rankObj.data_club:
            data = {}
            for club in division:
                data[rankObj.positions_club[club]] = [rankObj.positions_club[club], club] + division[club]            
            
            for i in range(1, len(data)+1):
                wr.writerow(data[i])
        
        