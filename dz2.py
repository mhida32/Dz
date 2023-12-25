# ЭТО НЕ ГДЗ , А ОБРАЗЦЫ!!!!!!!!!!!
credit by karpblch

# Задание 1

car = {'марка':'','модель': '','год': ''}
car.update({'цвет': ' '})
print(car.get('марка'))
fruits = (" "," ")
print(fruits[])
numbers = (" "," ")
print(numbers[])

credit by karpblch

# Задание 2
credit by karpblch

lst = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]

for row in lst:
    print(' '.join(map(str, row)))

credit by karpblch

# Задание 3 (Может изменится)
credit by karpblch

class Car:
    '''Машина'''
    def __init__(self, make:str, model:str, year:int) -> None:
        '''Информация о машине'''
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        '''Вывод информации о машине'''
        print(f"Марка машины: {self.make}\nМодель машины: {self.model}\nГод машины: {self.year}")
        

переменная = Car(Сюда написать марку машины , модель и год)
переменная.display_info()

credit by karpblch

# Задание 4
credit by karpblch
class Animal:
    def __init__(self,name, species) -> None:
        self.name = name
        self.species = species 


    def make_sound(self): 
        print("Текст")

class Dog(Animal): 
    def make_sound(self): 
        print("Текст")
    
class Cat(Animal): # подкласс Cat
    def make_sound(self):
        print("Текст")

animal = Animal("Текст","Текст")
animal.make_sound()
dog = Dog("Текст","Текст")
dog.make_sound()
cat = Cat("Текст","Текст")
cat.make_sound()
credit by karpblch

# Задание 5
credit by karpblch
with open('sample.txt','w',encoding='utf-8') as f: 
    f.write("Текст") 
with open('sample.txt','r',encoding='utf-8') as f:
    print(f.read()) 
credit by karpblch

# Задание 9
credit by karpblch
import pygame
from random import randint

pygame.init()

 
FRAME_COLOR = (120, 180, 205)

FPS = 5 

WIDHT_COUNT_RECT = 20 

HEIGHT_COUNT_RECT = 20 

SIZE_RECT = 20

RET = 1 

HEADER = 70 

COLOR_RECT_0 = (74, 145, 71)

COLOR_RECT_1 = (33, 107, 121) 

WIDHT = SIZE_RECT * (WIDHT_COUNT_RECT + 2 + RET) 

HEIGHT = SIZE_RECT * (HEIGHT_COUNT_RECT + 2 + RET) + HEADER 

COLOR_SNAKE = (0, 219, 7) 
END_COLOR = (255, 0, 0) 

FONT = pygame.font.SysFont(None, 60)
TEXT_END = FONT.render('GAME OVER', 1, (255, 255, 255)) 
RECT_TEXT_END = TEXT_END.get_rect(center=(WIDHT // 2, HEIGHT // 2))  

COLOR_FOOD = (255, 0, 41)
text_count = FONT.render('Счет: 0', 1, (255, 255, 255)) 
RECT_TEXT_COUNT = TEXT_END.get_rect(topleft=(20, 20)) 


TEXT_WIN = FONT.render('YOU WIN', 1, (255, 255, 255))
TEXT_WIN_RECT = TEXT_WIN.get_rect(center=(WIDHT // 2, HEIGHT // 2)) 


screen = pygame.display.set_mode((WIDHT, HEIGHT)) 
pygame.display.set_caption('Змейка') 


clock = pygame.time.Clock() 

done = False 

mode = 'game' 

count = 0 

class Snake:
    def __init__(self, x, y):
        
        self.x = x 
        
        self.y = y  
    
    def inside(self):
        return 0 <= self.x < WIDHT_COUNT_RECT and 0 <= self.y < HEIGHT_COUNT_RECT
    def __eq__(self, val):
        if isinstance(val, Snake):
            return self.x == val.x and self.y == val.y
        
def draw_rect(color, row, col):
    
    pygame.draw.rect(screen, color, 
                     [SIZE_RECT + col * SIZE_RECT + RET * col, 
                      HEADER + SIZE_RECT + row * SIZE_RECT + RET * row,
                      SIZE_RECT, SIZE_RECT])

def draw_map():
    for i in range(HEIGHT_COUNT_RECT):
        for j in range(WIDHT_COUNT_RECT):
            if (i + j) % 2 == 0:
                draw_rect(COLOR_RECT_0, i, j)
            else:
                draw_rect(COLOR_RECT_1, i, j)

def draw_snake(): 
    for snake in snake_rects:
        draw_rect(COLOR_SNAKE, snake.y, snake.x)

def move_snake(pos, speed):
    snake_rects.append(Snake(pos[0] + speed[0], pos[1] + speed[1]))
    snake_rects.pop(0)

def random_food_rect():
    x = randint(0, WIDHT_COUNT_RECT - 1)
    y = randint(0, HEIGHT_COUNT_RECT - 1)
    food_rect = Snake(y, x)
    while food_rect in snake_rects:
        if len(snake_rects) == WIDHT_COUNT_RECT * HEIGHT_COUNT_RECT:
            break
        x = randint(0, WIDHT_COUNT_RECT - 1)
        y = randint(0, HEIGHT_COUNT_RECT - 1)
        food_rect = Snake(y, x)
    return food_rect

def eat_self():
    return snake_rects[-1] in snake_rects[:-3]

def is_win():
    return len(snake_rects) == WIDHT_COUNT_RECT * HEIGHT_COUNT_RECT

snake_rects = [Snake(WIDHT_COUNT_RECT // 2, HEIGHT_COUNT_RECT // 2)]
speed = [-1, 0]
food = random_food_rect()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
        elif mode == 'game' and event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and speed[1] == 0: 
                speed = [0, -1]
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and speed[0] == 0: 
                speed = [1, 0]
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and speed[1] == 0: 
                speed = [0, 1]
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and speed[0] == 0: 
                speed = [-1, 0]
    if mode == 'game': 
        last_rect = snake_rects[-1]
        move_snake((last_rect.x, last_rect.y), speed)
        if not last_rect.inside() or eat_self():
            mode = 'end'
            continue
        if last_rect == food: 
            snake_rects.append(food)
            food = random_food_rect()
            count += 1
            text_count = FONT.render(f'Счет: {count}', 1, (255, 255, 255))
            if is_win():
                mode = 'win'
        screen.fill(FRAME_COLOR)
        screen.blit(text_count, RECT_TEXT_COUNT)
        draw_map()
        draw_rect(COLOR_FOOD, food.y, food.x)
        draw_snake()

    elif mode == 'end':
        screen.fill(END_COLOR)
        screen.blit(TEXT_END, RECT_TEXT_END)
    elif mode == 'win':
        screen.fill((0, 255, 0))
        screen.blit(TEXT_WIN, TEXT_WIN_RECT)

    pygame.display.flip()
    clock.tick(FPS)

credit by karpblch
