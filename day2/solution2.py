import sys

data = sys.stdin.readlines()
hor = 0
depth = 0
aim = 0

for line in data:
    num = int(line.split(" ")[1])
    if "forward" in line:
        hor+=num
        depth += num*aim
    elif "down" in line:
        aim+=num
    elif "up" in line:
        aim-=num 

print(hor*depth)