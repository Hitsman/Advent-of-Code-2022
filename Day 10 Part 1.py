#!/usr/bin/env python
# coding: utf-8

# In[16]:


def checkcycle(cycle,x):
    timing=False
    if cycle in [20,60,100,140,180,220]: timing=True
    return(timing)



x=1
cycle=1
values=[]

with open('Day10Input.txt','r') as file:
    for line in file:
        if "noop" in line.rstrip():
            if checkcycle(cycle,x): values.append(x*cycle)
            cycle+=1 #end of cycle
        if "addx" in line.rstrip():
            if checkcycle(cycle,x): values.append(x*cycle)
            cycle+=1
            command=line.rstrip().split(' ')
            if checkcycle(cycle,x): values.append(x*cycle)
            x+=int(command[1])
            cycle+=1
            
        #print(cycle,x, line.rstrip())
#print(values)
print(sum(values))


# In[ ]:




