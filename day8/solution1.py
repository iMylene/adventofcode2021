import sys

data = [ x.split(" | ")[1].strip("\n").split() for x in sys.stdin.readlines() ]

segment_one = 2
segment_four = 4
segment_seven = 3
segment_eight = 7
correct_segments = [segment_one, segment_four, segment_seven, segment_eight]

counter = 0
for line in data:
    for pattern in line:
        if len(pattern) in correct_segments:
            counter += 1
print(counter)