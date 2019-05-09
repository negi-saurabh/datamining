import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def SumofFive(index, data):
    newColumn = []
    j=0
    k=0
    m=0

    for index2, row in data.iterrows():

        if index == index2:
            for row2 in data.iterrows():
                loop =0
                j = row2[1][3]+j
                k = row2[1][4]+k
                m = row2[1][11]+m
                loop = loop+1
                if loop == 5:
                    break;

    return "saurabh"


def main():
    #magic keywords
    data = pd.read_csv("mood_data_clean.csv")

    data.head()


    for index, row in data.iterrows():
        if index > 0:
            SumofFive(index,data)
        print("negi")


if __name__ == "__main__":
    main()
