import pandas as pd

def SumofFive(index, data):
    newColumn = []
    c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=c13=c14=c15=c16=c17=c18=c19=c20=c21=c22=c23=c24=c25=c26=c27=0
    for index2, row in data.iterrows():
        if index == index2:
            for i in range(5):
                c3 = row[3]+c3
                c4 = row[4]+c4
                c5 = row[5]+c5
                c6 = row[6]+c6
                c7 = row[7]+c7
                c8 = row[8]+c8
                c9 = row[9]+c9
                c10 = row[10]+c10
                c11 = row[11]+c11
                c12 = row[12]+c12
                c13 = row[13]+c13
                c14 = row[14]+c14
                c15 = row[15]+c15
                c16 = row[16]+c16
                c17 = row[17]+c17
                c18 = row[18]+c18
                c19 = row[19]+c19
                c20 = row[20]+c20
                c21 = row[21]+c21
                c22 = row[22]+c22
                c23 = row[23]+c23
                c24 = row[24]+c24
                c25 = row[25]+c25
                c26 = row[26]+c26
                c27 = row[27]+c27
        data.insert(index, 'mondaynew', c3)
        data.insert(index, 'tuesdaynew', c4)


    return "first"




def main():
    #magic keywords
    data = pd.read_csv("mood_data_clean.csv")

    data.head()

    for index, row in data.iterrows():
        if index > 0:
            SumofFive(index,data)
        print("last")



if __name__ == "__main__":
    main()
