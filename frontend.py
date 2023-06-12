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
    
    
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Othello")
clock = pygame.time.Clock()
run = True
flag1 = False
flag2 = False
check1 = None
check2 = None

class Checkbox:
    def __init__(self, surface, x, y, idnum, color=(230, 230, 230),
        caption="", outline_color=(0, 0, 0), check_color=(0, 0, 0),
        font_size=30, font_color=(0, 0, 0), text_offset=(28, 1), font='Ariel Black'):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        self.ft = font

        #identification for removal and reorginazation
        self.idnum = idnum

        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()

        # variables to test the different states of the checkbox
        self.checked = False

    def _draw_button_text(self):
        self.font = pygame.font.SysFont(self.ft, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + self.to[0], self.y + 12 / 2 - h / 2 + 
        self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_checkbox(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            pygame.draw.circle(self.surface, self.cc, (self.x + 6, self.y + 6), 4)

        elif not self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = pygame.mouse.get_pos()
        px, py, w, h = self.checkbox_obj
        if px < x < px + w and py < y < py + w:
            if self.checked:
                self.checked = False
            else:
                self.checked = True

    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self._update(event_object)
            
 def check_boxes(screen):
    boxes = []
    font = pygame.font.Font('freesansbold.ttf', 38)

    b_text = font.render('Mode: ', True, (0, 144, 103))
    screen.blit(b_text, dest=(200, 30))

    button = Checkbox(screen, 200, 100, 0, caption='Human vs Human')
    button2 = Checkbox(screen, 200, 150, 1, caption='Human vs Computer')
    button3 = Checkbox(screen, 200, 200, 2, caption='Computer vs Computer')
    boxes.append(button)
    boxes.append(button2)
    boxes.append(button3)
    nboxes = []
 
    
    
    b1= Checkbox(screen, 200, 350, 3, caption='Easy')
    b2 = Checkbox(screen, 200, 400, 4, caption='Medium')
    b3 = Checkbox(screen, 200, 450, 5, caption='Hard')
    nboxes.append(b1)
    nboxes.append(b2)
    nboxes.append(b3)
    
    return boxes, nboxes

while run:
    clock.tick(FPS)
    if(begining == 1):
        screen.fill((34, 34, 34))
        boxes,_ = check_boxes(screen)
        
        for box in boxes:
            box.render_checkbox()

        
        pygame.display.update()
        pygame.display.flip()

#                 pygame.time.wait(1000000)
        if(boxes[0].checked):
            print("button1")
        if(boxes[0].checked):
            print("button1")
        elif(boxes[1].checked):
            print("button2")
        elif(boxes[2].checked):
            print("button3")
            
    elif(middle == 1):
        font = pygame.font.Font('freesansbold.ttf', 38)
        screen.fill((34, 34, 34))
        _,nboxes = check_boxes(screen)
        b_text = font.render('Difficulty level: ', True, (0, 144, 103))
        screen.blit(b_text, dest=(200, 290))
        button2 = Checkbox(screen, 200, 150, 1, caption=check1.caption)
        button2.checked = True
        button2.render_checkbox()
        for box in nboxes:
            box.render_checkbox()


        pygame.display.update()
        pygame.display.flip()

#                 pygame.time.wait(1000000)
        if(nboxes[0].checked):
            print("button1")
        if(nboxes[0].checked):
            print("button1")
        elif(nboxes[1].checked):
            print("button2")
        elif(nboxes[2].checked):
            print("button3")

    else: 
        draw_resetButton(screen)
        pygame.display.update()
        if(reset == 1):
            screen.fill((34, 34, 34))
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
            print("ABFABFABFABF",pygame.mouse.get_pos())
            if(begining == 1): 
               
                for box in boxes:
                    box.update_checkbox(event)
                    if box.checked is True:
                        check1 = box
                        for b in boxes:
                            if b != box:
                                b.checked = False

                for box in boxes:
                    box.render_checkbox()

                pygame.display.update()                
                pygame.display.flip()

                begining = 0
                middle = 1
                
                
            elif(middle == 1): 
               
                for box in nboxes:
                    box.update_checkbox(event)
                    if box.checked is True:
                        flag2 = True
                        check2 = box
                        for b in boxes:
                            if b != box:
                                b.checked = False
                
                check2.checked = True
                check2.render_checkbox()

                pygame.display.update()                
                pygame.display.flip()
                
                middle = 0
                reset = 1
                #to be sent check1 and check2
                print("AAAAAAAAAFFFFFFFFFF",check1.caption, check2.caption)
                
#                 if((mouse_pos[0]>= start_x[0]) and (mouse_pos[0]<= start_x[1]) and 
#                     (mouse_pos[1]>= start_y[0]) and (mouse_pos[1]<= start_y[1])):
#                     print("AAAAAAAAAAaFFFFFFFFFFFFFFFff")
#                     print("flags",flag1,flag2)
#                     if(flag1 and flag2):
#     #             if(((boxes[0].checked) or (boxes[1].checked) or (boxes[2].checked)) and
#     #                   ((nboxes[0].checked) or (nboxes[1].checked) or (nboxes[2].checked))):           

#                         print("******************")
#                         if((boxes[0].checked)):
#                             print("f1")
#                         elif(boxes[1].checked):
#                             print("f2")
#                         elif(boxes[2].checked):
#                             print("f3")
#                         if(nboxes[0].checked):
#                             print("f4")
#                         elif(nboxes[1].checked):
#                             print("f5")
#                         elif(nboxes[2].checked):
#                             print("f")
                        
                       
#                         reset = 1
#                         begining = 0
#                         #to be sent check1 and check2
#                         print("finnnnnnnnnnnnal: ",check1.caption, check2.caption)
#                         flag1 = False
#                         flag2 = False
#                         check1 = None
#                         check2 = None

            elif(begining == 0 and middle == 0 and (mouse_pos[0]>= reset_x[0]) and (mouse_pos[0]<= reset_x[1]) and 
               (mouse_pos[1]>= reset_y[0]) and (mouse_pos[1]<= reset_y[1])):
                reset = 1


            elif((mouse_pos[0]>= board_leftTop_x) and (mouse_pos[0]<= board_leftTop_x+board_width) and 
               (mouse_pos[1]>= board_leftTop_y) and (mouse_pos[1]<= board_leftTop_y+ board_height)):
                #to be sent to backend
                print(selected_cell(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
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
