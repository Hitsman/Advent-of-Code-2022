#!/usr/bin/env python
# coding: utf-8

# In[50]:


def compare(left,right,decision):
    if decision!=0: return(decision)

    length=min(len(left),len(right))
    for pos in range(length):
        if decision!=0: return(decision)
        l=left[pos]; r=right[pos]
        #print(l,r)
        if l==r: continue
        if isinstance(l, int) and isinstance(r, int):
            
            if l<r: decision=-1
            else: decision=1
            #print('both ints',decision)
            break
        if isinstance(l, list) and isinstance(r, list): decision=compare(l,r,decision);break
        if isinstance(l, int):l=[l];                    decision=compare(l,r,decision);break
        if isinstance(r, int):r=[r];                    decision=compare(l,r,decision);break

        
        #print(l,r)
    if decision==0:
        if isinstance(left, list) and isinstance(right, list):
            if len(left)<len(right): decision=-1
            else: decision=1
    return(decision)


pairs=[]
pair=[]
with open('Day13Input.txt','r') as file:
    for line in file:
        line=line.rstrip()
        
        if line !="": pair.append(line)
        if line=="": pairs.append(pair);pair=[]
        
pairs.append(pair);pair=[]

order=[]

for left,right in pairs:
    decision=0
    left=eval(left); right=eval(right)
    decision=compare(left,right,decision)
    print('Pair ',decision)
    order.append(decision)


            
print(order)
total=0    
for pos in range(len(order)):
    if order[pos]==-1: total+=(pos+1)
print(total)



#print();print();print()
#for pair in pairs:print(pair)

print('DONE')


# In[ ]:




