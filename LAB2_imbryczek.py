import pygame
import random

# ustalenie rozmiaru ekranu
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ustalenie rozmiaru puzzli
PUZZLE_SIZE = 100

# kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# inicjalizacja Pygame
pygame.init()

# stworzenie ekranu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Puzzle Game")

# ładowanie obrazka puzzli
puzzle_image = pygame.image.load("puzzle_image.jpg")

# podział obrazka na fragmenty
puzzle_pieces = []
for i in range(4):
    for j in range(4):
        puzzle_piece = pygame.Surface((PUZZLE_SIZE, PUZZLE_SIZE))
        puzzle_piece.blit(puzzle_image, (0, 0), (j*PUZZLE_SIZE, i*PUZZLE_SIZE, PUZZLE_SIZE, PUZZLE_SIZE))
        puzzle_pieces.append(puzzle_piece)

# losowe ustawienie puzzli
random.shuffle(puzzle_pieces)

# ustalenie pozycji puzzli
puzzle_positions = []
for i in range(4):
    for j in range(4):
        puzzle_positions.append((j*PUZZLE_SIZE, i*PUZZLE_SIZE))

# pusta pozycja puzzli
empty_position = (3*PUZZLE_SIZE, 3*PUZZLE_SIZE)

# pętla gry
running = True
while running:
    # obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            # sprawdzenie, czy kliknięto na puzzel
            for i, position in enumerate(puzzle_positions):
                if mouse_position[0] > position[0] and mouse_position[0] < position[0] + PUZZLE_SIZE and mouse_position[1] > position[1] and mouse_position[1] < position[1] + PUZZLE_SIZE:
                    # sprawdzenie, czy puzzel można przesunąć
                    if (position[0] == empty_position[0] and abs(position[1] - empty_position[1]) == PUZZLE_SIZE) or (position[1] == empty_position[1] and abs(position[0] - empty_position[0]) == PUZZLE_SIZE):
                        # zamiana miejscami puzzli
                        puzzle_positions[i], empty_position = empty_position, puzzle_positions[i]

    # rysowanie puzzli
    for i, position in enumerate(puzzle_positions):
        screen.blit(puzzle_pieces[i], position)

    # rysowanie pustej pozycji
    pygame.draw.rect(screen, WHITE, (empty_position[0], empty_position[1], PUZZLE_SIZE, PUZZLE_SIZE))

    # aktualizacja ekranu
    pygame.display.update()

# zamknięcie Pygame
pygame.quit()
