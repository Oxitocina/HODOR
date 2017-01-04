# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 19:12:15 2017

@author: isidoro
"""
from wx.lib import sheet

class SpreadSheet(sheet.CSheet):
    def __init__(self, parent, data_list):
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.SetNumberRows(len(data_list))
        self.SetNumberCols(len(data_list[0]))
                
        for element in data_list:
            for cell in element:
                self.SetCellValue(self.row, self.col, str(cell))
                self.col += 1
            self.row += 1