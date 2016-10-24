#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *
from helpers import *
import random
import time

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

global_timer = 10000
global_items_left = ["ring"]
global_items_bought = []
global_dict = {"ring": "ring.png",
               "bowl": "bowl.png",
               "spices": "spices.png",
               "purse": "purse.png",
               "rug": "rug.png",
               "slippers": "slippers.png",
               "lantern": "lantern.png"}

global_ali_items = ["ring", "spices", "lantern"]
global_max_ali_prices = [70, 60, 100]
global_base_ali_prices = [45, 40, 65]
global_delta_ali_prices = [7, 4, 7]

global_yasmine_items = ["ring", "purse", "rug"]
global_max_yasmine_prices = [70, 100, 100]
global_base_yasmine_prices = [45, 65, 65]
global_delta_yasmine_prices = [7, 7, 7]

global_omar_items = ["bowl", "slippers", "purse"]
global_max_omar_prices = [70, 70, 100]
global_base_omar_prices = [45, 45, 65]
global_delta_aomar_prices = [7, 7, 7]


class PyManMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, itemsLeft, width=1280,height=768):
        """Initialize"""
        global global_items_left
        global_items_left = itemsLeft
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
                        self.player.move(event.key)
                        
            # """Check for collision"""
            # lstCols = pygame.sprite.spritecollide(self.player
            #                                      , self.pellet_sprites
            #                                      , True)
            # """Update the amount of pellets eaten"""
            # self.player.pellets = self.player.pellets + len(lstCols)
            collide1 = pygame.sprite.collide_rect(self.player, self.stall1)
            collide2 = pygame.sprite.collide_rect(self.player, self.stall2)
            collide3 = pygame.sprite.collide_rect(self.player, self.stall3)
            collide4 = pygame.sprite.collide_rect(self.player, self.stall4)
            collide5 = pygame.sprite.collide_rect(self.player, self.stall5)
            collide6 = pygame.sprite.collide_rect(self.player, self.stall6)

            if collide1:
                print "Stall 1"
                runGame(AliPage())

            elif collide2:
                print "Stall 2"
                runGame(YasminePage())

            elif collide3:
                print "Stall 3"
                runGame(OmarPage())

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
            #     text = font.render("Pellets %s" % self.player.pellets
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

            self.khalid_sprites.draw(self.screen)
            self.omar_sprites.draw(self.screen)
            self.yasmine_sprites.draw(self.screen)
            self.salma_sprites.draw(self.screen)
            self.youssef_sprites.draw(self.screen)
            self.ali_sprites.draw(self.screen)

            self.tree1_sprites.draw(self.screen)
            self.tree2_sprites.draw(self.screen)

            self.player_sprites.draw(self.screen)
            
            self.house_sprites.draw(self.screen)
            self.house2_sprites.draw(self.screen)
            self.house3_sprites.draw(self.screen)
            

            pygame.draw.rect(self.screen, (224, 224, 209),
                             Rect((0,500), (1500,300)))

            myfont = pygame.font.SysFont("monospace", 15)
            
            global global_timer
            global_timer -= 10

            if global_timer == 0 or global_items_left == []:
                endScreen = EndLevel()
                endScreen.main()
                print "done"

            # render text
            timeLeft = myfont.render("Time Remaining: " + str(global_timer/100), 1, (0,0,0))
            self.screen.blit(timeLeft, (50, 520))
            startX = 100
            pathTo = global_dict
            itemsLeft = myfont.render("Items To Buy", 1, (0,0,0))
            self.screen.blit(itemsLeft, (50, 550))
            for item in global_items_left:
                self.item = StaticImage(startX, 640, pathTo[item])
                self.item_sprites = pygame.sprite.RenderPlain((self.item))
                self.item_sprites.draw(self.screen)
                startX += 120
           

            pygame.display.flip()
                    
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.player = Player()
        self.player_sprites = pygame.sprite.RenderPlain((self.player))

        #Stalls
        self.stall1 = StaticImage(100, 100, 'stall-1.png')
        self.stall1_sprites = pygame.sprite.RenderPlain((self.stall1))

        self.stall2 = StaticImage(300, 100, 'stall-1.png')
        self.stall2_sprites = pygame.sprite.RenderPlain((self.stall2))

        self.stall3 = StaticImage(500, 100, 'stall-1.png')
        self.stall3_sprites = pygame.sprite.RenderPlain((self.stall3))

        self.stall4 = StaticImage(100, 350, 'stall-1.png')
        self.stall4_sprites = pygame.sprite.RenderPlain((self.stall4))

        self.stall5 = StaticImage(300, 350, 'stall-1.png')
        self.stall5_sprites = pygame.sprite.RenderPlain((self.stall5))

        self.stall6 = StaticImage(500, 350, 'stall-1.png')
        self.stall6_sprites = pygame.sprite.RenderPlain((self.stall6))

        #Storekeepers
        self.khalid = StaticImage(140, 120, 'khalid.png')
        self.khalid_sprites = pygame.sprite.RenderPlain((self.khalid))

        self.omar = StaticImage(270, 120, 'omar.png')
        self.omar_sprites = pygame.sprite.RenderPlain((self.omar))

        self.yasmine = StaticImage(500, 120, 'yasmine.png')
        self.yasmine_sprites = pygame.sprite.RenderPlain((self.yasmine))        

        self.salma = StaticImage(70, 370, 'salma.png')
        self.salma_sprites = pygame.sprite.RenderPlain((self.salma))       
         
        self.youssef = StaticImage(340, 390, 'youssef.png')
        self.youssef_sprites = pygame.sprite.RenderPlain((self.youssef))       
        
        self.ali = StaticImage(470, 370, 'ali.png')
        self.ali_sprites = pygame.sprite.RenderPlain((self.ali))       
        
        #Decorative
        self.house = StaticImage(700, 300, 'house.png')
        self.house_sprites = pygame.sprite.RenderPlain((self.house))       
        
        self.house2 = StaticImage(800, 150, 'house2.png')
        self.house2_sprites = pygame.sprite.RenderPlain((self.house2)) 

        self.house3 = StaticImage(950, 200, 'house3.png')
        self.house3_sprites = pygame.sprite.RenderPlain((self.house3))

        self.tree1 = StaticImage(400, 150, 'tree.png')
        self.tree1_sprites = pygame.sprite.RenderPlain((self.tree1)) 

        self.tree2 = StaticImage(200, 250, 'tree.png')
        self.tree2_sprites = pygame.sprite.RenderPlain((self.tree2)) 

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


class Player(pygame.sprite.Sprite):
    """This is our player that will move around the screen"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.images = ['data/images/tourist-1.png','data/images/tourist-2.png']
        self.counter = 0
        self.image = pygame.image.load(self.images[self.counter])
        self.rect = self.image.get_rect()
        # self.image, self.rect = load_image('tourist-1.png',-1)
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
        
        self.counter = (self.counter + 1) % len(self.images)
        self.image = pygame.image.load(self.images[self.counter])
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove,yMove);
        

class StaticImage(pygame.sprite.Sprite):

    def __init__(self, x, y, path):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image(path,-1)
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
        self.delay = 50
        self.timer = pygame.time.Clock() # Initializes timer.
        # Set up window and screen (unique feature of pygame)
        (GUI, colorDepth) = (0, 32) 
        self.canvas = pygame.display.set_mode((width, height), GUI, colorDepth)
        pygame.display.set_caption('In Morocco')
        self.init()
        self.gameLoop() # Load game

class EndLevel():
    # Initialise screen
    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 768))
        pygame.display.set_caption('Basic Pygame program')

        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        # Display some text
        font = pygame.font.Font(None, 36)
        text = font.render("Level Complete!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        textpos.centery = 120
        background.blit(text, textpos)

        # Display some text
        bought = font.render("Items Bought: " + str(len(global_items_bought)), 1, (10, 10, 10))
        boughtpos = bought.get_rect()
        boughtpos.centerx = background.get_rect().centerx
        boughtpos.centery = 170
        background.blit(bought, boughtpos)

        # Display some text
        left = font.render("Items Remaining: " + str(len(global_items_left)), 1, (10, 10, 10))
        leftpos = bought.get_rect()
        leftpos.centerx = background.get_rect().centerx
        leftpos.centery = 200
        background.blit(left, leftpos)

        # Display some text
        score = font.render("Your Score: " + str(len(global_items_bought) * 10), 1, (10, 10, 10))
        scorepos = bought.get_rect()
        scorepos.centerx = background.get_rect().centerx
        scorepos.centery = 250
        background.blit(score, scorepos)

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
        # Event loop
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            screen.blit(background, (0, 0))
            pygame.display.flip()


class StorePage(Animation):

    #########
    # Model #
    #########

    def init(self):
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        self.globalindex = -1
        self.loadItemsData()
        self.moodBar = 5
        self.assignWeights()
        self.itemClicked = "NULL"
        self.loadPlayerSpeech()

        self.isItHaggleTime = False
        self.loadHaggleData()
        sellerImage = 'images/ali.png' #add location of all 6 seller imgs
        self.sellerImage = sellerImage
        self.loadSpeechData()
        self.loadSpeechOptionVars()
        self.loadBackground()



    def loadBackground(self):
        self.background = pygame.image.load('images/store.png')
        self.background = pygame.transform.smoothscale(self.background,
                                                (self.width,self.height))
        # gets the rect coords of the background.
        self.bgDimension = self.background.get_rect() 
        self.canvasArea = self.width * self.height

    def loadSpeechData(self):
        self.arrow = pygame.image.load('images/greenarrow.png')
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
        self.isThanksHighlighted = False

        #for mouse events
        self.speechHoverx = 900
        self.speech1hovery = 560
        self.speech2hovery = 600
        self.speech3hovery = 640
        self.speech4hovery = 680
        self.speech5hovery = 720

    def loadItemsData(self):
        self.totalItems = 0 #actual no of items are this +1
        self.itemsImage = ['images/ring.png', 'images/ring-glow.png']
        self.item1Glow = 0 #even no = no glow
        self.item2Glow = 0
        self.item3Glow = 0
        self.isItem1Clicked = False
        self.isItem2Clicked = False
        self.isItem3Clicked = False

    def isAnyItemClicked(self):
        if (self.isItem1Clicked == self.isItem2Clicked == 
            self.isItem3Clicked == False):
            return False
        else: 
            return True

    def loadSpeechOptionVars(self):
        self.speechLayer = 0
        self.sellerResponse = 0
        self.speechClicked = 100

        self.sellerText = ["""Ali: Salam traveler. Welcome to my store! Take a look around, see what you like.""", 
        "Ali: Fine, thank you. Do you see anything you like?",
        "Ali: Oh... thanks. What do you need?",
        "Ali: ... What do you want?",
        "Ali:If you think that, then leave",
        "Ali: I ask for %dDH. Thats a great price!" % self.curSellerOffer,
        "Ali: Accepted. Thank you for your business.",
        "Ali: I'll take %dDH, no less" % (self.curSellerOffer)]        

    def loadHaggleData(self):
        self.haggleTime = False
        self.offerAccepted = False
        self.isSellerAngry = False

        self.playerOffer = ""
        self.offerLengthLimit = 3
        self.offerLength = 0

        self.sellerStrikes = 0
        self.curSellerOffer = global_base_ali_prices[self.globalindex]

    def assignWeights(self):
        self.SpeechOption1Weights = [-3, 0, 0]
        self.SpeechOption2Weights = [0, 3, -1]
        self.SpeechOption3Weights = [3, -2, 0]
        self.SpeechOption4Weights = [0, 3, -1]

    def offerReset(self):
        self.playerOffer = ""
        self.offerLength = 0

    def haggleJudge(self):
        playerOffer = int(self.playerOffer)
        if (playerOffer >= self.curSellerOffer):
            self.offerAccepted = True
        elif (self.sellerStrikes == 0):
            self.curSellerOffer = random.randint(int(0.75*self.curSellerOffer), int(0.85*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Ali: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes == 1):
            self.curSellerOffer = random.randint(int(0.5*self.curSellerOffer), int(0.75*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Ali: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes == 2):
            self.curSellerOffer = random.randint(int(0.3*self.curSellerOffer), int(0.5*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Ali: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes > 2):
            if (playerOffer >= 0.3*self.curSellerOffer):
                self.offerAccepted = True
            elif (playerOffer < 0.3*self.curSellerOffer):
                self.isSellerAngry = True
                self.sellerText[7] = "Ali: You have bothered me enough. Leave."
            else:
                self.curSellerOffer = random.randint(int(0.25*self.curSellerOffer), int(0.4*self.curSellerOffer))
                self.sellerText[7] = "Ali: I'll take %d, no less" % (self.curSellerOffer)
        self.offerReset()


    ###########
    # Control #
    ###########

    def keyPressed(self, event):
        if (self.offerAccepted == False and self.haggleTime 
            and self.offerLength != self.offerLengthLimit):
            if (event.key == K_0 and self.offerLength != 0):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "0"
            if (event.key == K_1):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "1"
            if (event.key == K_2):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "2"
            if (event.key == K_3):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "3"
            if (event.key == K_4):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "4"
            if (event.key == K_5):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "5"
            if (event.key == K_6):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "6"
            if (event.key == K_7):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "7"
            if (event.key == K_8):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "8"
            if (event.key == K_9):
                self.offerLength = self.offerLength + 1
                self.playerOffer = self.playerOffer + "9" 
        if (self.offerAccepted == False and self.haggleTime):
            if (event.key == K_BACKSPACE):
                self.offerReset()
        if (self.offerLength != 0 and self.offerAccepted == False 
            and self.haggleTime):
               if (event.key == K_RETURN):
                    #print "Pressed!"
                    #self.playerOffer = ""
                    #self.offerLength = 0
                    self.haggleJudge()
                    #print self.curSellerOffer

    def adjustWeights(self):
        delta = self.SpeechOption1Weights[self.speechLayer-1]*global_delta_ali_prices[self.globalindex]
        self.curSellerOffer+= delta

    def mousePressed(self, event):
        (mouseCx, mouseCy) = pygame.mouse.get_pos()
        if (275 <= mouseCy <= 375):
            if (700 <= mouseCx <= 820):
                self.isItem1Clicked = True
                self.isItem2Clicked = False
                self.isItem3Clicked = False
            if (840 <= mouseCx <= 960):
                self.isItem1Clicked = False
                self.isItem2Clicked = True
                self.isItem3Clicked = False
            if (980 <= mouseCx <= 1100):
                self.isItem1Clicked = False
                self.isItem2Clicked = False
                self.isItem3Clicked = True

        #if (self.offerAccepted == False and self.speechLayer ==)

        if (self.offerAccepted == False and self.speechLayer != 3 and
            self.speechx <= mouseCx <= self.speechHoverx):
            if (530 <= mouseCy <= self.speech1hovery):
                self.speechClicked = 1
                self.speechLayer = self.speechLayer + 1
                self.adjustWeights() 
            if (570 <= mouseCy <= self.speech2hovery):
                self.speechClicked = 2
                self.speechLayer = self.speechLayer + 1
                self.adjustWeights() 
            if (610 <= mouseCy <= self.speech3hovery):
                self.speechClicked = 3
                self.speechLayer = self.speechLayer + 1
                self.adjustWeights() 
            if (650 <= mouseCy <= self.speech4hovery):
                self.speechClicked = 4
                self.speechLayer = self.speechLayer + 1
                self.adjustWeights() 
            if (690 <= mouseCy <= self.speech5hovery):
                self.speechClicked = 5

        if (self.offerAccepted == False and self.haggleTime and 
            self.speechx <= mouseCx <= self.speechHoverx):
            if (530 <= mouseCy <= self.speech1hovery):
                self.offerAccepted = True 

            if (690 <= mouseCy <= self.speech5hovery):
                MainWindow = PyManMain(["bowl", "spices", "purse", "rug", "slippers", "lantern"])
                MainWindow.MainLoop()

        if (self.offerAccepted and self.speechx <= mouseCx <= self.speechHoverx):
            if (530 <= mouseCy <= self.speech1hovery):
                MainWindow = PyManMain(["bowl", "spices", "purse", "rug", "slippers", "lantern"])
                MainWindow.MainLoop()


    def mouseOver(self, event):
        (mouseCx, mouseCy) = pygame.mouse.get_pos()

        if (275 <= mouseCy <= 375):
            if (700 <= mouseCx <= 820):
                self.item1Glow = 1
            elif (not self.isItem1Clicked): 
                self.item1Glow = 0
            if (840 <= mouseCx <= 960):
                self.item2Glow = 1
            elif (not self.isItem2Clicked): 
                self.item2Glow = 0
            if (980 <= mouseCx <= 1100):
                self.item3Glow = 1
            elif (not self.isItem3Clicked): 
                self.item3Glow = 0
        else:
            if (not self.isItem1Clicked):
                self.item1Glow = 0
            if (not self.isItem2Clicked):
                self.item2Glow = 0
            if (not self.isItem3Clicked):
                self.item3Glow = 0

        
        if (self.speechx <= mouseCx <= self.speechHoverx):
            if (530 <= mouseCy <= self.speech1hovery):
                self.speech1color = (215,255,185)
                if (self.offerAccepted == False):
                    self.isSpeech1Highlighted = True
                else: isThanksHighlighted = True
            else:
                self.speech1color = (255,255,255)
                self.isSpeech1Highlighted = False
            if (570 <= mouseCy <= self.speech2hovery):
                self.speech2color = (215,255,185)
                self.isSpeech2Highlighted = True
            else:
                self.speech2color = (255,255,255)
                self.isSpeech2Highlighted = False
            if (610 <= mouseCy <= self.speech3hovery):
                self.speech3color = (215,255,185)
                self.isSpeech3Highlighted = True
            else:
                self.speech3color = (255,255,255)
                self.isSpeech3Highlighted = False
            if (650 <= mouseCy <= self.speech4hovery):
                self.speech4color = (215,255,185)
                self.isSpeech4Highlighted = True
            else:
                self.speech4color = (255,255,255)
                self.isSpeech4Highlighted = False
            if (690 <= mouseCy <= self.speech5hovery):
                self.speech5color = (215,255,185)
                self.isSpeech5Highlighted = True
            else:
                self.speech5color = (255,255,255)
                self.isSpeech5Highlighted = False

    def loadPlayerSpeech(self):
        #global_yasmine_items = ["ring", "purse", "rug"]
        if (self.isItem1Clicked):
            self.globalindex = 0
            self.itemClicked = global_ali_items[self.globalindex]
        elif (self.isItem2Clicked):
            self.globalindex = 1
            self.itemClicked = global_ali_items[self.globalindex]
        elif (self.isItem3Clicked):
            self.globalindex = 2
            self.itemClicked = global_ali_items[self.globalindex]

        self.SpeechOption1 = ["Salam, how are you today?", 
        "How much for the %s?" % self.itemClicked, "Deal!", "Thank you."]
        self.SpeechOption2 = ["Wow everything in your store is so beautiful...",
        "The %s, peasant. How much?" % self.itemClicked, "Too expensive! {HAGGLE}"]
        self.SpeechOption3 = ["I just want to buy my things and leave", 
        "I need that %s! How much?" % self.itemClicked, "Don't try to rip me off! {HAGGLE}"]
        self.SpeechOption4 = ["Your items look like they're of poor quality.",
        "That's a beautiful %s! How much?" % self.itemClicked, "How about I propose a price? {HAGGLE}"]
        self.SpeechOption5 = ["No thanks, I'll just leave. {LEAVE STORE}"]


    def timerFired(self):
        self.loadPlayerSpeech()

    ########
    # View #
    ########

    def drawSpeechOption1(self):
        if (not self.isAnyItemClicked()):
            speech = self.SpeechOption5
        else:
            speech = self.SpeechOption1
        font = pygame.font.SysFont("Calibri", 26, self.speech1color)
        antiAlias = True # For smoother text.
        text = font.render(speech[self.speechLayer], 
            antiAlias, self.speech1color)
        self.canvas.blit(text, (self.speechx, 530))

    def highlightSpeech1(self):
        if (self.isSpeech1Highlighted):
            self.canvas.blit(self.arrow, (70, 530))

    def drawSpeechOption2(self):
        font = pygame.font.SysFont("Calibri", 26, self.speech2color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption2[self.speechLayer], 
            antiAlias, self.speech2color)
        self.canvas.blit(text, (self.speechx, 570))

    def highlightSpeech2(self):
        if (self.isSpeech2Highlighted and self.isAnyItemClicked()
            and self.offerAccepted == False
            and not self.haggleTime):
            self.canvas.blit(self.arrow, (70, 570))

    def drawSpeechOption3(self):
        font = pygame.font.SysFont("Calibri", 26, self.speech3color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption3[self.speechLayer], 
            antiAlias, self.speech3color)
        self.canvas.blit(text, (self.speechx, 610))

    def highlightSpeech3(self):
        if (self.isSpeech3Highlighted and self.isAnyItemClicked()
            and self.offerAccepted == False
            and not self.haggleTime):
            self.canvas.blit(self.arrow, (70, 610))

    def drawSpeechOption4(self):
        font = pygame.font.SysFont("Calibri", 26, self.speech4color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption4[self.speechLayer], 
            antiAlias, self.speech4color)
        self.canvas.blit(text, (self.speechx, 650))

    def highlightSpeech4(self):
        if (self.isSpeech4Highlighted and self.isAnyItemClicked()
            and self.offerAccepted == False
            and not self.haggleTime):
            self.canvas.blit(self.arrow, (70, 650))

    def drawSpeechOption5(self):
        font = pygame.font.SysFont("Calibri", 26, self.speech5color)
        antiAlias = True # For smoother text.
        text = font.render(self.SpeechOption5[0], 
            antiAlias, self.speech5color)
        self.canvas.blit(text, (self.speechx, 690)) 

    def highlightSpeech5(self):
        if (self.isSpeech5Highlighted and self.isAnyItemClicked()
            and self.offerAccepted == False):
            self.canvas.blit(self.arrow, (70, 690))

    def drawThanks(self):
        font = pygame.font.SysFont("Calibri", 26, self.speech2color)
        antiAlias = True # For smoother text.
        text = font.render("Thank you. {LEAVE}", 
            antiAlias, self.speech1color)
        self.canvas.blit(text, (self.speechx, 530))

    def highlightThanks(self):
        if (self.isThanksHighlighted and self.offerAccepted):
            self.canvas.blit(self.arrow, (70, 530))

    def drawHaggle(self):
        if (self.speechClicked == 1 or self.offerAccepted):
            self.sellerResponse = 6
            self.offerAccepted = True
            self.drawThanks()
            #draw thank you
            #remove item from display
            #ask if player wants anything else
        else:
            self.haggleTime = True
            self.sellerResponse = 7
            font = pygame.font.SysFont("Calibri", 26, self.speech3color)
            antiAlias = True # For smoother text.
            text1 = font.render("I accept your offer.", antiAlias, self.speech1color)
            text2 = font.render("Your Offer: %s" %(self.playerOffer), antiAlias, self.speech3color)
            text3 = font.render("No thanks, I'll just leave. {LEAVE}", antiAlias, self.speech5color)
            self.canvas.blit(text1, (self.speechx, 530))
            self.canvas.blit(text2, (self.speechx, 610))
            self.canvas.blit(text3, (self.speechx, 690))
            #something that displays haggling controls


    def chagingSellerResponse(self):
        #if self.offerAccepted == True:
            #self.drawThanks()
            #print "accepted"
            #MainWindow = PyManMain(["bowl", "spices", "purse", "rug", "slippers", "lantern"])
            #MainWindow.MainLoop()
        if (self.speechLayer == 1 and self.isAnyItemClicked()):
            if (self.speechClicked == 1):
                self.sellerResponse = 1
            elif (self.speechClicked == 2):
                self.sellerResponse = 2
            elif (self.speechClicked == 3):
                self.sellerResponse = 3
            elif (self.speechClicked == 4):
                self.sellerResponse = 4
            elif (self.speechClicked == 5):
                MainWindow = PyManMain(["ring", "bowl", "spices", "purse", "rug", "slippers", "lantern"])
                MainWindow.MainLoop()

        if (self.speechLayer == 2 and self.isAnyItemClicked()):
        #and item clicked
            self.sellerResponse = 5
        if (self.speechLayer == 3 and self.isAnyItemClicked()):
            self.drawHaggle()      

    def drawSellerText(self):
        white = (255, 255, 255)
        font = pygame.font.SysFont("Calibri", 30, white)
        antiAlias = True # For smoother text.
        text = font.render(self.sellerText[self.sellerResponse], 
            antiAlias, white)
        self.canvas.blit(text, (50, 480))


    def drawSeller(self):
        #replace sero below with some sort of indicator
        self.curSeller = pygame.image.load(self.sellerImage)
        self.canvas.blit(self.curSeller, (35, 150))

    def drawItems(self):
        pathTo = global_dict
        startX = 750
        for item in global_ali_items: #HARDCODED
            self.item = StaticImage(startX, 325, pathTo[item])
            self.item_sprites = pygame.sprite.RenderPlain((self.item))
            self.item_sprites.draw(self.screen)
            startX+= 140
        #self.item1 = pygame.image.load(global_dict[0])
        #self.item2 = pygame.image.load(global_dict[2])
        #self.item3 = pygame.image.load(global_dict[6])
        #self.canvas.blit(self.item1, (700, 275))
        #self.canvas.blit(self.item2, (840, 275))
        #self.canvas.blit(self.item3, (980, 275))

    def redrawAll(self):
        self.canvas.blit(self.background, self.bgDimension)
        #if (not self.gameOver):
        self.drawSeller()
        self.drawItems()
        self.chagingSellerResponse()
        self.drawSellerText()
        if (self.offerAccepted == False and not self.haggleTime):
            self.drawSpeechOption1()
        if (self.isAnyItemClicked() and not self.offerAccepted and
            self.speechLayer != 3):
            self.drawSpeechOption2()
            self.drawSpeechOption3()
            self.drawSpeechOption4()
            self.drawSpeechOption5()

        self.highlightSpeech1()
        self.highlightSpeech2()
        self.highlightSpeech3()
        self.highlightSpeech4()
        self.highlightSpeech5()
        self.highlightThanks()

class AliPage(StorePage):


    #########
    # Model #
    #########


    def loadBackground(self):
        self.background = pygame.image.load('images/store.png')
        self.background = pygame.transform.smoothscale(self.background,
                                                (self.width,self.height))
        # gets the rect coords of the background.
        self.bgDimension = self.background.get_rect() 
        self.canvasArea = self.width * self.height

class YasminePage(StorePage):

    #########
    # Model #
    #########

    def init(self):
        self.globalindex = 0
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        self.isItHaggleTime = False
        self.loadHaggleData()
        self.loadItemsData()
        sellerImage = 'images/yasmine.png' #add location of all 6 seller imgs
        self.sellerImage = sellerImage
        self.loadSpeechData()
        self.loadSpeechOptionVars()
        self.loadBackground()

        self.itemClicked = "NULL"
        self.loadPlayerSpeech()
        self.moodBar = 5
        self.assignWeights()

    def loadBackground(self):
        self.background = pygame.image.load('images/store2.png')
        self.background = pygame.transform.smoothscale(self.background,
                                                (self.width,self.height))
        # gets the rect coords of the background.
        self.bgDimension = self.background.get_rect() 
        self.canvasArea = self.width * self.height

    def loadSpeechOptionVars(self):
        self.speechLayer = 0
        self.sellerResponse = 0
        self.speechClicked = 100
        self.sellerText = ["Yasmine: Salam, traveler.",
        "Yasmine: Ah, so far away! What do you need?",
        "Yasmine: .....",
        "Yasmine: Well, yes. See if you like them",
        "Yasmine: So, what do you need?",
        "Yasmine: I ask for %s dirhams. It's the best price you'll find." % (self.curSellerOffer),
        "Yasmine: Accepted. Thank you for your business.",
        "Yasmine: I'll take %d dirhams, no less." % (self.curSellerOffer)]

    def loadHaggleData(self):
        self.haggleTime = False
        self.offerAccepted = False
        self.isSellerAngry = False

        self.playerOffer = ""
        self.offerLengthLimit = 3
        self.offerLength = 0

        self.sellerStrikes = 0
        self.curSellerOffer = global_base_yasmine_prices[self.globalindex]

    def haggleJudge(self):
        playerOffer = int(self.playerOffer)
        if (playerOffer >= self.curSellerOffer):
            self.offerAccepted = True
        elif (self.sellerStrikes == 0):
            self.curSellerOffer = random.randint(int(0.75*self.curSellerOffer), int(0.85*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Yasmine: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes == 1):
            self.curSellerOffer = random.randint(int(0.5*self.curSellerOffer), int(0.75*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Yasmine: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes == 2):
            self.curSellerOffer = random.randint(int(0.3*self.curSellerOffer), int(0.5*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Yasmine: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes > 2):
            if (playerOffer >= 0.3*self.curSellerOffer):
                self.offerAccepted = True
            elif (playerOffer < 0.3*self.curSellerOffer):
                self.isSellerAngry = True
                self.sellerText[7] = "Yasmine: You have bothered me enough. Leave."
            else:
                self.curSellerOffer = random.randint(int(0.25*self.curSellerOffer), int(0.4*self.curSellerOffer))
                self.sellerText[7] = "Yasmine: I'll take %d, no less" % (self.curSellerOffer)
        self.offerReset()
    ##############
    # Controller #
    ##############

    def loadPlayerSpeech(self):
        #global_yasmine_items = ["ring", "purse", "rug"]
        self.globalindex = 0
        if (self.isItem1Clicked):
            self.globalindex = 0
            self.itemClicked = global_yasmine_items[self.globalindex]
        elif (self.isItem2Clicked):
            self.globalindex = 1
            self.itemClicked = global_yasmine_items[self.globalindex]
        elif (self.isItem3Clicked):
            self.globalindex = 2
            self.itemClicked = global_yasmine_items[self.globalindex]

        self.SpeechOption1 = ["Salam, that's correct!", 
        "How much for the %s?" % self.itemClicked, "Deal!", "Thank you."]
        self.SpeechOption2 = ["Wow everything in your store is so beautiful...",
        "The %s, peasant. How much?" % self.itemClicked, "Too expensive! {HAGGLE}"]
        self.SpeechOption3 = ["I just want to buy my things and leave", 
        "I need that %s! How much?" % self.itemClicked, "Don't try to rip me off! {HAGGLE}"]
        self.SpeechOption4 = ["Your items look like they're of poor quality.",
        "That's a beautiful %s! How much?" % self.itemClicked, "How about I propose a price? {HAGGLE}"]
        self.SpeechOption5 = ["No thanks, I'll just leave. {LEAVE STORE}"]

    def timerFired(self):
        self.loadPlayerSpeech()

    ########
    # View #
    ########

    def drawItems(self):
        pathTo = global_dict
        startX = 750
        for item in global_yasmine_items: #HARDCODED
            self.item = StaticImage(startX, 325, pathTo[item])
            self.item_sprites = pygame.sprite.RenderPlain((self.item))
            self.item_sprites.draw(self.screen)
            startX+= 140

class OmarPage(StorePage):

    #########
    # Model #
    #########

    def init(self):
        self.globalindex = 0
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        self.isItHaggleTime = False
        self.loadHaggleData()
        self.loadItemsData()
        sellerImage = 'images/omar.png' #add location of all 6 seller imgs
        self.sellerImage = sellerImage
        self.loadSpeechData()
        self.loadSpeechOptionVars()
        self.loadBackground()

        self.itemClicked = "NULL"
        self.loadPlayerSpeech()
        self.moodBar = 5
        self.assignWeights()

    def loadBackground(self):
        self.background = pygame.image.load('images/store.png')
        self.background = pygame.transform.smoothscale(self.background,
                                                (self.width,self.height))
        # gets the rect coords of the background.
        self.bgDimension = self.background.get_rect() 
        self.canvasArea = self.width * self.height

    def loadSpeechOptionVars(self):
        self.speechLayer = 0
        self.sellerResponse = 0
        self.speechClicked = 100
        self.sellerText = ["Omar: You break it, you buy it. What do you need?",
        "Omar: Hmph, good.",
        "Omar: Are you mocking me?",
        "Omar: If you don't like it then leave.",
        "Omar: ...So, what do you need?",
        "Omar: %s dirhams. And that's my FINAL offer." % (self.curSellerOffer),
        "Omar: Accepted. Thank you for your business.",
        "Omar: I'll take %d dirhams, no less." % (self.curSellerOffer)]

    def loadPlayerSpeech(self):
        #global_omar_items = ["bowl", "slippers", "purse"]
        if (self.isItem1Clicked):
            self.globalindex = 0
            self.itemClicked = global_omar_items[self.globalindex]
        elif (self.isItem2Clicked):
            self.globalindex = 1
            self.itemClicked = global_omar_items[self.globalindex]
        elif (self.isItem3Clicked):
            self.globalindex = 2
            self.itemClicked = global_omar_items[self.globalindex]

        self.SpeechOption1 = ["Salam, I'll keep that in mind.", 
        "How much for the %s?" % self.itemClicked, "Deal!", "Thank you."]
        self.SpeechOption2 = ["I would never want to break anything in this store, brother.",
        "The %s, peasant. How much?" % self.itemClicked, "Too expensive! {HAGGLE}"]
        self.SpeechOption3 = ["That's a horrible way to treat buyers, you know", 
        "I need that %s! How much?" % self.itemClicked, "Don't try to rip me off! {HAGGLE}"]
        self.SpeechOption4 = ["I just want to buy things.....",
        "That's a beautiful %s! How much?" % self.itemClicked, "How about I propose a price? {HAGGLE}"]
        self.SpeechOption5 = ["No thanks, I'll just leave. {LEAVE STORE}"]

    def loadHaggleData(self):
        self.haggleTime = False
        self.offerAccepted = False
        self.isSellerAngry = False

        self.playerOffer = ""
        self.offerLengthLimit = 3
        self.offerLength = 0

        self.sellerStrikes = 0
        self.curSellerOffer = global_base_omar_prices[self.globalindex]

    def haggleJudge(self):
        playerOffer = int(self.playerOffer)
        if (playerOffer >= self.curSellerOffer):
            self.offerAccepted = True
        elif (self.sellerStrikes == 0):
            self.curSellerOffer = random.randint(int(0.75*self.curSellerOffer), int(0.85*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Omar: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes == 1):
            self.curSellerOffer = random.randint(int(0.5*self.curSellerOffer), int(0.75*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Omar: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes == 2):
            self.curSellerOffer = random.randint(int(0.3*self.curSellerOffer), int(0.5*self.curSellerOffer))
            self.sellerStrikes = self.sellerStrikes + 1
            self.sellerText[7] = "Omar: I'll take %d, no less" % (self.curSellerOffer)
        elif (self.sellerStrikes > 2):
            if (playerOffer >= 0.3*self.curSellerOffer):
                self.offerAccepted = True
            elif (playerOffer < 0.3*self.curSellerOffer):
                self.isSellerAngry = True
                self.sellerText[7] = "Omar: You have bothered me enough. Leave."
            else:
                self.curSellerOffer = random.randint(int(0.25*self.curSellerOffer), int(0.4*self.curSellerOffer))
                self.sellerText[7] = "Omar: I'll take %d, no less" % (self.curSellerOffer)
        self.offerReset()

    def timerFired(self):
        self.loadPlayerSpeech()

    ########
    # View #
    ########

    def drawItems(self):
        pathTo = global_dict
        startX = 750
        for item in global_omar_items: #HARDCODED
            self.item = StaticImage(startX, 325, pathTo[item])
            self.item_sprites = pygame.sprite.RenderPlain((self.item))
            self.item_sprites.draw(self.screen)
            startX+= 140




def runGame(page):
    startGame = page

    startGame.run()

        
if __name__ == "__main__":
    MainWindow = PyManMain(["ring", "bowl", "spices", "purse", "rug", "slippers", "lantern"])
    MainWindow.MainLoop()
    # endlevel = EndLevel()
    # endlevel.main()
    
       
