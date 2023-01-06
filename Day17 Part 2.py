#!/usr/bin/env python
# coding: utf-8

# In[56]:


import time
starttime=time.time()

def reader(day,inputorsample):
    if inputorsample=='i': word='Input'
    if inputorsample=='s': word='Sample'
    sensorlist=[]
    beaconlist=[]
    
    filename='Day'+str(day)+str(word)+'.txt'
    valves={}
    n=0
    with open(filename,'r') as file:
        for line in file:
            line=line.rstrip()
    
    return(line)

def printeach(thing):
    for each in thing:
        print(each)
    return()

# [CurrentRoomHuman, CurrentRoomElephant,Rate,Score,Valves,OptionsHuman, OptionsElephant]
def rockfun (type,highest):
    if type=='hline': rock=[[0,0],[0,1],[0,2],[0,3]]
    if type=='plus':  rock=[[1,0],[1,1],[1,2],[0,1],[2,1]]
    if type=='revl': rock=[[0,2],[1,2],[2,2],[0,1],[0,0]]
    if type=='vline': rock=[[3,0],[2,0],[1,0],[0,0]]
    if type=='square': rock=[[0,0],[0,1],[1,0],[1,1]]
    newrock=[]
    for piece in rock:
        newpiece=[piece[0]+highest+4,piece[1]+2]
        newrock.append(newpiece)
    return(newrock)
    
    
        
def main():
    highest=0
    lasthighest=0
    puffs=reader(17,'i')
    rockorder=['hline','plus','revl','vline','square']
    pit=[[True ,True ,True ,True ,True ,True ,True]]
    blankline=[False,False,False,False,False,False,False ]
    n=0
    rockno=0
    puffno=0
    highlist=[]
    rocklist=[]
    puffmax=len(puffs)
    print("Puffsmax ", puffmax)
    #pufftogram=[0]*puffmax
    endrock=1000000000000
    while(rockno<endrock):
        if time.time()-starttime>5: break
        #print('puff',puffno)
        #pufftogram[puffno%puffmax]+=1
        if puffno%puffmax==10002 and rockno%len(rockorder)==0: #puffno%puffmax==10002 
            highlist.append(highest)
            rocklist.append(rockno)
            if len(highlist)>3:
                if highlist[2]-highlist[1]==highlist[1]-highlist[0] and rocklist[2]-rocklist[1]==rocklist[1]-rocklist[0]: #Pattern has stabilied
                    print('stabilized')
                    rockstogo=endrock-rockno
                    patternstoskip=rockstogo//(rocklist[2]-rocklist[1])
                    rockno=rockno+patternstoskip * (rocklist[2]-rocklist[1])
                    skippedheight=patternstoskip * (highlist[2]-highlist[1])
                else: highlist.pop();rocklist.pop()
                        
            print(highest,highest-lasthighest, 'rock', rockno)
            lasthighest=highest
        #if n==5000: break
        if len(pit)<highest+10:
            for g in range (10):
                pit.extend([[False]*7])
        #print(len(pit))
        #if rockno==len(rockorder): rockno=0
        rock=rockfun(rockorder[rockno%len(rockorder)],highest)
#        print(rock)
#        print(rockorder[rockno])
        rockmoving=True
        m=0
        while rockmoving==True:
            if m==100: break
            m+=1
            puff=puffs[puffno%puffmax]
            if puff=='>':d=1
            if puff=='<':d=-1
            puffno+=1
            
            
            canmove=True
            for piece in rock:
                if piece[1]+d==7 or piece[1]+d==-1: canmove=False; break   #Check if piece hits wall
                if pit[piece[0]][piece[1]+d]==True:  canmove=False         #Check if piece hits rock
            if canmove==True: 
#                print("moved", puff)  #*************
                for p in range(len(rock)): 
                    rock[p][1]+=d
#            if canmove==False: print('blocked',puff)

            
            canmove=True
            for piece in rock: 
                if pit[piece[0]-1][piece[1]]==True:  canmove=False
                                   
            
            if canmove==False:
                rockmoving=False
#                print('Stopped')
                for piece in rock: 
                    pit[piece[0]][piece[1]]=True
                for level in range(highest,len(pit)):
                    if any(pit[level]): highest=level #*********************
                rockno+=1
#                print('Highest',highest)    
                
            if canmove==True:
#                print("Dropped")
                for p in range(len(rock)):
                    rock[p][0]-=1
            

            #print(rock)
#            if rockmoving==False:
#                for line in reversed(range(len(pit))):
#                    #print(pit[line])
#                    for point in pit[line]:
#                        if point: print('#',end="")
#                        else: print('.',end="")
#                    print('')
                
    #            

    
    
#    for line in reversed(range(len(pit)-20,len(pit))):
#        for point in pit[line]:
#            if point: print('#',end="")
#            else: print('.',end="")
#        print('')
    highest+=skippedheight
    print('Highest',highest)       
    # 1523167155402 is too low
                
    
    #print(pit)
#    for puff in range(len(pufftogram)):
#        print(puff,pufftogram[puff])
main()
print("Done",round(time.time()-starttime,4))


# In[ ]:




