#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get_ipython().system('pip install pygame')


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
        draw_resetButton(screen)
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
#                 screen.fill((255, 255, 255))
#                 draw_resetButton(screen)
#                 pygame.display.update()
            
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


def draw_circles(screen, circles):
    for circle in circles:
        
        if(circle[2]==(3, 0, 0)):
            s_circle = pygame.draw.circle(screen,(45, 94, 80),(circle[0], circle[1]),23,2)
        elif (circle[2]==(0, 140, 0)): pass   
        else:     
            s_circle = pygame.draw.circle(screen,(94, 96, 95),(circle[0], circle[1]),23)    
            m_circle = pygame.draw.circle(screen,circle[2],(circle[0], circle[1]),21)


# In[5]:


circles = [(443, 149,(255, 255, 255)), (495, 45, (0, 0, 0)), (651, 357,(255, 255, 255))]


# In[6]:


def selected_cell(x, y):
    col = int((x - board_leftTop_x) / (line + cell_size))
    row = int((y - board_leftTop_y) / (line + cell_size))
    return (row, col, player)


# In[8]:


# (row ,col, 0:B or 1:W)
def circles_cor(board):
    circles = []
    for row in range(len(board)):        
        for col in range(len(board[row])):

            x = col * (line + cell_size) + cell_size /2 + board_leftTop_x

            y = row * (line + cell_size) + cell_size /2 + board_leftTop_y
            color=(0, 140, 0)
            if(board[row][col] == 1): color = (0, 0, 0)
            elif (board[row][col] == 2): color= (255, 255, 255)
            elif (board[row][col] == 3): color = (3, 0, 0)    
            circle = (x, y, color)    
            circles.append(circle)
    return circles       
            
            


# In[9]:


sample = [[0,0,1,2,3,0,0,1],
[1,0,0,0,0,2,3,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,2,0],
[1,0,0,0,0,2,0,3],
[0,0,0,0,0,0,3,0],
[1,0,0,2,0,0,0,0],
[0,0,0,0,0,0,3,2]]


# In[10]:


def draw_score(screen, black_score, white_score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    pygame.draw.circle(screen,(0, 0, 0),(100, board_height/2+20-38),23)
    b_text = font.render(f'Score: {black_score}', True, (255, 255, 255))
    screen.blit(b_text, dest=(150, board_height/2+20-38-14))
    
    pygame.draw.circle(screen,(255, 255, 255),(100, board_height/2+20+38),23)
    w_text = font.render(f'Score: {white_score}', True, (255, 255, 255))
    screen.blit(b_text, dest=(150, board_height/2+20+38-14))


# In[31]:


def write_turn(screen, player):
    font = pygame.font.Font('freesansbold.ttf', 32)

    s = ""
    if(player == 1): s="Black"
    elif(player == 2): s="White"
    b_text = font.render(f'{s} turn ', True, (255, 255, 255))
    screen.blit(b_text, dest=(screen_width/2 - 100 , (screen_height-board_height-20)/2 - 16 + board_height + 20))


# In[28]:


def screen_reset(screen):
    init_board = [[0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,3,0,0,0,0],
                  [0,0,3,2,1,0,0,0],
                  [0,0,0,1,2,3,0,0],
                  [0,0,0,0,3,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0]]
    
    draw_circles(screen, circles_cor(init_board) )


# In[53]:


def draw_resetButton(screen):
    color = (255,255,255)
    color_light = (100,100,100)
    pygame.draw.rect(screen,color_light,(150,board_height/2+20+38-14+76,140,40))
    smallfont = pygame.font.SysFont('freesansbold.ttf',35)
    text = smallfont.render('Reset' , True , color)
    screen.blit(text, dest=(186,board_height/2+20+38-14+76+9))
