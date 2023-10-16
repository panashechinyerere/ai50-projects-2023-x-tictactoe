import pygame
from tictactoe import TicTacToe

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 300, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up game instance
game = TicTacToe()

# Set up the game loop
def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                game.make_move(mouse_pos)

        draw_window()

    pygame.quit()

# Draw the game window
def draw_window():
    WIN.fill(WHITE)

    # Draw board
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(WIN, BLACK, (col * 100, row * 100, 100, 100), 2)
            if game.board[row][col] != game.EMPTY:
                draw_move(row, col, game.board[row][col])

    pygame.display.update()

# Draw X or O on the board
def draw_move(row, col, move):
    x = col * 100 + 50
    y = row * 100 + 50
    if move == game.X:
        pygame.draw.line(WIN, BLACK, (x - 25, y - 25), (x + 25, y + 25), 2)
        pygame.draw.line(WIN, BLACK, (x + 25, y - 25), (x - 25, y + 25), 2)
    else:
        pygame.draw.circle(WIN, BLACK, (x, y), 25, 2)

# Run the game
if _name_ == "_main_":
    main()