#!/usr/bin/env python
# coding: utf-8

# In[32]:


import time


def reader(day,inputorsample):
    if inputorsample=='i': word='Input'
    if inputorsample=='s': word='Sample'
    sensorlist=[]
    beaconlist=[]
    
    filename='Day'+str(day)+str(word)+'.txt'
    with open(filename,'r') as file:
        for line in file:
            line=line.rstrip()
            words=line.split(' ')
            sensor=[int(words[2].split('=')[1].replace(',',''))   ,   int(words[3].split('=')[1].replace(':',''))]
            beacon=[int(words[8].split('=')[1].replace(',',''))   ,   int(words[9].split('=')[1])]
            sensorlist.append(sensor)
            beaconlist.append(beacon)
    
    return(sensorlist,beaconlist)


def main():
    sensors,beacons=reader(15,'i')
    distances=[]
    for n in range(len(beacons)):
        distances.append(abs(beacons[n][0]-sensors[n][0])+abs(beacons[n][1]-sensors[n][1]))
    ymax=4000000
    y=0
    while y<ymax:
        if y%100000==0: print(y)
        minmax=[]
        for n in range(len(sensors)):
            strength=distances[n]-abs(sensors[n][1]-y)
            if strength>=0:
                minmax.append([max(0,sensors[n][0]-strength),min(ymax,sensors[n][0]+strength)])
        
        
        minmax.sort(key=lambda x: x[0])
        #print(y,minmax)
        coverage=minmax[0]
        for a in minmax:
            
            if a[0]<=coverage[1]+1:
                if a[1]>coverage[1]:coverage[1]=a[1]
                else:continue
            
            else:
                answer=4000000*(a[0]-1)+y
                print('opening',a[0]-1,y);break
        
            #print(coverage)
        y+=1
        

  
    print()        
    print('Answer='answer)
    #print(distances)
    #print(covered)

    #print(sensors,beacons)
    #for n in range(len(sensors)): print(n,sensors[n],distances[n])
    
start=time.time()    
main()
print(time.time()-start)


# In[ ]:




