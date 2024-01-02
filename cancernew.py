import random 
import statistics
import pandas as pd
#reading data
data = pd.read_csv("data.csv")
#delete unesscary features 
newdata = data.drop(['diagnosis'], axis="columns")
del newdata ["id"]
del newdata ["Unnamed: 32"]
v = data["diagnosis"]
#normalization
for y in newdata:
    newdata[y] = (newdata[y] - min(newdata[y]) ) / (max(newdata[y]) - min(newdata[y]))
#splitting train and test
l=[]
rowcount = data.shape[0]
newrow = int(rowcount/20)
for w in range (0,newrow):
    randomdata=random.randint(0,len(newdata)-1)
    l.append(randomdata)
newestdata=newdata.drop(l,axis=0)
name = {}
counter = 0
for s in l:    
    for x in range (1,rowcount):
        if x not in l:
            distance = 0
            for y in newdata:
                distance += abs(newdata[y][s] - newdata[y][x])
            name[x]=distance 
    d = sorted(name.items(),key=lambda x:x[1])
    k=11
    q=[]
    for x in range (k):
     q.append(data["diagnosis"][d[x][0]])
    if statistics.mode(q) == data["diagnosis"][s]:
            counter += 1
print("accuracy=",counter/len(l))
