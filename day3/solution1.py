import sys

data = [ "".join(x.split()) for x in sys.stdin.readlines() ]
gamma = []
eps = []

#make dict with empty list
col = {}
col_size = len(data[0])
for i in range(col_size):
    col[i] = []

#fill dict with col num
for line in data:
    for i,num in enumerate(line):
        col[i].append(num)

#search for gamma/eps binary number
for i in range(col_size):
    if col[i].count('1') > col[i].count('0'):
        gamma.append('1')
        eps.append('0')
    else:
        gamma.append('0')
        eps.append('1')

#turn binary to int
gamma_int = int("".join(gamma),2)
eps_int = int("".join(eps),2)
power = gamma_int * eps_int

print(power)