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
    if set([coord['x0'], coord['y0']]) == set([coord['x1'], coord['y1']]):
        #print('yes! diag')
        same = True
    elif set([coord['x0'], coord['x1']]) == set([coord['y0'], coord['y1']]):
        same = True
    else:
        for index,label in enumerate(['x','y']):
            values = set()
            for i in range(2):
                values.add(coord[label+str(i)])
            if len(values)==1:
                #print('yes! hor/vert')
                same = True
    
    if same:
        print(coord)
        x0,x1 = [coord['x0'], coord['x1']]
        y0,y1 = [coord['y0'], coord['y1']]
        if x0 == y1 and x1 == y0:
            print('transpose case')
            if x0 > x1:
                start = x1
                end = x0
            else:
                start = x0
                end = x1
            for i in range(start,end+1):
                print(i,end)
                if (i,end) not in coords.keys():
                    coords[(i,end)] = 0
                coords[(i,end)] +=1
                end -= 1
        elif x0 == y0 and x1 == y1:
            print('yes')
            for k in range(x0,x1+1):
                print(k,k)
                if (k,k) not in coords.keys():
                    coords[(k,k)] = 0
                coords[(k,k)] +=1
        else:
            x0,x1 = sorted([coord['x0'], coord['x1']])
            y0,y1 = sorted([coord['y0'], coord['y1']])
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    print(x,y)
                    if (x,y) not in coords.keys():
                        coords[(x,y)] = 0
                    coords[(x,y)] +=1

#look for at least two or more tuples
print(len([x for x in coords.values() if x>1]))