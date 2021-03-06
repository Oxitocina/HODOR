# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 19:41:15 2016

@author: isidoro
"""

import wx

class AddResults(wx.Frame):
    def __init__(self, parent):
        super(AddResults, self).__init__(parent, size=(500,425))
            
        self.InitUI()
        self.Centre()
        self.Show()
        self.SetTitle('Añadir resultados')
    
    def InitUI(self):
        panel = wx.Panel(self, -1)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        st1 = wx.StaticText(panel, label='Archivo de resultados: ')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(panel)
        self.tc.SetValue('prueba_resultados.csv')
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,25))

        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Elija la carrera: ')
        st2.SetFont(font)
        hbox2.Add((15,0))
        hbox2.Add(st2, flag=wx.CENTER)
        hbox2.Add((55,0))
        self.listbox = wx.ListBox(panel, -1)
        for race in self.GetParent().logic.config_parameters.carreras:
            self.listbox.Append(race)
        hbox2.Add(self.listbox, flag=wx.EXPAND|wx.RIGHT)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.BOTTOM|wx.RIGHT)        
        vbox.Add((-1, 25))
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.cb1 = wx.CheckBox(panel, label='Carrera Internacional')
        self.cb1.SetFont(font)
        hbox3.Add((25,0))
        hbox3.Add(self.cb1, flag=wx.RIGHT)
        self.cb2 = wx.CheckBox(panel, label='No contar para ranking de clubes')
        self.cb2.SetFont(font)
        hbox3.Add((25,0))
        hbox3.Add(self.cb2, flag=wx.LEFT)
        vbox.Add(hbox3, flag=wx.BOTTOM, border=10)
        vbox.Add((-1, 25))
        

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox4.Add(btn1)
        btn2 = wx.Button(panel, label='Cancelar', size=(70, 30))
        hbox4.Add(btn2, flag=wx.ALIGN_CENTER, border=5)
        vbox.Add(hbox4, flag=wx.ALIGN_CENTER, border=10)
        
        btn1.Bind(wx.EVT_BUTTON, self.update)
        btn2.Bind(wx.EVT_BUTTON, self.OnClose)

        panel.SetSizer(vbox)
        
        
    def update(self, e):
        self.GetParent().logic.updateRanking(self.tc.GetValue(), self.listbox.GetStringSelection(), self.cb1.IsChecked(), self.cb2.IsChecked())
        self.GetParent().paintRanks()
        self.OnClose(None)
    
    def OnClose(self, e):
        self.Close(True) 
    