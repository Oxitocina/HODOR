# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:01:47 2016

@author: isidoro
"""
import sys
import os
import wx

import CreateRanking
import OpenRanking
import AddResults
import AddOrganizers
import EditConfig
import SpreadSheet
import Logic

class MainGraph(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MainGraph, self).__init__(*args, **kwargs)
        self.logic = Logic.Logic()
        
        self.InitUI()
    
    def InitUI(self):
        
        menu_bar = wx.MenuBar()
        toolbar = self.CreateToolBar()
        self.sb = self.CreateStatusBar()
        
        
        ranking_menu = wx.Menu()
        edit_menu = wx.Menu()
        statistics_menu = wx.Menu()
        help_menu = wx.Menu()
        
        new_tool = toolbar.AddLabelTool(wx.ID_FILE, 'New', wx.Bitmap(os.getcwd() + '\\images\\new_rank.png'))
        open_tool = toolbar.AddLabelTool(wx.ID_OPEN, 'Open', wx.Bitmap(os.getcwd() + '\\images\\open_rank.png'))
        add_tool = toolbar.AddLabelTool(wx.ID_ADD, 'Add results', wx.Bitmap(os.getcwd() + '\\images\\add_results.png'))        
        
        new_menu_opt = ranking_menu.Append(wx.ID_FILE, 'Nuevo ranking', 'Crea nuevo ranking')
        open_menu_opt = ranking_menu.Append(wx.ID_OPEN, 'Abrir ranking', 'Abre un ranking existente')
        #TODO: Añadir ñ y acentos        
        add_res_menu_opt = ranking_menu.Append(wx.ID_ADD, 'Anadir resultados', 'Permite añadir los resultados de una carrera al ranking actual')
        add_organizers = ranking_menu.Append(wx.ID_SAVE, 'Anadir organizadores', 'Permite añadir los organizadores de una carrera')
        
        ed_params_menu_opt = edit_menu.Append(wx.ID_EDIT, 'Editar parametros', 'Permite cambiar los parámetros de configuración desde la aplicación')
        ed_categ_menu_opt = edit_menu.Append(wx.ID_PROPERTIES, 'Editar categorias', 'Permite editar los parametros de cada categoria desde la aplicacion')
        
        manual_menu_opt = help_menu.Append(wx.ID_HELP, 'Manual', 'Abre el manual de la aplicacion')
        about_menu_opt2 = help_menu.Append(wx.ID_ABOUT, 'Acerca de', 'Muentra informacion sobre la aplicacion')
        
        
        menu_bar.Append(ranking_menu, '&Ranking')
        menu_bar.Append(edit_menu, '&Edicion')
        menu_bar.Append(statistics_menu, 'E&stadisticas')
        menu_bar.Append(help_menu, '&Ayuda')
        
        self.SetMenuBar(menu_bar)
        toolbar.Realize()
        
        self.Bind(wx.EVT_MENU, self.createRank, new_menu_opt)
        self.Bind(wx.EVT_MENU, self.openRank, open_menu_opt)
        self.Bind(wx.EVT_MENU, self.addResults, add_res_menu_opt)
        self.Bind(wx.EVT_MENU, self.addOrganizers, add_organizers)
        self.Bind(wx.EVT_MENU, self.editParameters, ed_params_menu_opt)        
        
        
        self.Bind(wx.EVT_TOOL, self.createRank, new_tool)
        self.Bind(wx.EVT_TOOL, self.openRank, open_tool)
        self.Bind(wx.EVT_TOOL, self.addResults, add_tool)
        
        box = wx.BoxSizer(wx.HORIZONTAL)
        self.notebook = wx.Notebook(self, -1, style=wx.BOTTOM)
        box.Add((5,5) , 0)
        box.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(box)
        self.SetSize((1200,700))
        self.SetTitle('HODOR')
        self.Centre()
        self.Show(True)
        
    def onQuit(self, e):
        self.Close()
        sys.exit()
        
    def createRank(self, e):
        CreateRanking.CreateRanking(self)
    
    def openRank(self, e):
        OpenRanking.OpenRanking(self)
    
    def addResults(self, e):
        AddResults.AddResults(self)
    
    def addOrganizers(self, e):
        AddOrganizers.AddOrganizers(self)
    
    def editParameters(self, e):
        EditConfig.EditConfig(self)
        
        
    
    def paintRanks(self):
        ind_rank = []
        club_rank = []
        for category in self.logic.current_ranking.data_ind:
            for position in range(1,len(category.keys())+1):
                actual_person = ''
                for person in category.keys():
                    if int(self.logic.current_ranking.positions_ind[person]) == position:
                        actual_person = person
                row = [self.logic.current_ranking.positions_ind[actual_person], actual_person]
                for element in category[actual_person]:
                    row.append(element)
                ind_rank.append(row)
        sheet_ind = SpreadSheet.SpreadSheet(self.notebook, ind_rank,
                                            self.logic.config_parameters.cabecera_ranking_individual[0:12] +
                                            self.logic.config_parameters.carreras +
                                            self.logic.config_parameters.cabecera_ranking_individual[12:])
        
        for division in self.logic.current_ranking.data_club:
            for position in range(1,len(division.keys())+1):
                actual_club = ''
                for club in division.keys():
                    if int(self.logic.current_ranking.positions_club[club]) == position:
                        actual_club = club
                if actual_club != '':
                    row = [self.logic.current_ranking.positions_club[actual_club], actual_club]
                    for element in division[actual_club]:
                        row.append(element)
                    club_rank.append(row)
        sheet_club = SpreadSheet.SpreadSheet(self.notebook, club_rank,
                                             self.logic.config_parameters.cabecera_ranking_clubes[0:5] +
                                             self.logic.config_parameters.carreras)
        
        self.notebook.AddPage(sheet_ind, 'Individual')
        self.notebook.AddPage(sheet_club, 'Grupos')
        
        
        
def main():   
    ex = wx.App()
    MainGraph(None)
    ex.MainLoop()
    
if __name__ == '__main__':
    main()
        