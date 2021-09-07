# Driver file handling userinput and display current State of any object
#added this comment here
import pygame as pg
import Engine

width = height = 512
dimension = 8 #8 square and 8 rows

square_size = (width) // dimension
max_fps = 30

Images = {}

def load_pieces():
    pieces = ['wR', 'wB' ,'wK', 'wN', 'wQ', 'wp', 'bR', 'bB', 'bK', 'bN', 'bQ', 'bp']
    for piece in pieces:
        Images[piece] = pg.transform.scale(pg.image.load(piece+".png"),(square_size, square_size))

    """This is my main driver will handle user input and will work on graphics objects"""

def main():
    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    screen.fill(pg.Color('white'))
    gs = Engine.gameState()
    load_pieces() #doing it only once as its a very resource heavy process
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        draw_gameState(screen, gs)
        clock.tick(max_fps)
        pg.display.flip()
def draw_gameState(screen, gs):
    drawboard(screen)
    draw_pieces(screen, gs.board)    

def drawboard(screen):
    colors = [pg.Color('#ffe9af'), pg.Color('#537c49')]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r + c) % 2)]
            # print(color)
            pg.draw.rect(screen, color, pg.Rect(c*square_size, r*square_size, square_size, square_size))
    

def draw_pieces(screen, board):
    for r in range (dimension):
        for c in range (dimension):
            piece = board[r][c]
            if (piece != "--"):
                screen.blit(Images[piece], pg.Rect(c*square_size, r*square_size, square_size, square_size))
                

def move_peices(board, screen):
    pass

def drag_drop(board, screen):
    pass
if __name__ == '__main__':
    main()
