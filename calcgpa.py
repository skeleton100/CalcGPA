import pandas as pd

df = pd.read_csv('GPAdata.csv')

suma = 0
sumb = 0
sumc = 0
sumf = 0

for index,item in df.iterrows():
    if item['評価'] == 'A':
        suma += item['単位数']
    elif item['評価'] == 'B':
        sumb += item['単位数']
    elif item['評価'] == 'C':
        sumc += item['単位数']
    elif item['評価'] == 'D':
        sumf += item['単位数']
    elif item['評価'] == 'F':
        sumf += item['単位数']

GPA = (4.0*suma + 3.0*sumb + 2.0*sumc) / (suma+sumb+sumc+sumf)

print('Your GPA is',GPA)
