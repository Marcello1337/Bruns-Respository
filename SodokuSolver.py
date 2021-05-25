board=[[0,3,0,0,0,0,0,0,0],
       [0,0,0,1,9,5,0,0,0],
       [0,0,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,0],
       [4,0,0,8,0,0,0,0,1],
       [0,0,0,0,2,0,0,0,0],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,0,0,0,7,0],
    ]

xboard=[[5,3,4,6,7,8,9,1,2],
       [6,7,2,1,9,5,3,4,8],
       [1,9,8,3,4,2,5,6,7],
       [8,5,9,7,6,1,4,2,3],
       [4,2,6,8,5,3,7,9,1],
       [7,1,3,9,2,4,8,5,6],
       [9,6,1,5,3,7,2,8,4],
       [2,8,7,4,1,9,6,3,5],
       [3,4,5,2,8,6,1,7,9],
    ]


yboard = [[7,8,0,4,0,0,1,2,0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


#valid input
#in zeile nicht die Zahl
#in spalte nicht die Zahl
#in block nicht die zahl

#zeile x = for j in 0 bis 8 board[x][j]
#spalte x = for i in 0 bis 8 board[i][x]
#block von punkt board[x][y] x/3=0(,1,2) + R , y/3=(0,1,)2 + R- > block for i in [0*3,1,2] for j in [3*2,7,8]
#Zähle fehlende Einträge, 0en und mache einen Vektor der so lang ist

def in_block(board, x_coord, y_coord, wert):
    x= int(x_coord/3)
    y= int(y_coord/3)
    for i in [x*3, x*3+1, x*3+2]:
        for j in [y*3,y*3+1, y*3+2]:
            if board[i][j] == wert:
                #print(i)
                #print(j)
                return False

    return True



def in_row(board, x_coord, y_coord, wert):
    for j in range(9):
        if board[x_coord][j] == wert:
            #print(x_coord)
            #print(j)
            return False
    return True



def in_column(board, x_coord, y_coord ,wert):
    for i in range(9):
        if board[i][y_coord] == wert:
            #print(i)
            #print(y_coord)
            return False
    return True

def is_valid(board, x_coord, y_coord, wert):
    if in_block(board, x_coord, y_coord, wert) and in_row(board, x_coord, y_coord, wert) and in_column(board, x_coord, y_coord, wert):
        return True
    else:
        return False

def creat_vektor(board):
    vec=[]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                vec.append([i,j])
    return vec


for i in range(9):
    print(board[i])


print("Das Sodoku wird gelöst!")
print("Haben Sie etwas Geduld")
print("---------------------------------------------")


vec=creat_vektor(board)
coord=0

while coord in range(len(vec)):
    wert=board[vec[coord][0]][vec[coord][1]]+1
    k=True
    while wert in range(1, 10) and k==True:
        valid=is_valid(board, vec[coord][0], vec[coord][1], wert)
        if valid == True:
            board[vec[coord][0]][vec[coord][1]]=wert
            coord=coord+1
            k=False
        else:
            wert +=1
    if wert not in range(1,10):
        board[vec[coord][0]][vec[coord][1]]=0
        coord = coord-1

if coord==-1:
    print("Das Sodoku hat keine Lösung")

else:
    print("Die Lösung wurde gefunden")
    for i in range(9):
      print(board[i])





