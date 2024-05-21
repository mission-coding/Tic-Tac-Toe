import pygame
import sys
import numpy
pygame.init()

# Screen
screen_width = 300
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic, Tac, Toe")

# Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Global Variables
run = True
clock = pygame.time.Clock()
fps = 30
turn = 'o'
board = (numpy.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
]))
o = 1
x = 2
winner = None
draw = None

def home():
    screen.fill(white)
    
    # GameBoard
        # Vertical lines
    pygame.draw.line(screen, black, (screen_width/3, 0), (screen_width/3, screen_height-100), 4)
    pygame.draw.line(screen, black, (screen_width/1.5, 0), (screen_width/1.5, screen_height-100), 4)
        # Horizontal lines
    pygame.draw.line(screen, black, (0, (screen_height-100)/3), (screen_width, (screen_height-100)/3), 4)
    pygame.draw.line(screen, black, (0, (screen_height-100)/1.5), (screen_width, (screen_height-100)/1.5), 4)
    # pygame.draw.line(screen, black, (0, screen_height-100), (screen_width, screen_height-100), 4)
    # pygame.draw.line(screen, black, (0, 0), (screen_width, 0), 4)

def mouse_pointing():
    global row, col
    x, y = pygame.mouse.get_pos()
    row = int(y // ((screen_height - 100) / 3))
    col = int(x // (screen_width / 3))
    draw_figure(row, col)

def draw_figure(row, col):
    global turn

    if board[row, col] == 0:
        fig_x = int((col + 0.5) * screen_width / 3)
        fig_y = int((row + 0.5) * (screen_height - 100) / 3)

        if turn == 'o' and winner == None and draw == None:
            pygame.draw.circle(screen, black, (fig_x, fig_y), 40, 4)
            board[row][col] = o
            turn = 'x'

        elif turn == 'x' and winner == None and draw == None:
            pygame.draw.line(screen, black, (fig_x-30, fig_y-30), (fig_x+30, fig_y+30), 5)
            pygame.draw.line(screen, black, (fig_x+30, fig_y-30), (fig_x-30, fig_y+30), 5)
            board[row][col] = x
            turn = 'o'

        check_winner()

    else:
        pass

def draw_text(text, color, size, x2, y):
    font = pygame.font.Font(None, size)
    display_text = font.render(text, True, color, white)
    screen.blit(display_text, (x2,y))

def check_winner():
    global winner, draw

    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            winner = True
            # Drawing line when winnig
            if row == 0:
                pygame.draw.line(screen, red, (0, (screen_height-100)/6), (screen_width, (screen_height-100)/6), 4)
            if row == 1:
                pygame.draw.line(screen, red, (0, (screen_height-100)/2), (screen_width, (screen_height-100)/2), 4)
            if row == 2:
                pygame.draw.line(screen, red, (0, (screen_height-100)/1.2), (screen_width, (screen_height-100)/1.2), 4)

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            winner = True
            # Drawing line when winning
            if col == 0:
                pygame.draw.line(screen, red, (screen_width/6, 0), (screen_width/6, screen_height-100), 4)
            if col == 1:
                pygame.draw.line(screen, red, (screen_width/2, 0), (screen_width/2, screen_height-100), 4)
            if col == 2:
                pygame.draw.line(screen, red, (screen_width/1.2, 0), (screen_width/1.2, screen_height-100), 4)


    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        winner = True
        # Drawing line when winnig
        pygame.draw.line(screen, red, (0,0), (screen_width, screen_height-100), 4)

    elif board[0][2] == board[1][1] == board[2][0] != 0:
        winner = True
        # Drawing line when winnig
        pygame.draw.line(screen, red, (screen_width,0), (0, screen_height-100), 4)

    # Check for Draw game
    if(all([all(row) for row in board]) and winner is None ):
        draw = True

    if winner:
        if turn == 'o':
            draw_text("X's Wins !!", green, 45, 80, screen_height - 65)
        else:
            draw_text("O's Wins !!", green, 45, 80, screen_height - 65)

        draw_text("Press Enter to Play again", blue, 25, 50, screen_height - 35)

    if draw:
        draw_text("It's Draw!", green, 45, 80, screen_height - 65)
        draw_text("Press Enter to Play again", blue, 25, 50, screen_height - 35)


def reset_game():
    global board, winner, draw, turn
    board = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    winner = None
    draw = None
    turn = 'o'
    home()

home()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pointing()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and (draw == True or winner == True):
                reset_game()

    msg = turn.upper()+"'s Turn"

    if winner == None and draw == None:
        draw_text(msg, blue, 45, 90, screen_height - 65)

    pygame.display.update()
