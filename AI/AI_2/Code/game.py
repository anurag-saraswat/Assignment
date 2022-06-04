# Import and initialize the pygame library
import pygame
import numpy as np
pygame.init()

clock=pygame.time.Clock()

#Loading Images
background=pygame.image.load("./images/background.png")

bluePlayer = pygame.image.load("./images/blueball3.png")
bluePlayer = pygame.transform.scale(bluePlayer, (30, 30))

redPlayer = pygame.image.load("./images/redball1.png")
redPlayer = pygame.transform.scale(redPlayer, (30, 30))

title = pygame.image.load("./images/title.png")
title = pygame.transform.scale(title, (220, 220))

#Color Mapping

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
dark_green=(0,100,0)
light_green=(92, 219, 92)
gray=(119,118,110)
blue=(0,0,255)


# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])


# Kick function return list having coordinate of players which is involve in passing
def kick(player_pos):
    center_x,center_y = 278,350
    goal_x ,goal_y =280,30 
    blue_p_cor = player_pos[0]
    red_p_cor = player_pos[1]
    
    blue_p_cor.append((goal_x ,goal_y))
    
    final_lst = []
    
    goal_reached = False
    first_turn = True
    solution_possible = True
    
    top1_cost = 0
    top2_cost = 0
    
    
    while(not goal_reached):
        cost = []
        player = []
        #ignored = []
        
        if first_turn:
            for i in range(len(blue_p_cor)):
                dist = np.linalg.norm(np.array((center_x,center_y)) - np.array(blue_p_cor[i]))
                cost.append(dist)
                player.append(i)
            
            srt = sorted(cost)
            
            top1_cost+=srt[0]
            top2_cost+=srt[1]
            
            
            final_lst.append(player[cost.index(srt[0])])
            first_turn = False
            
        else:
            for i in range(len(blue_p_cor)):
        
                
                check = True
                collide = False
                
                if i in final_lst:
                    check = False
                    
                if check:
                    for j in final_lst:
                        if blue_p_cor[j][1] < blue_p_cor[i][1]:
                            check = False
                if check:
                    for j in red_p_cor:
                        dict1 = np.linalg.norm(np.array(blue_p_cor[final_lst[-1]]) - np.array(j))
                        dict2 = np.linalg.norm(np.array(j) - np.array(blue_p_cor[i]))
                        dict3 = np.linalg.norm(np.array(blue_p_cor[final_lst[-1]]) - np.array(blue_p_cor[i]))
                        if abs(dict1 + dict2 - dict3) <50:
                            collide = True    
                
                if check and (not collide):
                    dist = np.linalg.norm(np.array(blue_p_cor[final_lst[-1]]) - np.array(blue_p_cor[i]))
                    cost.append(dist)
                    player.append(i)
                    
            srt = sorted(cost)
            
            try:
                top1_cost+=srt[0]
                top2_cost+=srt[1]
            except:
                top1_cost+=0
                top2_cost+=0
            
            
            try:
                next_player = player[cost.index(srt[0])]
            except:

                next_player = 3
                
        
            if next_player == 3:
                goal_reached = True
            else:
                final_lst.append(next_player)
    
    if solution_possible:
        if top1_cost > top2_cost:
            print("Top 2 cost are : {} and {}".format(top1_cost," Not Possible"))
        else :
            print("Top 2 cost are : {} and {}".format(top1_cost , top2_cost))
                
            
                
    result = [(center_x,center_y)]
    for i in final_lst:
        result.append(blue_p_cor[i])
    result.append((goal_x ,goal_y))
  
    return result

# This function Plot the trajectory of ball         
def plotKick(result):
    for i in range(0,(len(result)-1)):
        pygame.draw.circle(screen,black,result[i],5)
        pygame.draw.circle(screen,black,result[i+1],5)
        pygame.draw.line(screen, black, result[i], result[i+1], 2)
        clock.tick(1200)
        
        
#This Function places players in accoring to condition mentioned in question
def placePlayer():
    
    #Placing palyer in red goal box
    x1 = np.random.randint(100,400,2)
    y1 = np.random.randint(50,140,2)
    
    screen.blit(bluePlayer, (x1[0],y1[0]))
    screen.blit(redPlayer, (x1[1],y1[1]))
    
    #Placing other players
    x2 = np.random.randint(60,490,4)
    y2 = np.random.randint(180,285,4)
    
    screen.blit(bluePlayer, (x2[0],y2[0]))
    screen.blit(redPlayer, (x2[1],y2[1]))
    screen.blit(redPlayer, (x2[2],y2[2]))
    screen.blit(bluePlayer, (x2[3],y2[3]))
    
    player_pos = [[(x1[0],y1[0]),(x2[0],y2[0]),(x2[3],y2[3])],
                   [(x1[1],y1[1]),(x2[1],y2[1]),(x2[2],y2[2])]]
    
    return player_pos

# Used for printing on screen
def Message(size,mess,x_pos,y_pos,clr):
    font=pygame.font.SysFont(None,size)
    render=font.render(mess,True,clr)
    screen.blit(render , (x_pos,y_pos))
    
# Used to ceate button
def button(x_button,y_button,mess_b):
    pygame.draw.rect(screen,dark_green,[x_button,y_button,150,40])
    Message(50,mess_b,x_button+20,y_button+5,white)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
        
    if((x_button<mouse[0]<x_button+150)and(y_button<mouse[1]<y_button+40)):
        pygame.draw.rect(screen,light_green,[x_button,y_button,150,40])
        Message(50,mess_b,x_button+20,y_button+5,white)
        if click==(1,0,0) and mess_b=="RESET":
            return "RESET"
        if click==(1,0,0) and mess_b=="KICK":
            return "KICK"


# Main Game loop
def gameLoop():
    end_loop = False
    while(not end_loop):
        screen.fill(white)
        screen.blit(background, (0, 0))
        screen.blit(title, (680, 20))
        
        
        #Drawing Initial ball 
        pygame.draw.circle(screen,black,(278,350),5)
        
        # Fixing position of blue player
        screen.blit(bluePlayer, (260,358))
        
        # Setting up title image
        screen.blit(title, (680, 20))
        
        player_pos = placePlayer()
        #print(player_pos)
        
        
        running = True
        kicked = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    end_loop = True
    
            k_value = button(610,300,"KICK")
            r_value = button(820,300,"RESET")
            
            if r_value == "RESET":
                break
            if (k_value == "KICK" and (not kicked)):
                result = kick(player_pos)
                kicked = True
                plotKick(result)
                #print(result)
                
            
            
            #Displaying Name
            msg = "Designed By: Anurag Saraswat"
            Message(30,msg,650,680,black)
            
            pygame.display.update()



gameLoop()
pygame.quit()
quit()