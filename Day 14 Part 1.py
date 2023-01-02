#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time
from IPython.display import clear_output

def minmax(values):
    xlist=[]; ylist=[]
    for line in values:
        for x,y in line:
            xlist.append(x)
            ylist.append(y)
    minx=min(xlist)
    miny=min(ylist)
    maxx=max(xlist)
    maxy=max(ylist)
    return(minx,miny,maxx,maxy)

def scanshift(scan):
    minx, miny, maxx, maxy = minmax(scan)
    offsetx=minx-1
    offsety=0;#miny-1
    for row in range(len(scan)):
        for val in range(len(scan[row])):
            x,y=scan[row][val]
            x-= offsetx
            y-= offsety
            scan[row][val]=[x,y]

    return(scan, offsetx, offsety)

def makegrid(scanline):
    minx,miny,maxx,maxy=minmax(scanline)
    grid=[]
    for row in range (maxy+1):
        gridrow=[]
        for col in range (maxx+1):
            gridrow.append('.')
        grid.append(gridrow)
        
    for line in scanline:
        for n in range(len(line)-1):
            x1,y1=line[n]; x2,y2=line[n+1];
            grid[y1][x1]='#';grid[y2][x2]='#'
            if x1==x2:
                for y in range(min(y1,y2),max(y1,y2)):
                    grid[y][x1]='#'
                    #print('vert',x1,y)
                    
            if y1==y2:
                for x in range(min(x1,x2),max(x1,x2)):
                    grid[y1][x]='#'
                    #print('hori',x,y1)
    return(grid)
    

    
    
def dropsand(grid,sandpoint):
    sx=sandpoint[0]; sy=sandpoint[1]
    pour=False
    while 1:
        if sy+1==len(grid):pour=True;break
        if grid[sy+1][sx]=='.':          sy+=1; continue
        if grid[sy+1][sx-1]=='.': sx-=1; sy+=1; continue
        if grid[sy+1][sx+1]=='.': sx+=1; sy+=1; continue
        else: break
    grid[sy][sx]='o'
    #print('landed at ',sx,sy)
    #printgrid(grid)
    
    return(grid,pour)
        
    
def printgrid(grid):
    for line in grid:
        for col in line:
            print(col,end="")
        print()
    return()

scanline=[]
with open('Day14Input.txt','r') as file:
    for line in file:
        line=line.rstrip()
        wall=line.split(' -> ')
        wallline=[]
        for n in range(len(wall)):
            x=int(wall[n].split(',')[0]); y=int(wall[n].split(',')[1])
            wallline.append([x,y])
        scanline.append(wallline)

       
#print(scanline)

scan, offsetx, offsety = scanshift(scanline)
#print(scan)
grid=makegrid(scan) 


sandpoint=[500,0]
sandpoint= [sandpoint[0]-offsetx,sandpoint[1]-offsety]
grid[sandpoint[1]][sandpoint[0]]='+'

counter=0
while 1:#contained==True:
    counter+=1
    if counter>2001: break
    
    grid,pour=dropsand(grid,sandpoint)
    if pour==True: total=counter-1;break
    #if counter in [1,100,1000]:
    clear_output(wait=True)
    sleeper=2
    time.sleep(.01)
    printgrid(grid);print();print();print()
    
    
    
    

print(total)
                         


# In[7]:


print(counter)


# In[ ]:




