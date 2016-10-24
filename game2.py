#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *
from helpers import *
import random
import time

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PyManMain:
    
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        self.timer = 10000
        self.items = ["ring", "vase", "scarf"]
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
                                                          
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        
        """Load All of our Sprites"""
        self.LoadSprites();
        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(500, 30)
        
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((234,201,179))
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.snake.move(event.key)
                        
            # """Check for collision"""
            # lstCols = pygame.sprite.spritecollide(self.snake
            #                                      , self.pellet_sprites
            #                                      , True)
            # """Update the amount of pellets eaten"""
            # self.snake.pellets = self.snake.pellets + len(lstCols)
            collide1 = pygame.sprite.collide_rect(self.snake, self.stall1)
            collide2 = pygame.sprite.collide_rect(self.snake, self.stall2)
            collide3 = pygame.sprite.collide_rect(self.snake, self.stall3)
            collide4 = pygame.sprite.collide_rect(self.snake, self.stall4)
            collide5 = pygame.sprite.collide_rect(self.snake, self.stall5)
            collide6 = pygame.sprite.collide_rect(self.snake, self.stall6)

            if collide1:
                print "Stall 1"
                runGame()

            elif collide2:
                print "Stall 2"

            elif collide3:
                print "Stall 3"

            elif collide4:
                print "Stall 4"

            elif collide5:
                print "Stall 5"

            elif collide6:
                print "Stall 6"
                
            """Do the Drawging"""               
            self.screen.blit(self.background, (0, 0))     
            # if pygame.font:
            #     font = pygame.font.Font(None, 36)
            #     text = font.render("Pellets %s" % self.snake.pellets
            #                         , 1, (255, 0, 0))
            #     textpos = text.get_rect(centerx=self.background.get_width()/2)
            #     self.screen.blit(text, textpos)
               
            # self.pellet_sprites.draw(self.screen)
            self.stall1_sprites.draw(self.screen)
            self.stall2_sprites.draw(self.screen)
            self.stall3_sprites.draw(self.screen)
            self.stall4_sprites.draw(self.screen)
            self.stall5_sprites.draw(self.screen)
            self.stall6_sprites.draw(self.screen)
            self.snake_sprites.draw(self.screen)
            pygame.draw.rect(self.screen, (140,240,130),
                             Rect((100,400), (450,300)))
          
            myfont = pygame.font.SysFont("monospace", 15)
            
            self.timer+=1
            # render text
            timeLeft = myfont.render(str(self.timer), 1, (0,0,0))
            self.screen.blit(timeLeft, (100, 400))
            itemsList = ""
            for item in self.items:
                itemsList += item + " "
            itemsLeft = myfont.render(str(itemsList), 1, (0,0,0))
            self.screen.blit(itemsLeft, (200, 400))
            pygame.display.flip()
                    
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.snake = Snake()
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))

        self.stall1 = Stall(100, 100)
        self.stall1_sprites = pygame.sprite.RenderPlain((self.stall1))

        self.stall2 = Stall(300, 100)
        self.stall2_sprites = pygame.sprite.RenderPlain((self.stall2))

        self.stall3 = Stall(500, 100)
        self.stall3_sprites = pygame.sprite.RenderPlain((self.stall3))

        self.stall4 = Stall(100, 300)
        self.stall4_sprites = pygame.sprite.RenderPlain((self.stall4))

        self.stall5 = Stall(300, 300)
        self.stall5_sprites = pygame.sprite.RenderPlain((self.stall5))

        self.stall6 = Stall(500, 300)
        self.stall6_sprites = pygame.sprite.RenderPlain((self.stall6))

            
        """figure out how many pellets we can display"""
        nNumHorizontal = int(self.width/64)
        nNumVertical = int(self.height/64)       
        # """Create the Pellet group"""
        # self.pellet_sprites = pygame.sprite.Group()
        # """Create all of the pellets and add them to the 
        # pellet_sprites group"""
        # for x in range(nNumHorizontal):
        #     for y in range(nNumVertical):
        #         self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))        


class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('tourist-1.png',-1)
        self.pellets = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 5
        self.y_dist = 5 
        
    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0;
        yMove = 0;
        
        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove,yMove);
        
# class Pellet(pygame.sprite.Sprite):
        
#     def __init__(self, rect=None):
#         pygame.sprite.Sprite.__init__(self) 
#         self.image, self.rect = load_image('pellet.png',-1)
#         if rect != None:
#             self.rect = rect
        
class Stall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('stall-1.png',-1)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

###########################################
# Animation class
# Modified from f12 notes for pygame use
###########################################

class Animation(object):
    # Override these methods when creating your own animation
    def mouseOver(self, event): pass # Feature added to detect mouse cursor.
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def redrawAll(self): pass
    def init(self): pass

    def redrawAllWrapper(self):
    # Redraws and updates canvas.
        self.redrawAll()
        pygame.display.flip() # Updates the canvas.

    def timerFiredWrapper(self):
    # Updates model/canvas according to timerFired.
        self.timerFired()
        self.redrawAllWrapper()
        self.timersPerSec = 40 # times the game loop iterated in last sec
        self.timer.tick(self.timersPerSec) # computes # of ms passed since frame
        pygame.time.delay(self.delay) # pause for a number of ms

    def mouseOverWrapper(self, event):
        self.mouseOver(event)
        self.redrawAllWrapper()

    def mousePressedWrapper(self, event):
        self.mousePressed(event)
        self.redrawAllWrapper()
    
    def keyPressedWrapper(self, event):
        self.keyPressed(event)
        self.redrawAllWrapper()

    def gameLoop(self):
    # Creates game loop for pygame.
        while True: # Sets up game loop
            self.redrawAll()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # quits pygame
                    sys.exit() # exits out of system.
                # If cursor is put on screen.
                if event.type == MOUSEMOTION: self.mouseOverWrapper(event)
                # If mouse is clicked. 
                elif event.type == MOUSEBUTTONUP: \
                                               self.mousePressedWrapper(event)
                if event.type == KEYDOWN: self.keyPressedWrapper(event)
            # set up timerFired events
            self.timerFiredWrapper()
            
    def run(self, width=1280, height=768):
        # need to call init before calling any other commands
        pygame.init()
        pygame.mixer.init() # Sets music
        (self.width, self.height) = (width, height)
        self.delay = 250
        self.timer = pygame.time.Clock() # Initializes timer.
        # Set up window and screen (unique feature of pygame)
        (GUI, colorDepth) = (0, 32) 
        self.canvas = pygame.display.set_mode((width, height), GUI, colorDepth)
        pygame.display.set_caption('In Morocco')
        self.init()
        self.gameLoop() # Load game

class StorePage(Animation):

    #########
    # Model #
    #########

    def init(self):
        sellerImage = ['images/ali.png'] #add location of all 6 seller imgs
        itemsImage = ['images/ring.png', 'images/ring-glow.png']
        self.item1No = 0
        self.item2No = 0
        self.item3No = 0
        self.arrow = pygame.image.load('images/greenarrow.png')
        self.itemsImage = itemsImage
        self.sellerImage = sellerImage

        self.speech1color = (255,255,255)
        self.speech2color = (255,255,255)
        self.speech3color = (255,255,255)
        self.speech4color = (255,255,255)
        self.speech5color = (255,255,255)
        self.speechx = 100
        self.isSpeech1Highlighted = False
        self.isSpeech2Highlighted = False
        self.isSpeech3Highlighted = False
        self.isSpeech4Highlighted = False
        self.isSpeech5Highlighted = False

        self.loadBackground()

    def loadBackground(self):
        self.background = pygame.image.load('images/store.png')
        self.background = pygame.transform.smoothscale(self.background,
                                                (self.width,self.height))
        # gets the rect coords of the background.
        self.bgDimension = self.background.get_rect() 
        self.canvasArea = self.width * self.height

    ###########
    # Control #
    ###########

    def mouseOver(self, event):
        (mouseCx, mouseCy) = pygame.mouse.get_pos()

        if (275 <= mouseCy <= 375):
            if (700 <= mouseCx <= 820):
                self.item1No = 1
            else: 
                self.item1No = 0
            if (840 <= mouseCx <= 960):
                self.item2No = 1
            else: 
                self.item2No = 0
            if (980 <= mouseCx <= 1100):
                self.item3No = 1
            else: 
                self.item3No = 0
        else:
            self.item1No = 0
            self.item2No = 0
            self.item3No = 0

        speechHoverx = 900
        speech1hovery = 560
        speech2hovery = 600
        speech3hovery = 640
        speech4hovery = 680
        speech5hovery = 720
        if (self.speechx <= mouseCx <= speechHoverx):
            if (530 <= mouseCy <= speech1hovery):
                self.speech1color = (215,255,185)
                self.isSpeech1Highlighted = True
            else:
                self.speech1color = (255,255,255)
                self.isSpeech1Highlighted = False
            if (570 <= mouseCy <= speech2hovery):
                self.speech2color = (215,255,185)
                self.isSpeech2Highlighted = True
            else:
                self.speech2color = (255,255,255)
                self.isSpeech2Highlighted = False
            if (610 <= mouseCy <= speech3hovery):
                self.speech3color = (215,255,185)
                self.isSpeech3Highlighted = True
            else:
                self.speech3color = (255,255,255)
                self.isSpeech3Highlighted = False
            if (650 <= mouseCy <= speech4hovery):
                self.speech4color = (215,255,185)
                self.isSpeech4Highlighted = True
            else:
                self.speech4color = (255,255,255)
                self.isSpeech4Highlighted = False
            if (690 <= mouseCy <= speech5hovery):
                self.speech5color = (215,255,185)
                self.isSpeech5Highlighted = True
            else:
                self.speech5color = (255,255,255)
                self.isSpeech5Highlighted = False

    ########
    # View #
    ########

    def drawSpeechOption1(self):
        self.SpeechOption1 = "Salam, how are you today?"
        font = pygame.font.SysFont("Calibri", 26, self.speech1color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption1, antiAlias, self.speech1color)
        self.canvas.blit(text, (self.speechx, 530))

    def highlightSpeech1(self):
        if (self.isSpeech1Highlighted):
            self.canvas.blit(self.arrow, (70, 530))

    def drawSpeechOption2(self):
        self.SpeechOption2 = "Wow everything in your store is so beautiful..."
        font = pygame.font.SysFont("Calibri", 26, self.speech2color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption2, antiAlias, self.speech2color)
        self.canvas.blit(text, (self.speechx, 570))

    def highlightSpeech2(self):
        if (self.isSpeech2Highlighted):
            self.canvas.blit(self.arrow, (70, 570))

    def drawSpeechOption3(self):
        self.SpeechOption3 = "How much for that ring?"
        font = pygame.font.SysFont("Calibri", 26, self.speech3color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption3, antiAlias, self.speech3color)
        self.canvas.blit(text, (self.speechx, 610))

    def highlightSpeech3(self):
        if (self.isSpeech3Highlighted):
            self.canvas.blit(self.arrow, (70, 610))

    def drawSpeechOption4(self):
        self.SpeechOption4 = "Your items look like they're of poor quality."
        font = pygame.font.SysFont("Calibri", 26, self.speech4color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption4, antiAlias, self.speech4color)
        self.canvas.blit(text, (self.speechx, 650))

    def highlightSpeech4(self):
        if (self.isSpeech4Highlighted):
            self.canvas.blit(self.arrow, (70, 650))

    def drawSpeechOption5(self):
        self.SpeechOption5 = "No thanks, I'll just leave. {LEAVE STORE}"
        font = pygame.font.SysFont("Calibri", 26, self.speech5color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption5, antiAlias, self.speech5color)
        self.canvas.blit(text, (self.speechx, 690)) 

    def highlightSpeech5(self):
        if (self.isSpeech5Highlighted):
            self.canvas.blit(self.arrow, (70, 690))      

    def drawSellerText(self):
        sellerText = "Ali: Salam traveler. Welcome to my store! Take a look around, see what you like."    
        white = (255, 255, 255)
        font = pygame.font.SysFont("Calibri", 30, white)
        antiAlias = True # For smoother text.
        text = font.render(sellerText, antiAlias, white)
        self.canvas.blit(text, (50, 480))


    def drawSeller(self):
        #replace sero below with some sort of indicator
        self.curSeller = pygame.image.load(self.sellerImage[0])
        self.canvas.blit(self.curSeller, (35, 150))

    def drawItems(self):
        self.item1 = pygame.image.load(self.itemsImage[self.item1No])
        self.item2 = pygame.image.load(self.itemsImage[self.item2No])
        self.item3 = pygame.image.load(self.itemsImage[self.item3No])
        self.canvas.blit(self.item1, (700, 275))
        self.canvas.blit(self.item2, (840, 275))
        self.canvas.blit(self.item3, (980, 275))

    def redrawAll(self):
        self.canvas.blit(self.background, self.bgDimension)
        #if (not self.gameOver):
        self.drawSeller()
        self.drawItems()
        self.drawSellerText()
        self.drawSpeechOption5()
        #if (self.isItemClicked())
        self.drawSpeechOption1()
        self.drawSpeechOption2()
        self.drawSpeechOption3()
        self.drawSpeechOption4()

        self.highlightSpeech1()
        self.highlightSpeech2()
        self.highlightSpeech3()
        self.highlightSpeech4()
        self.highlightSpeech5()

def runGame():
    startGame = StorePage()
    startGame.run()

        
if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
    
       
