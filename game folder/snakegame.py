import pygame
import random
import os

#for initilizing all modules for music
pygame.mixer.init()

#initilizing all modules of pygame
pygame.init()

#game colour
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,255,0)
green = (0,0,255)

#game display
screen_hight = 700
screen_width = 700
gamewindow = pygame.display.set_mode((screen_hight,screen_width))
pygame.display.set_caption("my game")
pygame.display.update()

#game clock and system font(for score printing)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
#all game function

start_game = False

def drawsnake(gamewindow,color,llist,size):
    """for drawing snake"""
    for x,y in llist:
         pygame.draw.rect(gamewindow,black,[x,y,size,size])

def printscore(text,color,x,y):
    """for printing score"""
    screen_test = font.render(text,True,color)
    gamewindow.blit(screen_test, [x,y])
    #this function is used for updating the screen

def gameloop():

    #game variables
    game_over = False
    game_exit = False
    snake_x = 44
    snake_y = 55
    snake_size = 15
    velosity_x = 0
    velosity_y = 0
    init_velosity = 2
    food_x = random.randint(10,screen_width/2)
    food_y = random.randint(10,screen_hight/2)
    score = 0
    length = 1
    snake_list = []
    

    while not game_exit:
        
        if game_over:
            gamewindow.fill(blue)
            printscore("GAME OVER!", red, 200,200)
            printscore("PRESS ENTER TO CONTINUE", red,50,250)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game_exit = True
                if event.type == pygame.KEYDOWN:                  
                    if event.key == pygame.K_RETURN:
                        gameloop()
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   game_exit = True

                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_LEFT:
                      velosity_x = -init_velosity
                      velosity_y = 0
                   if event.key == pygame.K_RIGHT:
                      velosity_x = init_velosity
                      velosity_y = 0
                   if event.key == pygame.K_UP:
                      velosity_x = 0
                      velosity_y = -init_velosity
                   if event.key == pygame.K_DOWN:
                      velosity_x = 0
                      velosity_y = init_velosity
        
                
            gamewindow.fill(white)
            snake_x = snake_x + velosity_x
            snake_y = snake_y + velosity_y
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if abs(food_x-snake_x) < 13 and abs(food_y-snake_y) < 13:
              food_x = random.randint(0,screen_width/2)
              food_y = random.randint(0,screen_hight)
              score += 10
              length += 5

            if len(snake_list) > length:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_hight or snake_y < 0 or snake_y > screen_width:
               #gamewindow.fill(white)
               game_over =True
               pygame.mixer.music.load('gameover.mp3')
               pygame.mixer.music.play()


            printscore(f"score: {score}", blue, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x,food_y,snake_size,snake_size])
            drawsnake(gamewindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(60)      
                
    #for quiting game
    pygame.quit()
    quit()

while not start_game:
               
        gamewindow.fill(green)
        printscore("WELCOME!", red, 200,200)
        printscore("DESIGIND BY", red,200,250)
        printscore("SIDDHARTHA CHAKRABORTY", red,50,300)
        printscore("PRESS ENTER", red,200,350)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = True
            if event.type == pygame.KEYDOWN:                  
                if event.key == pygame.K_RETURN:
                    gameloop()
