import pygame, sys
import random
import time
from pygame.locals import *

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

def main():
    runGame()

if __name__ == "__main__":
    main()
