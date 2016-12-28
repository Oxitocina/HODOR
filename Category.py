# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:35:23 2016

@author: isidoro
"""

class Category:
    
    def __init__(self, parameters):
        self.name = parameters[0]
        self.gender = parameters[1]
        self.closed_group = False
        if parameters[2] == "SI":
            self.closed_group = True
        self.closed_group_file = parameters[3]
        self.limit_symbol = parameters[4]
        self.age_limit = parameters[5]
        if self.age_limit != "":
            self.age_limit = int(self.age_limit)
        self.coef_club = float(parameters[6])
        self.license_type = parameters[7]
        self.other_categories = False
        if parameters[8] == "SI":
            self.other_categories = True
        self.category_type_club = parameters[9]
        self.is_elite = False
        if parameters[10] == "1":
            self.is_elite = True
            
        