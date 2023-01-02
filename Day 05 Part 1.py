#!/usr/bin/env python
# coding: utf-8

# In[63]:


counter = 0
layers=[]
stacks=([],[],[],[],[],[],[],[],[],[])
stackno=0
with open('Day5Input.txt','r') as file:
    for line in file:
        #line=line.rstrip()
        #print(line)
        if '[' in line:
            layers.append(line)
        if "1   2   3 "in line:
            #print("found it")
            for layer in reversed(layers):
                #print(layer)
                for stackno in range(0,9):
                    #print(layer[(stackno)*4+1],stackno)
                    if layer[(stackno)*4+1] != " ":
                        stacks[stackno+1].append(layer[(stackno)*4+1])
            
            #print(stacks)
            
        if "move" in line:
            command=line.rstrip().split(" ")
            quantity=int(command[1])
            wherefrom=int(command[3])
            whereto=int(command[5])
            #print(quantity,wherefrom,whereto)
            for i in range(quantity):
                stacks[whereto].append(stacks[wherefrom].pop())
            
#print(layers)
for i in stacks:
    if i!=[]:
        print(i.pop(),end="")


# In[ ]:




