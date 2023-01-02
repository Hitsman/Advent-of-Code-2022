#!/usr/bin/env python
# coding: utf-8

# In[17]:


grove=[]
visib=[]
with open('Day8Input.txt','r') as file:
    for line in file:
        row=[]
        visibrow=[]
        for digit in line.rstrip():
            row.append(int(digit))
            visibrow.append(0)
        grove.append(row)
        visib.append(visibrow)
#print(grove)
#print(visib)

for y in range(len(grove)):
    height=-1
    for x in range(len(grove[y])):
        if grove[y][x]>height: visib[y][x]=1; height=grove[y][x]
        
    height=-1
    for x in reversed(range(len(grove[y]))):
        if grove[y][x]>height: visib[y][x]=1; height=grove[y][x]
        
        
for x in range(len(grove[0])):
    height=-1
    for y in range(len(grove[x])):
        if grove[y][x]>height: visib[y][x]=1; height=grove[y][x]
        
    height=-1
    for y in reversed(range(len(grove[x]))):
        if grove[y][x]>height: visib[y][x]=1; height=grove[y][x]
        

#print(visib)
total=0
for y in visib:
    #print(y)
    total+=y.count(1)
    
print(total)
        


# In[ ]:




