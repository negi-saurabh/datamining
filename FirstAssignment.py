# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:28:04 2019

@author: HP
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


def CollectData(df, A, C_S, Ectrie, QRM, Bioin, Ba):
    '''
       Purpose:
        Sort Data based upon the background of the students taking this course
    Inputs:
        df, A, C_S, Ectrie, QRM, Bioin, Ba
    Return value:
        AI:Artificial Intelligence, CS:Computer Science, Ectrics: Econometrics, QuantRM:Quantatitive Risk Management, BIO: Biotechnology
        , BA: Business Analytics
        '''
    
    
    
    AI = df.iloc[:,0][df.iloc[:,0].str.contains(A, case=False)].value_counts()
    CS = df.iloc[:,0][df.iloc[:,0].str.contains(C_S)].value_counts()
    Ectrics = df.iloc[:,0][df.iloc[:,0].str.contains(Ectrie, case=False)].value_counts()
    QuantRM = df.iloc[:,0][df.iloc[:,0].str.contains(QRM, case=False)].value_counts()
    BIO = df.iloc[:,0][df.iloc[:,0].str.contains(Bioin, case=False)].value_counts()
    BA = df.iloc[:,0][df.iloc[:,0].str.contains(Ba, case=False)].value_counts()
    



    

    return AI, CS, Ectrics, QuantRM, BIO, BA


def main():
    #magic keywords
    sIn='ODI-2019.xlsx'
    # met case=False we match strings regardless of capital letters or not
    A = 'ai|Artificial'
    C_S = 'Com|CS|com'# keyword 'cs' is present in some words thus we leave case=False out
    Ectrie = 'eco|eor'
    QRM = 'quant|risk|qrm' 
    Bioin = 'bio'
    Ba = 'ba|analyt'
    
    
    df = Readdata(sIn)
    AI, CS, Ectrics, QuantRM, BIO, BA=CollectData(df, A, C_S, Ectrie, QRM, Bioin, Ba)
    print(AI)
    print(CS)
    print(Ectrics)
    print(QuantRM)
    print(BIO)
    print(BA)


    #group_counts = Counter(df.iloc[:,0)

if __name__ == "__main__":
    main()
