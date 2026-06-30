import pygame
import GUI
import itertools

# Game variables
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60

# Pieces and their places
white_pieces = []
white_locations = []
black_pieces = []
black_locations = []

##### Adding the pieces to their places#####
for row, line in enumerate(GUI.all_rows):
    for col, cell in enumerate(line):
        coord = (col, 7 - row)
        if cell.startswith("white_"):
            white_pieces.append(cell.replace("white_", ""))
            white_locations.append(coord)
        elif cell.startswith("black_"):
            black_pieces.append(cell.replace("black_", ""))
            black_locations.append(coord)


# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# the starting turn comes from the puzzle data
if GUI.turn == "w":
    turn_step = 0
else: turn_step = 2

# load game piece images
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

##### Draw the board #####
def draw_board():
    for i in range(32):
        row = i // 4
        column = i % 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'gold', [600 - (column * 200 ), row * 100, 100, 100])
        else: 
            pygame.draw.rect(screen, 'gold', [700 - (column * 200 ), row * 100, 100, 100])

##### Draw the pieces from the FEN #####
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        x = white_locations[i][0]
        y = 7 - white_locations[i][1]        # flip logical y back to screen row
        screen.blit(white_images[index], (17 + x * 100, 17 + y * 100))
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        x = black_locations[i][0]
        y = 7 - black_locations[i][1]
        screen.blit(black_images[index], (17 + x * 100, 17 + y * 100))

##### Checking valid move options for all the pieces #####
def check_options(pieces, locations, turn): 
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)): ###CHECK
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)

    return all_moves_list


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


def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check valid moves on screen
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else: 
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

print(f"The turn step is {turn_step}")

# Temporary main
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
            y_coord = 7 - (event.pos[1] // 100)
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
                        white_piece = white_locations.index(click_coords) # taking a white piece as black
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

    pygame.display.flip()
pygame.quit()