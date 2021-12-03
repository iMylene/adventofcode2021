import sys

data = [ "".join(x.split()) for x in sys.stdin.readlines() ]
total_num = len(data)
num_size = len(data[0])
oxygen = []
co2 = []

oxygen_indices_ignore_list = []
co2_indices_ignore_list = []

one_indices_list = []
zero_indices_list = []

#find binary for oxygen
for i in range(num_size):
    for j in range(total_num):
        if j in oxygen_indices_ignore_list:
            continue
        elif int(data[j][i]) == 1:
            one_indices_list.append(j)
        elif int(data[j][i]) == 0:
            zero_indices_list.append(j)
    
    if len(zero_indices_list) > len(one_indices_list):
        oxygen_indices_ignore_list.extend(one_indices_list)
    else:
        oxygen_indices_ignore_list.extend(zero_indices_list)

    one_indices_list = []
    zero_indices_list = []

    if total_num - 1 == len(oxygen_indices_ignore_list):
        break
oxygen = data[(list(set([x for x in range(total_num)]) - set(oxygen_indices_ignore_list)))[0]]

#find binary for co2
for i in range(num_size):
    for j in range(total_num):
        if j in co2_indices_ignore_list:
            continue
        elif int(data[j][i]) == 1:
            one_indices_list.append(j)
        elif int(data[j][i]) == 0:
            zero_indices_list.append(j)
    
    if len(zero_indices_list) > len(one_indices_list):
        co2_indices_ignore_list.extend(zero_indices_list)
    else:
        co2_indices_ignore_list.extend(one_indices_list)

    one_indices_list = []
    zero_indices_list = []

    if total_num - 1 == len(co2_indices_ignore_list):
        break
co2 = data[(list(set([x for x in range(total_num)]) - set(co2_indices_ignore_list)))[0]]

#turn binary to int
oxygen_int = int("".join(oxygen),2)
co2_int = int("".join(co2),2)
life_support = oxygen_int * co2_int

print(life_support)