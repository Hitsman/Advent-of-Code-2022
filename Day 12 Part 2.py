#!/usr/bin/env python
# coding: utf-8

# In[1]:


def startpos(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]=='S': return(row,col)
    return()

def options (grid, row, col, height):
    options=[]
    for y,x in [[row-1,col],[row,col-1],[row+1,col],[row,col+1]]:
#        print('YX ' + str(y),str(x))
        if y<0 or x<0 or y>=len(grid) or x>=len(grid[0]): continue
#        print('Pass Edge')
        if grid[y][x]=='.': continue
        if grid[y][x]=='E' and height<ord('z'): continue
#        print('Pass Dot', height)
#        print(row,col," ",y,x, ' ', grid[y][x],height)
        if ord(grid[y][x])-height>1: continue
#        print('Pass height')
        options.append([y,x])
#    print(options)
    return(options)

def printgrid(grid):
    for row in range(18,23):
        for col in range(0,4):
            print(grid[row][col],end='')
        print()
    return()

grid=[]
with open('Day12Input.txt','r') as file:
    for line in file:
        line=line.rstrip()
        row=[]
        for character in line:
            row.append(character)
        #print(row)
        grid.append(row)



row,col=startpos(grid)
paths=[[[row,col]]]
#paths=[[[0, 0], [1, 0]],[[0, 0], [0, 1]]]
heights=[ord('a')]
done=False
counter=0

while done==False:
    counter+=1
    if counter%1000==0:
        print(counter, len(paths))
#    print(paths)
#    printgrid(grid)
#    print(heights)
    route=paths.pop(0)
    
    height=heights.pop(0)
    #print('route' + str(route))
    row=route[-1][0]; col=route[-1][1]
    grid[row][col]='.'
    directions=options(grid, row, col, height)
#    print(directions)
    for pos in directions:
        y=pos[0]; x=pos[1]
        current=route.copy()
        current.append([y,x])
        if grid[y][x]=='E': done=True; finished=current.copy(); break
        
        paths.append(current)
        #print("current",current)
        #print('paths' , paths)
        heights.append(ord(grid[y][x]))
        grid[y][x]='.'
        
        
        
        
        
print(len(finished)-1)
#print(finished)


# In[ ]:




