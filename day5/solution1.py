import sys

data = [ x.strip('\n').split(" -> ") for x in sys.stdin.readlines() ]

#search for correct coords
coords = {}
for line in data:
    coord = {}
    for i in range(2):
        for index,label in enumerate(['x','y']):
            coord[label+str(i)] = int(line[i].split(',')[index])
    
    same = False
    for index,label in enumerate(['x','y']):
        values = set()
        for i in range(2):
            values.add(coord[label+str(i)])
        if len(values)==1:
            same = True
    if same:
        x0,x1 = sorted([coord['x0'], coord['x1']])
        y0,y1 = sorted([coord['y0'], coord['y1']])
        for x in range(x0,x1+1):
            for y in range(y0,y1+1):
                if (x,y) not in coords.keys():
                    coords[(x,y)] = 0
                coords[(x,y)] +=1

#look for at least two or more tuples
print(len([x for x in coords.values() if x>1]))