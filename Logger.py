# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:01:32 2016

@author: isidoro
"""

def logError(message, errType):
    if errType == 1:
        with open('logNoPuntua.txt', 'a') as logFile:
            for line in message:
                logFile.write('Persona no cualificada para competir: ' + line + '\n')
    elif errType == 2:
        with open('logError.txt', 'a') as errorFile:
            for line in message:
                errorFile.write('Ha ocurrido un error: ' + line + '\n')
    else:
        with open('logVariado.txt', 'a') as errorFile:
            for line in message:
                errorFile.write('Ha ocurrido un algo: ' + line + '\n')
            
    