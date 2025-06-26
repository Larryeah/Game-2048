import pygame
from logics import *
import sys


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    pretty_print(mas)
    text_score = font_score.render(f"Score: ", True, ORANGE)
    text_score_value = font_score.render(f"{score}", True, ORANGE)

    screen.blit(text_score, (20,30))
    screen.blit(text_score_value, (175, 30))
    if delta>0:
        text_delta = font_delta.render(f"+{delta}", True, ORANGE)
        screen.blit(text_delta, (170, 70))
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f"{value}", True, BLACK)
            w = column * SIZE_BLOCKS + (column + 1) * MARGIN
            h = row * SIZE_BLOCKS + (row + 1) * MARGIN + SIZE_BLOCKS
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCKS, SIZE_BLOCKS))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCKS - font_w) / 2
                text_y = h + (SIZE_BLOCKS - font_h) / 2
                screen.blit(text, (text_x, text_y))

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (138, 105, 76),
    16: (153, 112, 77),
    32: (166, 115, 71),
    64: (181, 118, 63),
    128: (191, 117, 52),
    256: (207, 115, 35),
    512: (222, 116, 24),
    1024: (237, 115, 9),
    2048: (237, 115, 9),
}

#Размеры блоков
BLOCKS = 4
SIZE_BLOCKS = 110
MARGIN = 10
WIDTH = BLOCKS*SIZE_BLOCKS + (BLOCKS+1)*MARGIN
HEIGHT = WIDTH+110
TITLE_REC = pygame.Rect(0,0,WIDTH,110)

#Цвета
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (130, 130, 130)
ORANGE = (255, 165, 0)

#Переменные, шрифты, настройки
score = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")
font = pygame.font.SysFont("comicsansms", 70)
font_score = pygame.font.SysFont("simsun", 48)
font_delta = pygame.font.SysFont("simsun", 32)
img = pygame.image.load("2048_logo.svg.png")
pygame.display.set_icon(img)
FPS = 60
clock = pygame.time.Clock()

#Первый вывод меню
draw_interface(score)
pygame.display.update()

#запускаем игру
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        #закрыть игру
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        #сама игра идет отсюда
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            if event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            if event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2_or_4(mas, x ,y)
            draw_interface(score, delta)
            print(f"Мы заполнили элемент под номером {random_num}")
            pygame.display.update()


    # clock.tick(FPS)
    # screen.fill(BLACK)
    # pygame.display.update()