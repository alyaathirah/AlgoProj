import pandas as pd
import matplotlib.pyplot as plt

fullData = pd.read_csv('distance.csv')
print(fullData)

courier = fullData['Courier Company']
cust1 = fullData['Customer 1']
cust2 = fullData['Customer 2']
cust3 = fullData['Customer 3']
sent = fullData['Article']
rank_d = []
rank=[]
total = 0
total1=0
for i in range(5):
    total = (cust1[i] + cust2[i] +cust3[i])/3
    rank_d.append(round(total,2))
    total1 = (rank_d[i] + sent[i]) / 2
    rank.append(round(total1, 2))


fullData['CRank_dist'] = rank_d
fullData['Rank_d&a'] = rank
print(fullData)
"""""
set1 = fullData.sort_values(by=['CRank-dist'],ascending=[True])
rank1=[1,2,3,4,5]
set1['Rank'] = rank1
print(set1)"""

set1 = fullData.sort_values(by=['Rank_d&a'],ascending=[True])
rank1=[1,2,3,4,5]
set1['Ranking'] = rank1
print(set1)

plt.ylim(1, 5)

plt.plot(set1['Courier Company'],set1['CRank_dist'],color='blue',label ='Distance')
plt.scatter(set1['Courier Company'],set1['CRank_dist'],color='lightblue')
plt.plot(set1['Courier Company'],set1['Article'],color='red',label ='Article')
plt.scatter(set1['Courier Company'],set1['Article'],color='pink')
plt.plot(set1['Courier Company'],set1['Rank_d&a'],color='yellow',label ='Both')
plt.scatter(set1['Courier Company'],set1['Rank_d&a'],color='green')

plt.legend()
plt.gca().invert_yaxis()
plt.xlabel('Courier Company')
plt.ylabel('Ranking')
plt.title('Courier Company Ranking ')
plt.show()







