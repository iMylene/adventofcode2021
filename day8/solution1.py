import sys

data = [ x.split(" | ")[1].strip("\n").split() for x in sys.stdin.readlines() ]
segments = [2, 4, 3, 7]
counter = 0
for line in data:
    for pattern in line:
        if len(pattern) in segments:
            counter += 1
print(counter)