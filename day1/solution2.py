import sys

data = [int(x) for x in sys.stdin.readlines()]
increased = 0
summation = sum(data[0:3])

for i,num in enumerate(data):
    num = sum(data[i:i+3])
    
    if summation<num:
        increased+=1
    summation = num

print(increased)