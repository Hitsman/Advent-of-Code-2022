#!/usr/bin/env python
# coding: utf-8

# In[21]:


motion=[]
with open('Day9Input.txt','r') as file:
    for line in file:
        motion.append(line.rstrip().split(' '))
head=[0,0]
dict={'R':[1,0],'L':[-1,0],'U':[0,1],'D':[0,-1],}
tail=[0,0]
tailtrail=[[0,0]]
lasthead=[0,0]
for direction,steps in motion:
    for n in range(int(steps)):
        lasthead[0]=head[0]; lasthead[1]=head[1]
        
        head[0]+=dict[direction][0] ; head[1]+=dict[direction][1]
        #print(lasthead, head, tail)
        if abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1:
            tail[0]=lasthead[0];tail[1]=lasthead[1]
            tailtrail.append([tail[0],tail[1]])
            #print(tail)
            #print(tailtrail)
            
        
print()
#print(tailtrail)
tailpositions=list(set(map(tuple,tailtrail)))
print(len(tailpositions))


# In[ ]:




