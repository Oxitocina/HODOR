# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:33:26 2016

@author: isidoro
"""

import wx

ID_NEW = 1
ID_RENAME = 2
ID_CLEAR = 3
ID_DELETE = 4


class AddOrganizers(wx.Frame):
    def __init__(self, parent):
        super(AddOrganizers, self).__init__(parent, size=(500,300))
            
        self.InitUI()
        self.Centre()
        self.Show()
        self.SetTitle('Añadir organizadores')
    
    def InitUI(self):
        panel = wx.Panel(self, -1)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        st1 = wx.StaticText(panel, label='Archivo de organizadores: ')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
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
        
        cb2 = wx.CheckBox(panel, label='No contar para ranking de clubes')
        cb2.SetFont(font)
        hbox3.Add((25,0))
        hbox3.Add(cb2, flag=wx.LEFT)
        vbox.Add(hbox3, flag=wx.BOTTOM, border=10)
        vbox.Add((-1, 25))
        

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox4.Add(btn1)
        btn2 = wx.Button(panel, label='Cancelar', size=(70, 30))
        hbox4.Add(btn2, flag=wx.ALIGN_CENTER, border=5)
        vbox.Add(hbox4, flag=wx.ALIGN_CENTER, border=10)

        panel.SetSizer(vbox)

