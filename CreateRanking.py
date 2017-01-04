# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:59:29 2016

@author: isidoro
"""
import wx

class CreateRanking(wx.Frame):
  
    def __init__(self, parent):
        super(CreateRanking, self).__init__(parent, size=(390, 350))
            
        self.InitUI()
        self.Centre()
        self.Show()
        self.SetTitle('Crear Ranking')
        
    def InitUI(self):
    
        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Nombre: ')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(panel)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Fichero licencias: ')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.tc2 = wx.TextCtrl(panel)
        hbox2.Add(self.tc2, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))


        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Fichero categorias: ')
        st3.SetFont(font)
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        self.tc3 = wx.TextCtrl(panel)
        hbox3.Add(self.tc3, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label='Fichero configuracion: ')
        st4.SetFont(font)
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        self.tc4 = wx.TextCtrl(panel)
        hbox4.Add(self.tc4, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st6 = wx.StaticText(panel, label='Fichero clubes anterior temporada: ')
        st6.SetFont(font)
        hbox6.Add(st6, flag=wx.RIGHT, border=8)
        self.tc6 = wx.TextCtrl(panel)
        hbox6.Add(self.tc6, proportion=1)
        vbox.Add(hbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))
        
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Crear', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Cancelar', size=(70, 30))
        hbox5.Add(btn2, flag=wx.CENTER|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_CENTER|wx.RIGHT, border=10)
        
        btn1.Bind(wx.EVT_BUTTON, self.create)
        btn2.Bind(wx.EVT_BUTTON, self.OnClose)
        panel.SetSizer(vbox)

    def create(self, e):
        self.GetParent().logic.setConfigParams(self.tc4.GetValue())
        self.GetParent().logic.setLicenses(self.tc2.GetValue())
        self.GetParent().logic.setCategories(self.tc3.GetValue())
        self.GetParent().logic.createRanking(self.tc.GetValue(), self.tc6.GetValue())
        self.GetParent().logic.currentRanking
        self.OnClose(None)
    def OnClose(self, e):
        self.Close(True) 
