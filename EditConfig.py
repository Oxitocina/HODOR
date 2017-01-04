# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 17:47:47 2017

@author: isidoro
"""
import wx

class EditConfig(wx.Frame):
    def __init__(self, parent):
        super(EditConfig, self).__init__(parent, size=(500,300))
            
        self.InitUI()
        self.Centre()
        self.Show()
        self.SetTitle('Editar parametros configuracion')
    
    def InitUI(self):
        panel = wx.Panel(self, -1)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        st1 = wx.StaticText(panel, label='Numero de carreras que puntuan: ')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,25))
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        st2 = wx.StaticText(panel, label='Numero de carreras que puntuan en elite: ')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        tc2 = wx.TextCtrl(panel)
        hbox2.Add(tc2, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,25))
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        
        st3 = wx.StaticText(panel, label='Numero de carreras para la media: ')
        st3.SetFont(font)
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        tc3 = wx.TextCtrl(panel)
        hbox3.Add(tc3, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        
        st4 = wx.StaticText(panel, label='Numero de carreras para la media en elite: ')
        st4.SetFont(font)
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        tc4 = wx.TextCtrl(panel)
        hbox4.Add(tc4, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1,25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Cancelar', size=(70, 30))
        hbox5.Add(btn2, flag=wx.ALIGN_CENTER, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_CENTER, border=10)

        panel.SetSizer(vbox)
