import pygame
import time
import random

## initiliaze all modules of pygame (import) > NEEDED
pygame.init()

##Variables
    # settings
display_width = 640
display_height = 640
border_width=16
fps=15
car_width= 16
car_height= 16
thingw=car_width
thingh=car_width
speed = 1
stepsize=car_width


    #colour definition
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

## Define stuff
    #clock> will time things (frames per second)
clock=pygame.time.Clock()
    #snake image
snakeImg = pygame.image.load('snake.png')


## setup display
    #set resolution
gameDisplay = pygame.display.set_mode((display_width, display_height))
    #set titel of window
pygame.display.set_caption('Snakarel')

## functions

def drawScreen(x,y,thing_startx,thing_starty):
    gameDisplay.fill(white) # set background > DOES ALL SO AFTER THIS THE REST
        # top line
    pygame.draw.rect(gameDisplay, red, [0,0,display_width,border_width])
        # bottom line
    pygame.draw.rect(gameDisplay, red, [0,display_height -border_width,display_width,border_width])
        # left line
    pygame.draw.rect(gameDisplay, red, [0,0,border_width, display_height])
        # right line
    pygame.draw.rect(gameDisplay, red, [display_width-border_width,0,border_width, display_height+border_width])

    car(x,y) #> blits car
    things(thing_startx, thing_starty, thingw, thingh, blue) #> Blits

    
def car(x,y):
    #blit draws stuff to background
    # x,y is where you will blit the image
    # y starts top, gets more when go down, x starts left goes right more
    gameDisplay.blit(snakeImg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def crash():
    message_display('You died')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115) #font and size as parameters
    TextSurf, TextRect = text_objects(text, largeText)  #returns text surface and text rectangle 
    TextRect.center = (display_width/2,display_height/2) #center text rectangle
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update() #update message to display
    
    time.sleep(2) #wait 2 seconds

    game_loop() #restart game loop

def text_objects(text, font):
    textSurface = font.render(text, True, red) #True= anti-analisian
    return textSurface, textSurface.get_rect()
    
    
def game_loop():
    ##set game loop > stops when quit or when snake crashes (wall)
    gameExit = False #start it is not crashed
        #starting position snake
    x = (display_width*0.4)
    x_right = False
    x_left = False
    y = (display_height *0.8)
    y_up = False
    y_down = False

    thing_startx= random.randrange(0, display_width, car_width)
    thing_starty= random.randrange(0, display_height, car_width)



    
    

    while not gameExit:
        #start loop with event handling> all input happens in here! 
        for event in pygame.event.get(): #gets every event (mouse movement, button movement> makes list per frame)
            #crash event> here when user does quit button
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #if a button is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #when arrow left is pressed
                    x_left = True
                    x_right = 0
                    y_up = 0
                    y_down = 0
                if event.key == pygame.K_LEFT: #when arrow right is pressed
                    x_right = True
                    x_left = 0
                    y_up = 0
                    y_down = 0
                if event.key == pygame.K_DOWN: #when arrow right is pressed
                    y_up = True
                    y_down = 0
                    x_right = 0
                    x_left = 0
                if event.key == pygame.K_UP: #when arrow right is pressed
                    y_up = 0
                    y_down = True
                    x_right = 0
                    x_left = 0


                
                # x will adjust to event
                #x = x + x_right + x_left
                #y = y + y_up + y_down
            

            #if button is released
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #when arrow left is pressed
            #        x_change = 0



        drawScreen(x,y,thing_startx,thing_starty)

        ##questionaire > check states (e.g. crashes with wall)
            #crash
        if x > display_width - car_width -border_width or x < 0 + border_width :
            crash()
        if y > display_height - car_height - border_width or y < 0 +border_width :
            crash()
            #apple thing
        if x == thing_startx and y == thing_starty:
            thing_startx= random.randrange(0, display_width,stepsize)
            thing_starty= random.randrange(0, display_height,stepsize)
            things(thing_startx, thing_starty, thingw, thingh, blue)
            #movement
        if x_left== True:
            x=x+speed*car_width
            y=y
        if x_right== True:
            x=x-speed*car_width
            y=y
        if y_up==True:
            y=y+speed*car_width
            x=x
        if y_down==True:
            y=y-speed*car_width
            x=x
            

            ##print the events to console
            #print(event)

        #update display (we made everything above, now display it)> no parameters updates everything
        pygame.display.update()

        clock.tick(fps)



game_loop()
# uninitiate pygame
pygame.quit()
quit()

        
