import pandas as pd #importing
import time

f = open('rsns_levels.txt','r') #opens file from scraper code
g = open('rsns-levels-time.txt', 'w')
rsns = f.read().splitlines() #read
unix_time = str(time.time())[:10]

data = []
pairs = {}

for x in rsns: #storing scraper data into list
    data.append(x.split(':'))

for r in data: #adding rsn-level pairs into dictionary
    pairs[r[0]] = r[1]

for i in data:
    out = i[0] + ': ' + '[' + i[1] + ', ' + unix_time + ']'
    g.write(out + '\n')

#port to excelt
df = pd.DataFrame(data=pairs, index=[0])
df = (df.T)
print (df)
df.to_excel('rsn_level.xlsx')

f.close()
g.close()