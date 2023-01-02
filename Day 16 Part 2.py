#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


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
            words=line.split(' ')
            paths=line.split('valve')[1].split(' ')
            parsedpaths=[]
            for tunnel in paths:
                if ',' in tunnel: tunnel=tunnel.replace(',','')
                if tunnel.isupper():parsedpaths.append(tunnel)
            parsedpaths.append('v')
            
            valves[words[1]]=[int(words[4].split('=')[1].replace(';','')),parsedpaths,n]
            n+=1
    
    return(valves)

# [CurrentRoomHuman, CurrentRoomElephant,Rate,Score,Valves,OptionsHuman, OptionsElephant]
def runattempt(valves,attempt):
#print(timeleft,attempt)
    newattempts=[]
    
    releif=attempt[3] + attempt[2]
    
    OptionsHuman=attempt[5]
    OptionsElephant=attempt[6]
    
    for option1 in attempt[5]:
        valveindex1=valves[attempt[0]][2]   #gets the valve position in the open/close table
        if option1 =='v' and attempt[4][valveindex1]==False:break
        
        for option2 in attempt[6]:
            newvalves=attempt[4][:]
            rate=attempt[2]
            history=attempt[7][:]
            subhistory=[]
            valveindex2=valves[attempt[1]][2]   #gets the valve position in the open/close table
            if option2 =='v' and attempt[4][valveindex2]==False:break
            
            if option1 =='v' and option2 =='v'and attempt[0]==attempt[1]: break
            humanroom=attempt[0]    
            elephantroom=attempt[1]    
            
            if option1.isupper():               
                newoptions1=valves[option1][1]
                humanroom=option1
                subhistory.append(humanroom)
            if option2.isupper():               
                newoptions2=valves[option2][1]
                elephantroom=option2
                subhistory.append(elephantroom)
                    
                    

            if option1 =='v':
                newvalves[valveindex1]=False #sets valve to closed
                rate+=valves[attempt[0]][0]
                newoptions1=valves[humanroom][1]
                subhistory.append(humanroom+'valve')
                
            if option2 =='v':
                newvalves[valveindex2]=False #sets valve to closed
                rate+=valves[attempt[1]][0]
                newoptions2=valves[elephantroom][1]
                subhistory.append(elephantroom+'valve')
                
            if valves[humanroom][2]>valves[elephantroom][2]:
                g=humanroom
                humanroom=elephantroom
                elephantroom=g
            history.append(subhistory)    
            newattempt=([humanroom,elephantroom,rate,releif,newvalves,newoptions1,newoptions2,history])
            newattempts.append(newattempt)       
        
    return(newattempts)

def main():
    valves=reader(16,'i')
    #print(valves)
    valvelist=[]
    for valve in valves:
        #print(valves[valve][0])
        if valves[valve][0]==0:valvelist.append(False)
        else: valvelist.append(True)
    firstvalveroom='AA'#list(valves.keys())[0]
    print(firstvalveroom)
    options=valves[firstvalveroom][1]
    #options.append('v')
    attempts=[[firstvalveroom,firstvalveroom,0,0,valvelist,options,options,[]]]
    
    timeleft=26

    #print(valvelist)
    minute=0
    while timeleft>0:
        minute+=1
        newattempts=[]
        print(timeleft, len(attempts))
        for attempt in attempts:
            #if 0:
            #    continue
            if not any(attempt[4]):
                attempt[5]=['AA']
                attempt[6]=['AA']
                
                
                #print(attempt)
                #runattempts=['AA','AA',attempt[2],score,attempt[4],['AA'],['AA']]
                #print(runattempts)
            runattempts=runattempt(valves,attempt)
            for run in runattempts:
                if run not in newattempts:  newattempts.append(run)
        #for state in newattempts:
            
        newattempts.sort(key=lambda x: (x[3],x[2]),reverse=True)
        #newattempts.reverse
#        print(minute,newattempts[0][0:3])
        if len(newattempts)>10000:
        attempts.sort(key=lambda x: (x[0],x[1]))
        while n < range(len(attempts)):
            first=n
            while attempts[n][0],attempts[n][1]==attempts[n+1][0],attempts[n+1][1]:
                n+=1
            
            if a[0]==b[0]:
                if a[1]==b[1]:
                    if a
            
            attempts=newattempts[0:10000]
        else:attempts=newattempts
        
        timeleft-=1
    attempts.sort(key=lambda x: (x[0],x[1]))
    for attempt in attempts[0:1]:
        print(attempt[0:8])
    
    #2821 is too high
    #2456 is too low
main()


# In[ ]:





# In[ ]:




