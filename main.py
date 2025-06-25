import pygame
import random


def pretty_print(mas):
    print("-"*10)
    for row in mas:
        print(*row)
    print("-" * 10)

def get_number_from_index(i,j):
    return i*4+j+1

def get_index_from_number(num):
    num -= 1
    x,y = num//4, num%4
    return x,y

def insert_2_or_4(mas,x,y):
    if random.random()<=0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas

def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j]==0:
                num = get_number_from_index(i,j)
                empty.append(num)
    return empty

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

# pygame.init()
# size = (800, 600)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("2048")
# font = pygame.font.SysFont("comicsansms", 32)
#
# #Цвета
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
# BLACK = (0,0,0)
#
# img = pygame.image.load("2048_logo.svg.png")
# pygame.display.set_icon(img)
# FPS = 60
# clock = pygame.time.Clock()
#
while True:
    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num = empty.pop()
    x, y = get_index_from_number(random_num)
    mas = insert_2_or_4(mas, x ,y)
    print(f"Мы заполнили элемент под номером {random_num}")
    pretty_print(mas)

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         quit()
    # clock.tick(FPS)
    # screen.fill(BLACK)
    # pygame.display.update()