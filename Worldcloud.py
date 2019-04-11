# -*- coding: utf-8 -*-
"""
@author: SN
"""


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def Readdata(sIn):
    '''f
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


def Cloud(df):
    '''
       Purpose:
        To make word cloud for male female and unknowns with their choice of what make their day good
    Return value:
        male, female, unknown with things that make their day happy
        '''

    male = []
    tempMale = []
    female = []
    tempFemale = []
    unknown = []
    tempUnknown = []
    j=0
    for i in df.iloc[:, 5]:
        if i == 'male':
            tempMale.append(df.iloc[j]['What makes a good day for you (1)?']);
            tempMale.append(df.iloc[j]['What makes a good day for you (2)?']);
            j = j + 1;
        elif i == 'female':
            tempFemale.append(df.iloc[j]['What makes a good day for you (1)?']);
            tempFemale.append(df.iloc[j]['What makes a good day for you (2)?']);
            j = j + 1;
        elif i == 'unknown':
            tempUnknown.append(df.iloc[j]['What makes a good day for you (1)?']);
            tempUnknown.append(df.iloc[j]['What makes a good day for you (2)?']);
            j=j+1;

    comment_words_m = ' '
    comment_words_f = ' '
    comment_words_u = ' '


    # Converts each token into lowercase
    for i in range(len(tempMale)):
        if isinstance(tempMale[i], str):
            tempMale[i] = tempMale[i].lower()
            male.append(tempMale[i])

    for words in male:
            comment_words_m = comment_words_m + words + ' '

            # Converts each token into lowercase
    for i in range(len(tempFemale)):
        if isinstance(tempFemale[i], str):
            tempFemale[i] = tempFemale[i].lower()
            female.append(tempFemale[i])

    for words in female:
        comment_words_f = comment_words_f + words + ' '

        # Converts each token into lowercase
    for i in range(len(tempUnknown)):
        if isinstance(tempUnknown[i], str):
            tempUnknown[i] = tempUnknown[i].lower()
            unknown.append(tempUnknown[i])

    for words in unknown:
        comment_words_u = comment_words_u + words + ' '

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate(comment_words_m)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate(comment_words_f)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate(comment_words_u)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

    return male, female, unknown

def main():
    #magic keywords
    sIn='ODI-2019.xlsx'

    df = Readdata(sIn)
    male, female, unknown = Cloud(df)


 

if __name__ == "__main__":
    main()
