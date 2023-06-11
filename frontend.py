#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pygame')


# In[1]:


import pygame 


# In[66]:


screen_width = 800
screen_height = 600
rows, cols = 8, 8
cell_size = 50
line = 2 
player = 1
next_player = 1
reset = 1
FPS = 60
reset_x =(150, 290)
reset_y =(327, 367)
board_width, board_height = cols*cell_size + (cols-1)* line, rows*cell_size + (rows-1)* line
board_leftTop_x, board_leftTop_y = screen_width-board_width-20, 20
print(board_width, board_height)


# In[67]:


pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Othello")
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    draw_resetButton(screen)
    pygame.display.update()
    if(reset == 1):
        draw_board(screen)
        screen_reset(screen)
        draw_score(screen, 2, 2)
        write_turn(screen, 1)
#         draw_resetButton(screen)
        pygame.display.update()
        reset = 0
        continue
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            print(selected_cell(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
            if((mouse_pos[0]>= reset_x[0]) and (mouse_pos[0]<= reset_x[1]) and 
               (mouse_pos[1]>= reset_y[0]) and (mouse_pos[1]<= reset_y[1])):
                reset = 1
                screen.fill((255, 255, 255))
                draw_resetButton(screen)
                pygame.display.update()
            
            elif((mouse_pos[0]>= board_leftTop_x) and (mouse_pos[0]<= board_leftTop_x+board_width) and 
               (mouse_pos[1]>= board_leftTop_y) and (mouse_pos[1]<= board_leftTop_y+ board_height)):
                if (player == 1): next_player = 2
                elif (player == 2): next_player = 1  

                draw_board(screen)
                #sample is the board output of backend
                circles = circles_cor(sample)
                draw_circles(screen, circles)

                #1, 2 will be replaced with the output score of backend
                draw_score(screen, 1, 2)
                write_turn(screen, player)

                pygame.display.update()
    player = next_player
    print(player)
    
    

pygame.quit()


# In[3]:


def draw_board(screen):
    screen.fill((34, 34, 34))
    main_rect = pygame.draw.rect(screen, (0, 144, 103), (board_leftTop_x, board_leftTop_y, board_width, board_height))
#  horezontal lines
    for i in range(rows - 1):
        pygame.draw.rect(screen, (0, 0, 0), (main_rect.x, main_rect.y + (i+1)*cell_size + i*line,
                                          board_width, line))
#  vertical lines                                               
    for i in range(cols - 1):
        pygame.draw.rect(screen, (0, 0, 0), (main_rect.x + (i+1)*cell_size + i*line, main_rect.y ,
                                             line, board_height))   
        


# In[4]:
