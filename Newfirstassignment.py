# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:55:26 2019

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:28:04 2019

@author: HP
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keyword 
import filecmp
import difflib 
''' in order to run the code for line 86 in code fuzzywuzzy go to : https://anaconda.org/conda-forge/fuzzywuzzy
    install it with  Anaconda Prompt if using Anaconda, select first link: conda install -c conda-forge fuzzywuzzy 
    paste it in Anaconda Prompt , afterwards code can be run smoothly '''
from fuzzywuzzy import fuzz
from fuzzywuzzy import process







def Readdata(sIn):
    '''
       Purpose:
        Read Data
    Inputs:
        sIn : Data file name
    Return value:
        df : dataframe
        '''
    
    
    df = pd.read_excel(sIn)
    df = df.set_index('Timestamp')    
    
 
    
    return df


def CollectData(df):
    
    '''          
      Purpose: 
          Set New Column within the existing DataFrame where we sort all the Studies 
         Inputs:
             df
        Return Value:
         Study  '''
    
    
    
    
    
    
    
    AI = ['AI', 'Artificial Intelligence', 'Master Artificial Intelligence', 'Master AI']
    CS = ['Computer Science', 'Master CS', 'Master Computer Science', 'CS exchan', 'MsC']
    CLS = ['Master CLS','CLS', 'Computational Science']
    Econometrics = ['EOR', 'Econometrics','Master Econometrics','Operation Research', 'Financial Econometriv']
    QuantRM = ['QRM', 'Quantitative Risk Management', 'DHPQRM']
    BIO = ['Bioinformatics and systems Biology','BIO','Biosb', 'Bioinf', 'Boinformatics']
    BA = ['Business Analytics','BA']
    Finance = ['Finance','Master of Finance']
    Datascience = ['Data science', 'DS']
    Healthstudies = ['Health', 'Entrepeneurship', 'Health sciences','Medical']
    Business = ['Business', 'MBA','Business Administration']
    Total_studies = AI + CS + CLS + Econometrics + QuantRM+BIO+BA+Finance+Datascience+Healthstudies+Business
    
    ''' Apply process.extract() to get the match of the studies and save in match_fuzz, then take highest match above 80
    and store in new df column : Study position of column next to 'What programme are you in ?' ''' 
    
    match_fuzz = []
    for study in df.iloc[:,0].values:
        process.extract(study, Total_studies, scorer = fuzz.token_set_ratio)[0]
        match_fuzz.append(process.extract(study, Total_studies, scorer = fuzz.token_set_ratio)[0])
    
    df['Study'] = df.iloc[:,0]
    Study= df['Study']
    
    for i, match in enumerate(match_fuzz):
        if match[1] > 80:
            if match[0] in AI:
                Study[i] ='Artificial Intelligence'
            elif match[0] in CS:
                Study[i] ='Computer Science'
            elif match[0] in CLS:
                Study[i] = 'Computational Science'
            elif match[0] in Econometrics:
                Study[i]= 'Econometrics'
            elif match[0] in QuantRM:
                Study[i]='Quantatitive Risk Management'
            elif match[0] in BIO:
                Study[i]='Bioinformatics and Systems Biology'
            elif match[0] in BA:
                Study[i]='Business Analytics'
            elif match[0] in Finance:
                Study[i]='Finance'
            elif match[0] in Datascience:
                Study[i] = 'DataScience'
            elif match[0] in Healthstudies:
                Study[i]='Health Studies'
            elif match[0] in Business:
                Study[i]='Business Studies'
    
    df.drop(labels= ['Study'], axis = 1, inplace= True)
    df.insert(1, 'Study', Study)
    
    ''' create new list for plotting values with category Others for better representation of pie plot ''' 

    return Study

def Plots(df, Study):
    
    '''          
      Purpose: 
          Plot pie chart for Studies and seperate them by categories 
         Inputs:
             df, Study
        Return Value:
         pie: Complete Study column with with group of Others
         pie_2: Plot Original Other categories 
         '''
    
    
    
    
    Com_list = df.iloc[:,1].value_counts()
    Com_part = Com_list.iloc[0:11]


    '''Create Series with category Other'''
    Other = []
    for i, c in enumerate(Com_list.index):
        if Com_list[i] < 3:
            Other.append(c)
            Org_Other = pd.Series(Other).value_counts()
    ''' Manipulate Other in order to plot it with values of Study'''   
    Plot_Other= []
    for i in range(len(Other)): 
        i = 'Other'
        Plot_Other.append(i)
        Pl_Other = pd.Series(Plot_Other).value_counts()
   
    Other_Com = pd.concat([Com_part, Pl_Other])
    
    
    '''Plot values of Studies in pie chart with Other''' 
    pie = Other_Com.plot(kind='pie', autopct = '%.1f%%', shadow= True, rotatelabels=True, labeldistance=1, explode = [0.09,0,0,0,0,0,0,0,0,0,0,0])
    plt.title('Plot of Studies with Other Category', loc='center', fontsize=10, fontweight=100, pad=50, horizontalalignment='center')
    plt.figure(0)
    '''Plot values of Other alone'''
    pie_2 = Org_Other.plot(kind='pie', autopct = '%.1f%%', shadow= True, rotatelabels=True, labeldistance=1, explode = [0.09,0,0,0,0,0,0,0,0,0,0])
    plt.title('Others category of students education', loc='center', fontsize=10, fontweight=100, pad=50, horizontalalignment='center')
    plt.ylabel("")
    plt.figure(1)
    plt.ylabel("")
    plt.show()

    return pie, pie_2




def main():
    #magic keywords
    sIn='ODI-2019.xlsx'

    
    
    df = Readdata(sIn)
    Study=CollectData(df)
    pie, pie_2 = Plots(df, Study)
 

    
if __name__ == "__main__":
    main()
