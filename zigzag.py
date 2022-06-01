numRows = 4
name="GAJANANMUDALIAR"

direction = True
index = 0
for i in range(len(name)):
    "nam"+str(i) += name[i]
    if index == numRows - 1:
        direction = False
    elif index == 0:
        direction = True
    
    if direction == True:
        index += 1
    else:
        index -= 1