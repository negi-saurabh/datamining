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
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd


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
    CLS = ['Master CLS', 'CLS', 'Computational Science']
    Econometrics = ['EOR', 'Econometrics', 'Master Econometrics', 'Operation Research', 'Financial Econometriv']
    QuantRM = ['QRM', 'Quantitative Risk Management', 'DHPQRM']
    BIO = ['Bioinformatics and systems Biology', 'BIO', 'Biosb', 'Bioinf', 'Boinformatics']
    BA = ['Business Analytics', 'BA']
    Finance = ['Finance', 'Master of Finance']
    Datascience = ['Data science', 'DS']
    Healthstudies = ['Health', 'Entrepeneurship', 'Health sciences', 'Medical']
    Business = ['Business', 'MBA', 'Business Administration']
    Total_studies = AI + CS + CLS + Econometrics + QuantRM + BIO + BA + Finance + Datascience + Healthstudies + Business

    ''' Apply process.extract() to get the match of the studies and save in match_fuzz, then take highest match above 80
    and store in new df column : Study position of column next to 'What programme are you in ?' '''

    match_fuzz = []
    for study in df.iloc[:, 0].values:
        process.extract(study, Total_studies, scorer=fuzz.token_set_ratio)[0]
        match_fuzz.append(process.extract(study, Total_studies, scorer=fuzz.token_set_ratio)[0])

    df['Study'] = df.iloc[:, 0]
    Study = df['Study']

    for i, match in enumerate(match_fuzz):
        if match[1] > 80:
            if match[0] in AI:
                Study[i] = 'Artificial Intelligence'
            elif match[0] in CS:
                Study[i] = 'Computer Science'
            elif match[0] in CLS:
                Study[i] = 'Computational Science'
            elif match[0] in Econometrics:
                Study[i] = 'Econometrics'
            elif match[0] in QuantRM:
                Study[i] = 'Quantatitive Risk Management'
            elif match[0] in BIO:
                Study[i] = 'Bioinformatics and Systems Biology'
            elif match[0] in BA:
                Study[i] = 'Business Analytics'
            elif match[0] in Finance:
                Study[i] = 'Finance'
            elif match[0] in Datascience:
                Study[i] = 'DataScience'
            elif match[0] in Healthstudies:
                Study[i] = 'Health Studies'
            elif match[0] in Business:
                Study[i] = 'Business Studies'

    df.drop(labels=['Study'], axis=1, inplace=True)
    df.insert(1, 'Study', Study)

    ML_course =[]
    Info_Ret_course = []
    Stat_course = []
    DB_course = []
    '''4-----> ML_course'''
    '''1-----> Info_Ret_course'''
    '''2-----> Stat_course'''
    '''3-----> DB_course'''

    AI1, AI2, AI3, AI4 = 0, 0, 0, 0
    CS1, CS2, CS3, CS4 = 0, 0, 0, 0
    CuS1, CuS2, CuS3, CuS4 = 0, 0, 0, 0
    E1, E2, E3, E4 = 0, 0, 0, 0
    QRM1, QRM2, QRM3, QRM4 = 0, 0, 0, 0
    BSB1, BSB2, BSB3, BSB4 = 0, 0, 0, 0
    BA1, BA2, BA3, BA4 = 0, 0, 0, 0
    F1, F2, F3, F4 = 0, 0, 0, 0
    DS1, DS2, DS3, DS4 = 0, 0, 0, 0
    HS1, HS2, HS3, HS4 = 0, 0, 0, 0
    BS1, BS2, BS3, BS4 = 0, 0, 0, 0
    for sub in df.iloc[:, 0:6].values:
        '''for machine learning'''
        if sub[2] == 'yes':
            if sub[1] == 'Artificial Intelligence':
                AI4= AI4+1
            if sub[1] == 'Computer Science':
                CS4= CS4+1
            if sub[1] == 'Computational Science':
                CuS4= CuS4+1
            if sub[1] == 'Econometrics':
                E4= E4+1
            if sub[1] == 'Quantatitive Risk Management':
                QRM4= QRM4+1
            if sub[1] == 'Bioinformatics and Systems Biology':
                BSB4= BSB4+1
            if sub[1] == 'Business Analytics':
                BA4= BA4+1
            if sub[1] == 'Finance':
                F4= F4+1
            if sub[1] == 'DataScience':
                DS4= DS4+1
            if sub[1] == 'Health Studies':
                HS4= HS4+1
            if sub[1] == 'Business Studies':
                BS4= BS4+1
        '''for informational retrieval'''
        if sub[3] == 1:
            if sub[1] == 'Artificial Intelligence':
                AI1= AI1+1
            if sub[1] == 'Computer Science':
                CS1= CS1+1
            if sub[1] == 'Computational Science':
                CuS1= CuS1+1
            if sub[1] == 'Econometrics':
                E1= E1+1
            if sub[1] == 'Quantatitive Risk Management':
                QRM1= QRM1+1
            if sub[1] == 'Bioinformatics and Systems Biology':
                BSB1= BSB1+1
            if sub[1] == 'Business Analytics':
                BA1= BA1+1
            if sub[1] == 'Finance':
                F1= F1+1
            if sub[1] == 'DataScience':
                DS1= DS1+1
            if sub[1] == 'Health Studies':
                HS1= HS1+1
            if sub[1] == 'Business Studies':
                BS1= BS1+1
        '''for statistics'''
        if sub[4] == 'mu':
            if sub[1] == 'Artificial Intelligence':
                AI2= AI2+1
            if sub[1] == 'Computer Science':
                CS2= CS2+1
            if sub[1] == 'Computational Science':
                CuS2= CuS2+1
            if sub[1] == 'Econometrics':
                E2= E2+1
            if sub[1] == 'Quantatitive Risk Management':
                QRM2= QRM2+1
            if sub[1] == 'Bioinformatics and Systems Biology':
                BSB2= BSB2+1
            if sub[1] == 'Business Analytics':
                BA2= BA2+1
            if sub[1] == 'Finance':
                F2= F2+1
            if sub[1] == 'DataScience':
                DS2= DS2+1
            if sub[1] == 'Health Studies':
                HS2= HS2+1
            if sub[1] == 'Business Studies':
                BS2= BS2+1
        '''for databases'''
        if sub[5] == 'ja':
            if sub[1] == 'Artificial Intelligence':
                AI3= AI3+1
            if sub[1] == 'Computer Science':
                CS3= CS3+1
            if sub[1] == 'Computational Science':
                CuS3= CuS3+1
            if sub[1] == 'Econometrics':
                E3= E3+1
            if sub[1] == 'Quantatitive Risk Management':
                QRM3= QRM3+1
            if sub[1] == 'Bioinformatics and Systems Biology':
                BSB3= BSB3+1
            if sub[1] == 'Business Analytics':
                BA3= BA3+1
            if sub[1] == 'Finance':
                F3= F3+1
            if sub[1] == 'DataScience':
                DS3= DS3+1
            if sub[1] == 'Health Studies':
                HS3= HS3+1
            if sub[1] == 'Business Studies':
                BS3= BS3+1

    # y-axis in bold
    rc('font', weight='bold')

    # Values of each group
    bars1 = np.array([AI4, AI1, AI2, AI3])
    bars2 = np.array([CS4, CS1, CS2, CS3])
    bars3 = np.array([CuS4, CuS1, CuS2, CuS3])
    bars4 = np.array([E4, E1, E2, E3])
    bars5 = np.array([QRM4, QRM1, QRM2, QRM3])
    bars6 = np.array([BSB4, BSB1, BSB2, BSB3])
    bars7 = np.array([BA4, BA1, BA2, BA3])
    bars8 = np.array([F4, F1, F2, F3])
    bars9 = np.array([DS4, DS1, DS2, DS3])
    bars10 = np.array([HS4, HS1, HS2, HS3])
    bars11= np.array([BS4, BS1, BS2, BS3])



    # Heights of bars
    bars = np.add(bars1, bars2).tolist()

    # The position of the bars on the x-axis
    r = [0, 1, 2, 3]

    # Names of group and bar width
    names = ['ML','IR','Statistics','Databases']
    barWidth = 1

    # Create bars
    p1= plt.bar(r, bars1, color='#6c17b5', edgecolor='white', width=0.7,label='Artificial Intelligence')
    # Create bars (middle)
    p2= plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=0.7, label='Computer Science')
    # Create bars
    p3= plt.bar(r, bars3, bottom=bars2+bars1, color='#ffcd35', edgecolor='white', width=0.7,label='Computational Science')
    # Create bars
    p4= plt.bar(r, bars4, bottom=bars2+bars1+bars3, color='#fa6766', edgecolor='white', width=0.7,label='Econometrics')
    # Create bars
    p5= plt.bar(r, bars5, bottom=bars2+bars1+bars3+bars4, color='#8a7fbe', edgecolor='white', width=0.7,label='Quantatitive Risk Management')
    # Create bars
    p6= plt.bar(r, bars6, bottom=bars2+bars1+bars3+bars4+bars5, color='#200f5e', edgecolor='white', width=0.7,label='Bioinformatics and Systems Biology')
    # Create bars
    p7= plt.bar(r, bars7, bottom=bars2+bars1+bars3+bars4+bars5+bars6, color='#880d1f', edgecolor='white', width=0.7, label='Business Analytics')
    # Create bars
    p8= plt.bar(r, bars8, bottom=bars2+bars1+bars3+bars4+bars5+bars6+bars7, color='#f28464', edgecolor='white', width=0.7, label='Finance')
    # Create bars
    p9= plt.bar(r, bars9, bottom=bars2+bars1+bars3+bars4+bars5+bars6+bars7+bars8, color='#b12bb4', edgecolor='white', width=0.7, label='DataScience')
    # Create bars
    p10= plt.bar(r, bars10, bottom=bars2+bars1+bars3+bars4+bars5+bars6+bars7+bars8+bars9, color='#7e603d', edgecolor='white', width=0.7, label='Health Studies')
    # Create bars
    p11= plt.bar(r, bars11, bottom=bars2+bars1+bars3+bars4+bars5+bars6+bars7+bars8+bars9+bars10, color='#5fc4f8', edgecolor='white', width=0.7, label='Business Studies')

    ''' plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], p11[0]), ('Artificial Intelligence',
                                                                                                 'Computer Science','Computational Science')
               ,'Econometrics','Quantatitive Risk Management','Bioinformatics and Systems Biology','Business Analytics','Finance',
               'DataScience','Health Studies','Business Studies') '''


    plt.legend(loc="upper left", prop={'size': 6})
    # Custom X axis
    plt.xticks(r, names, fontweight='bold')
    plt.ylabel('Number of students')
    plt.title('Students in each of the Disciplines who have done the Courses')

    # Show graphic
    plt.show()


    return Study


def Plots():
    '''
      Purpose:
          Plot stacked bar chart for Studies and seperate them by categories
         Inputs:
             df, Study
        Return Value:
         pie: Complete Study column with with group of Others
         pie_2: Plot Original Other categories
         '''

    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, yerr=menStd)
    p2 = plt.bar(ind, womenMeans, width,
                 bottom=menMeans, yerr=womenStd)

    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))

    plt.show()

    return pie, pie_2


def main():
    # magic keywords
    sIn = 'ODI-2019.xlsx'

    df = Readdata(sIn)
    Study = CollectData(df)
    '''pie, pie_2 = Plots()'''


if __name__ == "__main__":
    main()
