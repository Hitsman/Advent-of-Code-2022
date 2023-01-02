#!/usr/bin/env python
# coding: utf-8

# In[73]:


def printthis (evaluated):
    for line in evaluated:
        print(line)
    print();print();print();
    return()


def compare(left,right,decision):
    if decision!=0: return(decision)

    length=min(len(left),len(right))
    for pos in range(length):
        if decision!=0: return(decision)
        l=left[pos]; r=right[pos]
        #print(l,r)
        if l==r:continue
        if isinstance(l, int) and isinstance(r, int):
            
            if l<r: decision=-1
            else: decision=1
            #print('both ints',decision)
            break
        if isinstance(l, list) and isinstance(r, list):
            #print('bothlists ',l,'   ',r);
            decision=compare(l,r,decision);break
        if isinstance(l, int):l=[l];                    decision=compare(l,r,decision);break
        if isinstance(r, int):r=[r];                    decision=compare(l,r,decision);break

        
        #print(l,r)
    if decision==0:
        if isinstance(left, list) and isinstance(right, list):
            #print('still bothlists ',left,'   ',right)
            if len(left)<len(right): decision=-1
            if len(left)>len(right): decision=1
            #else: decision=1
    return(decision)


codes=[]
with open('Day13Input.txt','r') as file:
    for line in file:
        line=line.rstrip()
        if line=="": continue
        codes.append(line)

evaluated=[[[2]],[[6]]]
#evaluated=[]
for code in codes:
    evaluated.append(eval(code))

    
    
ordered=[]
counter=0

bubble=True
while bubble==True:
    counter+=1
    if counter>2000: break
    #if counter>0: printthis(evaluated)
    if counter>1995: 
        for n in range(len(evaluated)):
            if evaluated[n]==[[2]] or evaluated[n]==[[6]]:
                print(n)
        print()
                
                
    bubble=False
    for n in range(len(evaluated)-1):
        decision=0
        #print(n)
        left=evaluated[n]; right=evaluated[n+1]
        #print(left,right)
        decision=compare(left,right,decision)
        #print('decision',decision)
        if decision==1:
            #print(left,'      ',right)
            evaluated[n]=right
            evaluated[n+1]=left
            bubble=True
        
    

#printthis(evaluated)
            
#print(ordered)
total=1    
for n in range(len(evaluated)):
    if evaluated[n]==[[2]] or evaluated[n]==[[6]]:
        total=total*(n+1)

print(total)
#print();print();print()
#for pair in pairs:print(pair)

print('DONE')


# In[ ]:





# In[ ]:




