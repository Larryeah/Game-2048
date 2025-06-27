import pygame
from logics import *
import sys
from database import *

GAMERS_DB = get_best()

def draw_top_gamers():
    text_head = font_top.render(f"Best score: ", True, ORANGE)
    screen.blit(text_head, (250,5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f"{index+1}. {name} - {score}"
        text_gamer = font_gamer.render(f"{s}", True, ORANGE)
        screen.blit(text_gamer, (250, 35 + 25*index))
        print(index,name, score)

def draw_intro():
    img2048 = pygame.image.load("2048_logo.svg.png")
    text_welcome = font_score.render(f"Welcome!", True, ORANGE)
    name = "Text your name"
    is_find_name = False

    #Запуск заставки
    while not is_find_name:
        for event in pygame.event.get():
            # закрыть игру
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Text your name":
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name)>2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break


        screen.fill(BLACK)
        text_name = font_score.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center

        screen.blit(pygame.transform.scale(img2048, [200,200]), [10,10])
        screen.blit(text_welcome, (250,35))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)

def draw_game_over():
    text_game_over = font_score.render(f"Game over", True, ORANGE)
    text_score = font_score.render(f"Your score: {score}", True, ORANGE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = "New record!"
    else:
        text = f"Best record {best_score}"
    text_record = font_top.render(text, True, ORANGE)
    while True:
        for event in pygame.event.get():
            # закрыть игру
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.fill(BLACK)
        screen.blit(text_game_over, (150, 200))
        screen.blit(text_score, (50, 250))
        screen.blit(text_record, (150, 330))
        pygame.display.update()

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
    draw_top_gamers()
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
USERNAME = None
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")

#Шрифты
font = pygame.font.SysFont("comicsansms", 70)
font_score = pygame.font.SysFont("simsun", 48)
font_delta = pygame.font.SysFont("simsun", 32)
font_top = pygame.font.SysFont("calibri", 26)
font_gamer = pygame.font.SysFont("calibri", 20)



img = pygame.image.load("2048_logo.svg.png")
pygame.display.set_icon(img)
FPS = 60
clock = pygame.time.Clock()

#Заставка
draw_intro()


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
            if is_zero_in_mas(mas):
                empty = get_empty_list(mas)
                random.shuffle(empty)
                random_num = empty.pop()
                x, y = get_index_from_number(random_num)
                mas = insert_2_or_4(mas, x ,y)
            draw_interface(score, delta)
            print(f"Мы заполнили элемент под номером {random_num}")
            pygame.display.update()
draw_game_over()



    # clock.tick(FPS)
    # screen.fill(BLACK)
    # pygame.display.update()