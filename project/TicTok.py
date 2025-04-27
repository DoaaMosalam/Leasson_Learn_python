import pygame as pg
import sys
''' 
Create TicTok game
'''
# Initialize pygame
pg.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
WIN_LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw grid lines
def draw_lines():
    # Horizontal
    pg.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical
    pg.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw figures (X and O)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pg.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                      int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                               CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pg.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pg.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

# Check for winner
def check_win(player):
    # Vertical win
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            pg.draw.line(screen, (255, 0, 0),
                         (col * SQUARE_SIZE + SQUARE_SIZE // 2, 15),
                         (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 15), WIN_LINE_WIDTH)
            return True

    # Horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            pg.draw.line(screen, (255, 0, 0),
                         (15, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                         (WIDTH - 15, row * SQUARE_SIZE + SQUARE_SIZE // 2), WIN_LINE_WIDTH)
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        pg.draw.line(screen, (255, 0, 0), (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        pg.draw.line(screen, (255, 0, 0), (WIDTH - 15, 15), (15, HEIGHT - 15), WIN_LINE_WIDTH)
        return True

    return False

# Restart game
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None

draw_lines()
player = 'X'
game_over = False

# Game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    game_over = True
                player = 'O' if player == 'X' else 'X'
                draw_figures()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                restart()
                player = 'X'
                game_over = False

    pg.display.update()
