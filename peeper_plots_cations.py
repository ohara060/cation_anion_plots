# -*- coding: utf-8 -*-
"""
Script for Plotting Cation Concentrations at Depth for Sample Locations at
Second Creek, MN

Plots data with depth on the y axis uM on the x axis.

All cation concentrations at depth are displayed at the same time

sample data files are provided, data needs to be setup in accordance with
format of sample data files. Input file is set as "peeper_data" directly below
ID flag.

A flag is set at the beginning of the script for sample location labeled "ID". 
comment out all but one location for script to run properly.

"""

import pandas as pd

from matplotlib import pyplot as plt

#ID = 'W3'
#ID = 'W4'
#ID = 'W5'
#ID = 'W6'
#ID = 'C3'
#ID = 'C4'
#ID = 'C5'
ID = 'C6'


peeper_data = pd.read_csv("cation_anion_peeper.csv", header = 0)
peeper_data = peeper_data.rename(columns=lambda x: x.strip())
fig = plt.figure(figsize=(12,15))
fig.subplots_adjust(hspace=.6)
plt.style.use('bmh')
ax1 = plt.subplot(3,4,1)
plt.title('Al')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,2],peeper_data.ix[i,1], 'ro')
        i += 1
    else:
        i += 1
ax2 = plt.subplot(3,4,2)
plt.title('Ba')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90)  
plt.gca().invert_yaxis() 
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,3],peeper_data.ix[i,1], 'go')
        i += 1
    else:
        i += 1   
ax3 = plt.subplot(3,4,3)
plt.title('Ca')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)')
plt.xticks(rotation = 90)   
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,4],peeper_data.ix[i,1], 'yo')
        i += 1
    else:
        i += 1     
ax4 = plt.subplot(3,4,4)
plt.title('Fe')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)')  
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,5],peeper_data.ix[i,1], 'ro')
        i += 1
    else:
        i += 1    
ax5 = plt.subplot(3,4,5)
plt.title('K')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)')
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,6],peeper_data.ix[i,1], 'go')
        i += 1
    else:
        i += 1   
ax6 = plt.subplot(3,4,6)
plt.title('Li')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,7],peeper_data.ix[i,1], 'yo')
        i += 1
    else:
        i += 1    
ax7 = plt.subplot(3,4,7)
plt.title('Mg')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,8],peeper_data.ix[i,1], 'ro')
        i += 1
    else:
        i += 1      
ax8 = plt.subplot(3,4,8)
plt.title('Mn')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,9],peeper_data.ix[i,1], 'go')
        i += 1
    else:
        i += 1    
ax9 = plt.subplot(3,4,9)
plt.title('Na')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis() 
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,10],peeper_data.ix[i,1], 'yo')
        i += 1
    else:
        i += 1    
ax10 = plt.subplot(3,4,10)
plt.title('P')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)')
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,11],peeper_data.ix[i,1], 'ro')
        i += 1
    else:
        i += 1    
ax11 = plt.subplot(3,4,11)
plt.title('Si')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)')
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,12],peeper_data.ix[i,1], 'go')
        i += 1
    else:
        i += 1   
ax12 = plt.subplot(3,4,12)
plt.title('Sr')
plt.xlabel('$\mu$M')
plt.ylabel('Depth (cm)')
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,0] == ID:
        plt.plot(peeper_data.ix[i,13],peeper_data.ix[i,1], 'yo')
        i += 1
    else:
        i += 1  
plt.tight_layout(pad=4,h_pad=6)
plt.show()
