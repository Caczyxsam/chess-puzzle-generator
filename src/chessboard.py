import pygame
import GUI

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60
# Game variables

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (6,7)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# the turn comes from the puzzle data
if GUI.turn == "w":
    turn_step = 0
else: turn_step = 2

#load game piece images
white_king = pygame.image.load('assets/white_king.png')
white_king = pygame.transform.scale(white_king, (70, 70))

white_queen = pygame.image.load('assets/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (70, 70))

white_rook = pygame.image.load('assets/white_rook.png')
white_rook = pygame.transform.scale(white_rook, (70, 70))

white_bishop = pygame.image.load('assets/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (70,70))

white_knight = pygame.image.load('assets/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (75,75))

white_pawn = pygame.image.load('assets/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65,65))


black_king = pygame.image.load('assets/black_king.png')
black_king = pygame.transform.scale(black_king, (70, 70))

black_queen = pygame.image.load('assets/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (70, 70))

black_rook = pygame.image.load('assets/black_rook.png')
black_rook = pygame.transform.scale(black_rook, (70, 70))

black_bishop = pygame.image.load('assets/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (70,70))

black_knight = pygame.image.load('assets/black_knight.png')
black_knight = pygame.transform.scale(black_knight, (75,75))

black_pawn = pygame.image.load('assets/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65,65))


white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
puzzle_over = False #Mieti miten tämä ratkaistaan!

# draw the board
def draw_board():
    for i in range(32):
        row = i // 4
        column = i % 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'gold', [600 - (column * 200 ), row * 100, 100, 100])
        else: 
            pygame.draw.rect(screen, 'gold', [700 - (column * 200 ), row * 100, 100, 100])

# draw the pieces from the FEN
def draw_pieces():    
    row_number = 0
    for i in GUI.all_rows:
        column_number = 0
        for j in i:
            if j == "white_pawn":
                screen.blit(white_pawn, (17 + column_number * 100, 17 + row_number * 100))
            if j == "black_pawn":
                screen.blit(black_pawn, (17 + column_number * 100, 17 + row_number * 100))
            if j == "white_knight":
                screen.blit(white_knight, (17 + column_number * 100, 17 + row_number * 100))
            if j == "black_knight":
                screen.blit(black_knight, (17 + column_number * 100, 17 + row_number * 100))
            if j == "white_bishop":
                screen.blit(white_bishop, (17 + column_number * 100, 17 + row_number * 100))
            if j == "black_bishop":
                screen.blit(black_bishop, (17 + column_number * 100, 17 + row_number * 100))
            if j == "white_rook":
                screen.blit(white_rook, (17 + column_number * 100, 17 + row_number * 100))
            if j == "black_rook":
                screen.blit(black_rook, (17 + column_number * 100, 17 + row_number * 100))
            if j == "white_queen":
                screen.blit(white_queen, (17 + column_number * 100, 17 + row_number * 100))
            if j == "black_queen":
                screen.blit(black_queen, (17 + column_number * 100, 17 + row_number * 100))
            if j == "white_king":
                screen.blit(white_king, (17 + column_number * 100, 17 + row_number * 100))
            if j == "black_king":
                screen.blit(black_king, (17 + column_number * 100, 17 + row_number * 100))
            column_number += 1
        row_number += 1


#Temporary main
run = True
while run:
    timer.tick(fps)
    screen.fill("silver")
    draw_board()
    draw_pieces()
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # WORK ON MOVING THE PIECES STARTS HERE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)


    pygame.display.flip()
pygame.quit()

