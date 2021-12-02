import sys

data = sys.stdin.readlines()
hor = 0
depth = 0

for line in data:
    num = int(line.split(" ")[1])
    if "forward" in line:
        hor+=num
    elif "down" in line:
        depth+=num
    elif "up" in line:
        depth-=num 

print(hor*depth)