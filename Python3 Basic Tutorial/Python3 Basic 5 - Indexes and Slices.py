l = [1, 2, 3, 4, 5]
print("Second Element:",l[1])
print("Fifthe Element:",l[4])
print("Last Element:",l[-1])
print("InBetween Elements:",l[2:4])
l[1] = 99
print("Changed List:",l,"\n")


#List
game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

print("   a  b  c")
game[0][1] = 2

for count, row in enumerate(game):
    print(count, row) 
    