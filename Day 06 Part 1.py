#!/usr/bin/env python
# coding: utf-8

# In[29]:


groupsize=14
with open('Day6Input.txt','r') as file:
    for line in file:
        received=line.rstrip()
#print(len(received))

for position in range(len(received)):
    group=[]
    #print(position)
    for letters in range(groupsize):
        if received[position+letters] in group: 
            #print(group)
            break
        else: group.append(received[position+letters])
        
    if len(group)==groupsize:
        print(position+groupsize, received[position+0:position+groupsize])
        break
    
#if position+4==1757: print('Correct!')


# In[ ]:




