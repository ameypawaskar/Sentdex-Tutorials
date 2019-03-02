#List
game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

print("   a  b  c")

'''count = 0
for row in game:
    print(count,row)
    count += 1'''
# OR

for count, row in enumerate(game):
    print(count, row) 
    # For iterating list of list 
    #for item in row:
    #    print(item)
