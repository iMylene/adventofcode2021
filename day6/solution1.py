import sys

data = map(int, sys.stdin.readline().split(","))
#data = [3]
new_internal = 8
curr_internal = 6
goal = 80

for _ in range(1,goal+1):
    new_data = []
    for fish_internal in data:
        if fish_internal == 0:
            [ new_data.append(x) for x in [curr_internal,new_internal] ]
        else:
            new_data.append(fish_internal-1)
    data = new_data

print(len(data))
#print(data)