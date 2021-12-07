import sys
from statistics import median

data = [ int(x) for x in sys.stdin.readline().split(",") ]
final_pos = int(median(data))

fuel = 0
for num in data:
    fuel += abs(num-final_pos)
print(fuel)