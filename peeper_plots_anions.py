# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:17:06 2017

@author: Patrick
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
fig = plt.figure(figsize=(15,9))
fig.subplots_adjust(hspace=.6)
plt.style.use('bmh')
ax1 = plt.subplot(2,4,1)
plt.title('Flouride')
plt.xlabel('mM')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,14] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,14],peeper_data.ix[i,1], 'ro')
            i += 1
        else:
            i += 1
    else:
        i +=1
ax2 = plt.subplot(2,4,2)
plt.title('Chloride')
plt.xlabel('mM')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90)  
plt.gca().invert_yaxis() 
i = 0 
while i < 32:
    if peeper_data.ix[i,15] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,15],peeper_data.ix[i,1], 'go')
            i += 1
        else:
            i += 1
    else:
        i +=1  
ax3 = plt.subplot(2,4,3)
plt.title('Nitrite-N')
plt.xlabel('mM')
plt.ylabel('Depth (cm)')
plt.xticks(rotation = 90)   
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,16] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,16],peeper_data.ix[i,1], 'ro')
            i += 1
        else:
            i += 1
    else:
        i +=1   
ax4 = plt.subplot(2,4,4)
plt.title('Bromide')
plt.xlabel('mM')
plt.ylabel('Depth (cm)')  
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,17] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,17],peeper_data.ix[i,1], 'go')
            i += 1
        else:
            i += 1
    else:
        i +=1   
ax5 = plt.subplot(2,4,5)
plt.title('Nitrate-N')
plt.xlabel('mM')
plt.ylabel('Depth (cm)')
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,18] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,18],peeper_data.ix[i,1], 'ro')
            i += 1
        else:
            i += 1
    else:
        i +=1   
ax6 = plt.subplot(2,4,6)
plt.title('Sulfate')
plt.xlabel('mM')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,19] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,19],peeper_data.ix[i,1], 'go')
            i += 1
        else:
            i += 1
    else:
        i +=1    
ax7 = plt.subplot(2,4,7)
plt.title('Thiosulfate')
plt.xlabel('mM')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,20] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,20],peeper_data.ix[i,1], 'ro')
            i += 1
        else:
            i += 1
    else:
        i +=1      
ax8 = plt.subplot(2,4,8)
plt.title('Phosphate-P')
plt.xlabel('mM')
plt.ylabel('Depth (cm)') 
plt.xticks(rotation = 90) 
plt.gca().invert_yaxis()
i = 0 
while i < 32:
    if peeper_data.ix[i,21] >= 0:
        if peeper_data.ix[i,0] == ID:
            plt.plot(peeper_data.ix[i,21],peeper_data.ix[i,1], 'go')
            i += 1
        else:
            i += 1
    else:
        i +=1   
plt.tight_layout(pad=4,h_pad=6)
plt.show()