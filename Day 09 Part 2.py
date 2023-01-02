#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def display(knotsx,knotsy):
    display=[]
    for n in range(25):
        display.append(['.']*26)
        
    #display[5][2]=str(8)
    for knot in range(len(knotsx)):
        #print(knotsy[knot] ,knotsx[knot])
        display[knotsy[knot]] [knotsx[knot]]=str(knot)
    
    for line in reversed(range(len(display))): print(display[line],line)
    print()
    return()


motion=[]
with open('Day9Input.txt','r') as file:
    for line in file:
        motion.append(line.rstrip().split(' '))
headx=0; heady=0
dict={'R':[1,0],'L':[-1,0],'U':[0,1],'D':[0,-1],}
knotsx=[0]*10;knotsy=[0]*10;
tailtrail=[[0,0]]


for direction,steps in motion:
    for n in range(int(steps)):
        knotsx[0]+=dict[direction][0] ; knotsy[0]+=dict[direction][1]
        for knot in range(1,len(knotsx)):
            xdiff=knotsx[knot-1]-knotsx[knot]
            ydiff=knotsy[knot-1]-knotsy[knot]
            
            if abs(xdiff)==2 and abs(ydiff)==0:
                knotsx[knot]+=int((xdiff)/2)
                
            if abs(xdiff)==0  and abs(ydiff)==2:
                knotsy[knot]+=int((ydiff)/2)
            
            if abs(xdiff)==2 and abs(ydiff)==1:
                knotsx[knot]+=int((xdiff)/2)
                knotsy[knot]+=int((ydiff))
                
            if abs(xdiff)==1  and abs(ydiff)==2:
                knotsx[knot]+=int((xdiff))
                knotsy[knot]+=int((ydiff)/2)
                
            if abs(xdiff)==2 and abs(ydiff)==2:
                knotsx[knot]+=int((xdiff)/2)
                knotsy[knot]+=int((ydiff)/2)
                
                
        #print(knotsx);print(knotsy);print()
        #display(knotsx,knotsy)
        if [knotsx[9],knotsy[9]] not in tailtrail: tailtrail.append([knotsx[9],knotsy[9]])
        
#    rope=[]    
#    for knot in range(len(knotsx)):
#        rope.append([knotsx[knot],knotsy[knot]])
#    print(rope)
#    print()


#                (knotsy[knot-1]-knotsy[knot])
#            tail[0]=lasthead[0];tail[1]=lasthead[1]
#            tailtrail.append([tail[0],tail[1]])
#            #print(tail)
#            #print(tailtrail)
            
        
print()
print(len(tailtrail))
tailpositions=list(set(map(tuple,tailtrail)))
print(len(tailpositions))
if len(tailpositions)<=2195: print('Too Low')

#trailx=[]
#traily=[]
#for n in range(len(tailtrail)):
#    trailx.append(tailtrail[n][0])
#    traily.append(tailtrail[n][1])
#display(trailx,traily)


# In[ ]:


for n in range(-4,4,):
    print(n/2,round(n/2))


# In[ ]:




