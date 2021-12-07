import sys

drawn_num = [ int(x) for x in sys.stdin.readline().split(",") ]
raw_data = sys.stdin.readlines()[1:]
size_data = len(raw_data)
size_bingo_card = 5
marked = "-1"

def bingo_check(bingo_card):
    vert_bingo = []
    for k in range(0,size_bingo_card):
        vert_bingo.append([])
    for i,row in enumerate(bingo_card):
        #print(row)
        #test = [ int(x) for x in row ]
        #print(test)
        if sum(row) == -size_bingo_card:
            return True
        if marked in row:
            for item in row:
                if item == marked:
                    vert_bingo[i] = int(item)
    for col in vert_bingo:
        if sum(col) == -size_bingo_card:
            return True
    return False

data = []
for line in raw_data:
    new_line = []
    for item in line.split(" "):
        if item != " ":
            new_item = int(item)
            new_line.append(new_item)
    data.append(new_line)
print(data)
'''
#get matrices with bingo cards
cards, card = [], []
for index,line in enumerate(data):
    if '\n' != line:
        #card.append(line)
        temp = [ x for x in line.split(" ") ]
        temp[-1] = temp[-1].strip('\n')
        print(temp)
        card.append(temp)
    if '\n' == line or index == size_data - 1:
        cards.append(card)
        card = []

#play bingo
play_bingo = True
#while play_bingo:
for i,number in enumerate(drawn_num):
    print(i,number)
    if i == 12:
        break
    for bingo_card in cards:
        for index, row in enumerate(bingo_card):
            if number in row:
                for j,item in enumerate(row):
                    #print(j,item,number)
                    if item == number:
                        row[j] = marked
                bingo_card[index] = row        

    if i >= size_bingo_card:
        #do bingo check for each card
        for card in cards:
            play_bingo = bingo_check(card)

print(cards)
'''