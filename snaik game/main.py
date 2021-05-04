import pygame
import random

pygame.init()

black = (0, 0, 0)
blue = (65, 167, 198)
red = (255, 0, 0)
orange = (249, 102, 63)
grey = (109, 107, 107)
width, height = 600, 400

game_display = pygame.display.set_mode((width, height))

pygame.display.set_caption('Sanik Game')

snake_size = 10
snake_speed = 15

font_style = pygame.font.SysFont('ubuntu', 30)
'''def message(msg,color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width/2, height/2])'''

clock = pygame.time.Clock()


def our_snake(snake_size, snake_List, color):
    if color==orange:
        for x in snake_List:
            pygame.draw.rect(game_display, color, [x[0], x[1], snake_size, snake_size])
    elif color==blue:
        for x in snake_List:
            pygame.draw.rect(game_display, color, [x[0], x[1], snake_size, snake_size])


#pygame.draw.rect(game_display, orange, [fuudx, fuudy, snake_size, snake_size])
#ygame.draw.rect(game_display, blue, [foodx, foody, snake_size, snake_size])








def main_game():

    global color,y,snake_speed
   # global foodx,foody,fuudx,fuudy

    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    fuudx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    fuudy = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    food_color = ['blue', 'orange']




    color=blue
    game_over = False
    game_close = False
    x1 = width / 2
    y1 = height / 2

    x1_new = 0
    y1_new = 0

    snake_List = []
    Length_of_snake = 1

    x = random.randrange(0, 2)
    y = food_color[x]

    while not game_over:
        while game_close == True:
            game_display.fill(black)


            mesg = font_style.render('You Lost! or Press R-Play Again or Press Q-Quit', True, grey)
            game_display.blit(mesg, [width / 11, height / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_r:
                        main_game()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                '''if Length_of_snake>3:
                    print(Length_of_snake)

                    if snake_List[0][0] > snake_List[1][0]:# moving left
                        if event.key == pygame.K_DOWN:
                            x1_new = 0
                            y1_new = 10
                        elif event.key == pygame.K_LEFT:
                            x1_new = -10
                            y1_new = 0
                        elif event.key == pygame.K_UP:
                            x1_new = 0
                            y1_new = -10
                        elif event.key == pygame.K_RIGHT:
                             pass

                    elif snake_List[0][0] < snake_List[1][0]:# moving right
                        if event.key == pygame.K_DOWN:
                            x1_new = 0
                            y1_new = 10
                        elif event.key == pygame.K_RIGHT:
                            x1_new = 10
                            y1_new = 0
                        elif event.key == pygame.K_UP:
                            x1_new = 0
                            y1_new = -10
                        elif event.key == pygame.K_LEFT:
                            pass

                    elif snake_List[0][1] < snake_List[1][1]:# moving up
                        if event.key == pygame.K_DOWN:
                            pass
                        elif event.key == pygame.K_LEFT:
                            x1_new = -10
                            y1_new = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_new = 10
                            y1_new = 0
                        elif event.key == pygame.K_UP:
                            pass

                    elif snake_List[0][1] > snake_List[1][1]:# moving down
                        if event.key == pygame.K_UP:
                            x1_new = 0
                            y1_new = 10
                        elif event.key == pygame.K_LEFT:
                            x1_new = -10
                            y1_new = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_new = 10
                            y1_new = 0
                        elif event.key == pygame.K_DOWN:
                            pass
                else:'''
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                            x1_new = -10
                            y1_new = 0
                    elif event.key == pygame.K_RIGHT:
                            x1_new = 10
                            y1_new = 0
                    elif event.key == pygame.K_UP:
                            x1_new = 0
                            y1_new = -10
                    elif event.key == pygame.K_DOWN:
                            x1_new = 0
                            y1_new = 10


        if x1 >= width or x1 < 0 or y1 > height or y1 < 0:
            game_close = True
            print('Your score:', Length_of_snake-1)

        x1 += x1_new
        y1 += y1_new
        game_display.fill(black)

        if y == 'orange':
            orange_snake=pygame.draw.rect(game_display, orange, [fuudx, fuudy, snake_size, snake_size])
        elif y=='blue':
            pygame.draw.rect(game_display, blue, [foodx, foody, snake_size, snake_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        '''for x in snake_List[:-1]:
            if x[0] == snake_Head[0] and x[1]==snake_Head[1]:
                print(x, snake_Head)
                game_close = True

            if x == snake_Head:
                print('final hit', x, snake_Head)
                game_close = True
                print('Your score:', Length_of_snake-1)'''
        if x1 == foodx and y1 == foody:
            print(x1, y1)
            foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            x = random.randrange(0, 2)
            y = food_color[x]
            Length_of_snake += 1
            color=blue

        elif x1 == fuudx and y1 == fuudy:
            if snake_List[0][0]> snake_List[1][0]:
                x1_new = 10                             #moving left
                y1_new = 0
                x1 += x1_new
                y1 += y1_new
            elif snake_List[0][0]< snake_List[1][0]:
                x1_new = -10                            #moving right
                y1_new = 0
                x1 += x1_new
                y1 += y1_new
            elif snake_List[0][1]< snake_List[1][1]:
                x1_new = 0                              #moving up
                y1_new = -10
                x1 += x1_new
                y1 += y1_new
            elif snake_List[0][1]> snake_List[1][1]:
                x1_new = 0                               #moving down
                y1_new = 10
                x1 += x1_new
                y1 += y1_new
            print('orange food',x1, y1)
            fuudx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            fuudy = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            print(snake_List)
            Length_of_snake += 1
            color = orange

            x = random.randrange(0, 2)
            y=food_color[x]


        our_snake(snake_size, snake_List, color)
        pygame.display.update()

        clock.tick(15)

    pygame.quit()
    quit()


main_game()
