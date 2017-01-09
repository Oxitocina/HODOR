# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 19:12:15 2017

@author: isidoro
"""
from wx.lib import sheet

class SpreadSheet(sheet.CSheet):
    def __init__(self, parent, data_list, headers):
        real_data_list = [headers] + data_list
            
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.SetSize(parent.GetSize())
        self.SetNumberRows(len(real_data_list))
        self.SetNumberCols(len(real_data_list[0]))
        for i in range(len(real_data_list)):
            self.SetRowSize(i, 20)
        for element in real_data_list:
            for cell in element:
                self.SetCellValue(self.row, self.col, str(cell))
                self.col += 1
            self.col = 0
            self.row += 1