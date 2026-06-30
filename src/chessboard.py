import pygame
import GUI
import itertools

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60
# Game variables

white_pieces = []
white_locations = []

black_pieces = []
black_locations = []
#Piece list

long_piece_list = list(itertools.chain.from_iterable(GUI.all_rows))

for j in long_piece_list:
    if j == "white_pawn":
            white_pieces.append("pawn")
    elif j == "white_knight":
            white_pieces.append("knight")
    elif j == "white_bishop":
            white_pieces.append("bishop")
    elif j == "white_rook":
            white_pieces.append("rook")
    elif j == "white_queen":
            white_pieces.append("queen")
    elif j == "white_king":
            white_pieces.append("king")
    else: white_pieces.append(" ")

for j in long_piece_list:
    if j == "black_pawn":
            black_pieces.append("pawn")
    elif j == "black_knight":
            black_pieces.append("knight")
    elif j == "black_bishop":
            black_pieces.append("bishop")
    elif j == "black_rook":
            black_pieces.append("rook")
    elif j == "black_queen":
            black_pieces.append("queen")
    elif j == "black_king":
            black_pieces.append("king")
    else: 
        black_pieces.append(" ")

#Piece locations
for j in range(8):
    for i in range(8):
        white_locations.append((i % 8, 7 - j % 8))
black_locations = white_locations
print(len(white_locations))

print(len(white_pieces))
print(black_pieces)
print(white_locations)


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

#####Checking valid move options for all the pieces#####
def check_options(pieces, locations, turn): 
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)): ###CHECK
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        '''elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)'''
        all_moves_list.append(moves_list)

    return all_moves_list

#valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

#check valid moves on screen
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else: 
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

print(f"The turn step is {turn_step}")

#Temporary main
white_options = check_options(white_pieces, white_locations, 'white')
black_options = check_options(black_pieces, black_locations, 'black')
run = True
while run:
    timer.tick(fps)
    screen.fill("silver")
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()


    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # WORK ON MOVING THE PIECES STARTS HERE
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords) # taking a black piece as white
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords) # taking a black piece as white
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []



    pygame.display.flip()
pygame.quit()

