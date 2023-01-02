#!/usr/bin/env python
# coding: utf-8

# In[54]:


grove=[]
score=[]
with open('Day8Input.txt','r') as file:
    for line in file:
        row=[]
        scorerow=[]
        for digit in line.rstrip():
            row.append(int(digit))
            scorerow.append(0)
        grove.append(row)
        score.append(scorerow)
#print(grove)
#print(visib)

maxscore=0
besttree=0,0
for y in range(len(grove)):
    for x in range(len(grove[y])):
        height=grove[y][x]
        score=1
        
        sighttop=-1
        subscore=0
        for y2 in range(y+1,len(grove)): # Look South
            if grove[y2][x]<=height: subscore+=1
            if grove[y2][x]>=height: break
        score=score*subscore
        #print(height,score)
        
        sighttop=-1
        subscore=0
        for y2 in reversed(range(y)): # Look North
            if grove[y2][x]<=height: subscore+=1
            if grove[y2][x]>=height: break
        score=score*subscore
        #print(height,score)
        
        sighttop=-1
        subscore=0
        for x2 in range(x+1,len(grove)): # Look East
            if grove[y][x2]<=height: subscore+=1
            if grove[y][x2]>=height: break
        score=score*subscore
        #print(height,score)
        
        sighttop=-1
        subscore=0
        for x2 in reversed(range(x)): # Look West
            if grove[y][x2]<=height: subscore+=1
            if grove[y][x2]>=height: break
        score=score*subscore
        
        if score>maxscore: maxscore=score; besttree=y,x;#print(height,score,y,x,maxscore)
        
print (maxscore, besttree)
if maxscore<=3420: print("Something's not right")
#    height=-1
#    for x in reversed(range(len(grove[y]))):
#        if grove[y][x]>height: visib[y][x]=1; height=grove[y][x]
        
        
#for x in range(len(grove[0])):
#    height=-1
#    for y in range(len(grove[x])):
#        if grove[y][x]>height: visib[y][x]=1; height=grove[y][x]
#        
#    height=-1
#    for y in reversed(range(len(grove[x]))):
#        if grove[y][x]>height: visib[y][x]=1; height=grove[y][x]
        

#print(visib)
#total=0
#for y in visib:
#    #print(y)
#    total+=y.count(1)
    
#print(total)
        


# In[ ]:




