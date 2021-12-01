import sys

data = [int(i) for i in sys.stdin.readlines()]
increased = 0

for i,num in enumerate(data):
    if i == 0:
        continue
    else:
        if data[i-1]<num:
            increased+=1

print(increased)