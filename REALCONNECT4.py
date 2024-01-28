from graphics import *

win = GraphWin("Connect Four", 700, 650)
win.setBackground('blue')

# to generate 7x6 board
board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]] 

ROW_COUNT = 6
COLUMN_COUNT = 7

def getverts(board):
    verts = []
    for x in range(len(board[0])):
        vert = []
        for y in range(len(board)):
            vert.append(board[y][x])
        verts.append(vert)
    return verts

def get_col(board):
    invalid = Text(Point(350, 30), "That column is full! ")
    invalid.setSize(20)
    drawcount = 0
    while True:
        click = win.getMouse()
        col = int(click.getX()) // 100
        verts = getverts(board)
        if 0 in verts[col]:
            invalid.undraw()
            drawcount = 0
            return col
        else:
            if drawcount == 0:
                invalid.draw(win)

            drawcount += 1

def place_disk(color):
    for y in range(5, -1, -1):
        if board[y][col] == 0:
            circle = Circle(Point((col*100)+50, (y*100)+100), 40).draw(win)
            circle.setFill(color)
            if color == 'red':
                board[y][col] = 1
            if color == 'yellow':
                board[y][col] = 2
            break

def winning_move(board, piece):
    # check rows
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # check cols
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # check diags 
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # check other diags
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

#change winning move to look for all lengths of pieces
#and if there's a length of 4 then win
#then this would be the new evaluate() lol



# draws the board
for y in range(len(board)):
    for x in range(len(board[y])):
        circle = Circle(Point((x*100)+50, (y*100)+100), 40).draw(win)
        circle.setFill('white')

#starts the actual gameplay
while True:
    col = get_col(board)
    place_disk('red')
    if winning_move(board, 1) == True:
        text = Text(Point(350, 30), "RED WINS").draw(win)
        text.setSize(20)
        break
    print(board)

    col = get_col(board)
    place_disk('yellow')
    if winning_move(board, 2) == True:
        text = Text(Point(350, 30), "YELLOW WINS").draw(win)
        text.setSize(20)
        break
    

win.getMouse()

def evaluate(board): #where positive is good for red?
    pass

def minimax(board, depth, maximizingPlayer):
    if depth == 0: # or game over?
        return evaluate(board)
    pass
