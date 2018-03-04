# Paint Project Created by Andrew Gao
# Super Smash Bros 4 Themed Paint Clone

import tkinter as tk
from random import *
from tkinter import filedialog
import os
from pygame import *
from math import *

# Setup and Initialize
root = tk.Tk()
root.withdraw()
init()

# FPS Clock
clock = time.Clock()

# Gameloop
running = True

# Current screen
currentScreen = "Menu"

# File name used for saving
fileName = "Untitled"

# Undo/Redo Lists
undoList = []
redoList = []

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (192,192,192)

# Data Storing Variables
attemptLoadFile = False  # Try to load a valid image (used for Load Button)
tool = "" # Stores which tool is currently active
music = True # Music
size = 10 # Size of tools
colour = BLACK # Default colour
UI = False # UI is only drawn once
Loaded = False # Loaded img is only drawn once
rectFill = False # Fill rectangle or not
circFill = False # Fill ellipse or not
polyFill = False # Fill polygon or not
textFont = "" # Font Selected
textContent = "" # Stores user input
stampSelected = "" # Current stamp selected
w = 50 # width of img
h = 50 # height of img
text_rendered = [] # List for rendering text on canvas
useFont = font.Font("fonts/smash.ttf", size) # Default font
polygonList = [] # List for polygon points
helpOn = False # Display help screen or not
helpFont = font.Font("fonts/smash.ttf", 14) # Font for help text

# Import UI images
wall1 = image.load("graphics/winG.png") # Window Graphic
menuWin = image.load("graphics/MenuWin.png") # Window Graphic
colourPicker = image.load("graphics/col.jpg")  # Colour Picker
wallpaper = transform.scale(image.load("graphics/wallpaper.png"),(1280,720)) # Wallpaper
drawingWin = image.load("graphics/drawing.png")  # Drawing Window
helpScr = image.load("graphics/helpScr.png") # Help window
redraw1 = image.load("graphics/redraw1.png") # Thickness redraw window
redraw2 = image.load("graphics/redraw2.png") # Help redraw window

# Import Icons
newFile2 = transform.scale(image.load("icons/newFileBig.png"), (200, 200))
loadFile2 = transform.scale(image.load("icons/loadFileBig.png"), (200, 200))
newFile2G = transform.scale(image.load("icons/newFileBigG.png"), (200, 200))
loadFile2G = transform.scale(image.load("icons/loadFileBigG.png"), (200, 200))
brush = transform.scale(image.load("icons/paintbrush.png"), (50, 50))
eraser = transform.scale(image.load("icons/eraser.png"), (50, 50))
dropper = transform.scale(image.load("icons/dropper.png"), (50, 50))
polygon = transform.scale(image.load("icons/polygon.png"), (50, 50))
text = transform.scale(image.load("icons/text.png"), (50, 50))
spray = transform.scale(image.load("icons/spray.png"), (50, 50))
stamp = transform.scale(image.load("icons/stamp.png"), (50, 50))
fill = transform.scale(image.load("icons/fill.png"), (50, 50))
mute = transform.scale(image.load("icons/volumemute.png"), (50, 50))
down = transform.scale(image.load("icons/volumedown.png"), (50, 50))
up = transform.scale(image.load("icons/volumeup.png"), (50, 50))
welp = transform.scale(image.load("icons/help.png"), (50, 50))
info = transform.scale(image.load("icons/info.png"), (50, 50))
load = transform.scale(image.load("icons/load.png"), (50, 50))
new = transform.scale(image.load("icons/newfile.png"), (50, 50))
pencil = transform.scale(image.load("icons/pencil.png"), (50, 50))

# Import Stamps (w and h variables for resizing stamps)
stamp1 = transform.scale(image.load("stamps/stamp1.png"), (w, h))  # Smash logo
stamp2 = transform.scale(image.load("stamps/stamp2.png"), (w, h))  # Mario
stamp3 = transform.scale(image.load("stamps/stamp3.png"), (w, h))  # Link
stamp4 = transform.scale(image.load("stamps/stamp4.png"), (w, h))  # Pikachu
stamp5 = transform.scale(image.load("stamps/stamp5.png"), (w, h))  # Bowser
stamp6 = transform.scale(image.load("stamps/stamp6.png"), (w, h))  # Bowser

# Import fonts
font.init()
smashFont = font.Font("fonts/smash.ttf", 40)
timesNewRomanFont = font.Font("fonts/tnr.ttf", 20)
calibriFont = font.Font("fonts/calibri.ttf", 20)

# Import Font Boxes
smashFBox = transform.scale(image.load("graphics/smashFBox.png"), (200,40))
calibriFBox = transform.scale(image.load("graphics/calibriFBox.png"), (200,40))
tnrFBox = transform.scale(image.load("graphics/tnrFBox.png"), (200,40))

# Import Fill Shape Boxes
fillShapeBox = transform.scale(image.load("graphics/fillBox.png"), (200,40))
nofillShapeBox = transform.scale(image.load("graphics/nofillBox.png"), (200,40))

# Import Stamp Boxes
smashStamp = transform.scale(image.load("stamps/smash.png"), (60, 60))
marioStamp = transform.scale(image.load("stamps/mario.png"), (60, 60))
linkStamp = transform.scale(image.load("stamps/link.png"), (60, 60))
pikachuStamp = transform.scale(image.load("stamps/pikachu.png"), (60, 60))
bowserStamp = transform.scale(image.load("stamps/bowser.png"), (60, 60))
megamanStamp = transform.scale(image.load("stamps/megaman.png"), (60, 60))

# Window Settings
screen = display.set_mode((1280, 720))
display.set_caption("Smash Paint")
display.set_icon(stamp1)

# Creates a translucent surface to gradially darken
Fade = Surface((1280, 720))

# Decreases alpha
for i in range(255, 80, -6):
    screen.blit(wallpaper, (0, 0))  # Adds window wallpaper
    Fade.set_alpha(i)  # Makes it transparent
    screen.blit(Fade, (0, 0))  # puts the transparent backdrop
    display.flip()  # Updates
    
# Creates window
for i in range(0, 10, 5):
    screen.blit(wallpaper, (0, 0))  # Replaces background
    screen.blit(Fade, (0, 0))  # Makes it dark again
    screen.blit(menuWin, (0, 0))  # Adds window

display.flip()  # Updates the screen

# Hitboxes for menu screen buttons
newFile2Rect = Rect(400,270,200,200)
loadFile2Rect = Rect(700,270,200,200)

# Hitboxes for drawing screen buttons (72px top bar)
canvasRect = Rect(333,75,927,625)
drawArea = screen.subsurface(canvasRect)
brushRect = Rect(1,56,80,80)
eraserRect = Rect(1,137,80,80)
dropperRect = Rect(1,218,80,80)
polygonRect = Rect(1,299,80,80)
textRect = Rect(1,380,80,80)
sprayRect = Rect(1,461,80,80)
stampRect = Rect(1,542,80,80)
fillRect = Rect(1,623,80,80)
muteRect = Rect(84,1,75,53)
downRect = Rect(160,1,75,53)
upRect = Rect(236,1,75,53)
pencilRect = Rect(312,1,75,53)
markerRect = Rect(384,1,75,53)
penRect = Rect(456,1,75,53)
rectRect = Rect(528,1,75,53)
circRect = Rect(600,1,75,53)
lineRect = Rect(672,1,75,53)
newRect = Rect(744,1,75,53)
loadRect = Rect(816,1,75,53)
saveRect = Rect(888,1,75,53)
saveasRect = Rect(960,1,75,53)
helpRect = Rect(1,1,82,55)
undoRect = Rect(1132,1,75,53)
redoRect = Rect(1204,1,75,53)
colourRect = Rect(88,405,220,295)

# Hitboxes for font boxes
smashFRect = Rect(97,226,200,40)
calibriFRect = Rect(97,266,200,40)
tnrFRect = Rect(97,306,200,40)

# Hitboxes for fill shape boxes
yesfillRect = Rect(97,236,200,40)
nofillRect = Rect(97,286,200,40)

# Hitboxes for stamp boxes
smashRect = Rect(97,224,60,60)
marioRect = Rect(167,224,60,60)
linkRect = Rect(237,224,60,60)
bowserRect = Rect(97,288,60,60)
pikachuRect = Rect(167,288,60,60)
megamanRect = Rect(237,288,60,60)

# Music
musicList = [] # List of songs

# Add each song to list
for i in range(8,0,-1):
    musicList.append("audio/song%i.ogg"%(i))

shuffle(musicList) # Randomize music

if music: # Cycles through music
    mixer.init()
    mixer.music.load(musicList.pop())
    mixer.music.queue(musicList.pop())
    mixer.music.set_endevent(USEREVENT)
    mixer.music.play()
    volume = 1

# Help Text Contents
helpText1 = ["Brush: Creates strokes", # Help list line 1
             "Eraser: Removes a part",
             "Colour Picker: Select",
             "Polygon: Draw polygons",
             "Text: Type to preview",
             "Spray: Creates random",
             "Stamp: Paste pictures",
             "Fill: Fills a enclosed",
             "Mute: Mute music",
             "Volume Down: Lowers",
             "Volume Up: Increases",
             "Pencil: Creates strokes",
             "Marker: Creates lucent",
             "Pen: Creates lines",
             "Rect: Creates rectangle",
             "Circle: Creates circle",
             "Line: Creates a single",
             "Undo: Undo the previous",
             "Redo: Redo the previous",
             "Load: Load an image file",
             "New: Clears the canvas",
             "Save: Save your work",
             "Save as: Save your work",
             "Help: Click to toggle"]

helpText2 = ["that follow the cursor", # Help list line 2
             "of the picture",
             "a colour from the",
             "from a set of points",
             "text on screen",
             "dots on screen",
             "onto the screen",
             "region with selected",
             "",
             "volume of music",
             "volume of music",
             "that follow the cursor",
             "strokes that follow the",
             "with sharp edges",
             "of any length and width",
             "/ellipse of any radius",
             "line of any length",
             "action performed",
             "action performed",
             "from your computer",
             "",
             "to your computer",
             "as a new file to your",
             "help window"]

helpText3 = ["Use mouse wheel to", # Help list line 3
             "Use mouse wheel to",
             "drawing canvas",
             "Right click to end",
             "Left click to blit",
             "Use mouse wheel to",
             "Use mouse wheel to",
             "colour",
             "",
             "",
             "",
             "Size not adjustable",
             "cursor.Use mouse wheel",
             "Use mouse wheel to",
             "Click and drag to draw",
             "Click and drag to draw",
             "Click and drag to draw",
             "",
             "",
             "",
             "",
             "",
             "computer",
             ""]

helpText4 = ["change size of stroke", # Help list line 4
             "change size of eraser",
             "",
             "drawing polygon",
             "text onto screen",
             "change size of spray",
             "change size of stamp",
             "",
             "",
             "",
             "",
             "",
             "to change size of stroke",
             "change size of stroke",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             ""]

# Functions -----------------------------------------------------------------------------------------
# Draw toolboxes and other buttons
def drawUI():
    screen.blit(drawingWin, (0,0))
    draw.rect(screen, BLACK, brushRect, 2)
    draw.rect(screen, BLACK, eraserRect, 2)
    draw.rect(screen, BLACK, dropperRect, 2)
    draw.rect(screen, BLACK, polygonRect, 2)
    draw.rect(screen, BLACK, textRect, 2)
    draw.rect(screen, BLACK, sprayRect, 2)
    draw.rect(screen, BLACK, stampRect, 2)
    draw.rect(screen, BLACK, fillRect, 2)
    draw.rect(screen, BLACK, muteRect, 2)
    draw.rect(screen, BLACK, downRect, 2)
    draw.rect(screen, BLACK, upRect, 2)
    draw.rect(screen, BLACK, pencilRect, 2)
    draw.rect(screen, BLACK, penRect, 2)
    draw.rect(screen, BLACK, markerRect, 2)
    draw.rect(screen, BLACK, circRect, 2)
    draw.rect(screen, BLACK, rectRect, 2)
    draw.rect(screen, BLACK, lineRect, 2)
    draw.rect(screen, BLACK, newRect, 2)
    draw.rect(screen, BLACK, loadRect, 2)
    draw.rect(screen, BLACK, saveRect, 2)
    draw.rect(screen, BLACK, saveasRect, 2)
    draw.rect(screen, BLACK, helpRect, 2)
    draw.rect(screen, BLACK, undoRect, 2)
    draw.rect(screen, BLACK, redoRect, 2)
    
# Brush Tool
def brushTool(colour, mx, my, size):
    dx, dy = omx-mx, omy-my # Calculates delta x and y from current mouse position and old position
    dist = max(abs(dx),abs(dy)) # Gets distance between old and new points
    for i in range(dist):
        x = int(mx+i/dist*dx) # Calculates the position of the circle for drawing
        y = int(my+i/dist*dy)
        draw.circle(screen, colour,(x, y), size) # Draw the circle
        
    return mx, my

# Eraser Tool
def eraserTool(mx, my, size):
    dx, dy = omx-mx, omy-my # Calculates delta x and y from current mouse position and old position
    dist = max(abs(dx),abs(dy)) # Gets distance between old and new points
    for i in range(dist):
        x = int(mx+i/dist*dx) # Calculates the position of the circle for drawing
        y = int(my+i/dist*dy)
        draw.circle(screen, WHITE, (x, y), size) # Draw the circle

    return mx, my

# Colour picker Tool
def dropperTool(colour, mx, my):
    if canvasRect.collidepoint((mx ,my)) and mb[0] == 1: # Checks if the mouse in on the canvas and left mouse button is down
        colour = screen.get_at((mx, my)) # Return the colour that mouse is on
        
    draw.circle(screen, colour, (1084,27), 20) # Update the current colour circle
    return colour

# Polygon Tool
def polygonTool(colour, mx, my):
    polygonList.append((mx, my)) # Adds mouse points to list
    
    return mx, my

# Pencil Tool
def pencilTool(colour, mx, my):
    draw.line(screen, colour, (omx,omy), (mx,my)) # Draws a line from old and new mouse positions

    return mx, my

# Marker Tool
def markerTool(colour, mx, my, size):
    brushHead = Surface((20,20), SRCALPHA) # Makes a semi-transparent surface for marker
    draw.circle(brushHead, (colour[0], colour[1], colour[2],22), (10,10), size) # Draw the circle
    
    dx, dy = omx-mx, omy-my # Calculates delta x and y from current mouse position and old position
    dist = max(abs(dx),abs(dy)) # Gets distance between old and new points
    for i in range(dist):
        x = int(mx+i/dist*dx) # Calculates the position of the circle for drawing
        y = int(my+i/dist*dy)
        screen.blit(brushHead, (x, y))  # Draw the circle

    return mx, my

# Spraypaint Tool
def sprayTool(colour, mx, my):
    for i in range(10):
        rx = randint(-size, size) # Generate a random value for x and y based on cursor size
        ry = randint(-size, size)
    
        if hypot(rx, ry) <= size: # Euclidean norm (sqrt(x*x + y*y))
            draw.circle(screen, colour, (mx + rx, my + ry), 0) # Draw the circle

    return mx, my

# Fill Bucket Tool
def fillTool(mx, my, fillCol):
    pixelQueue = [(mx, my)] # List of pixels from mouse position
    startCol = screen.get_at((mx, my)) # Makes sure only certain pixels are filled
    
    if startCol != fillCol: # Checks that clicked colour is not the fill colour
        while len(pixelQueue) > 0:
            # Takes coordinates of the canvas rectangle and check if the pixel that is to be filled is inside the canvas and has the same colour the pixel mouse clicked on
            if pixelQueue[0][0] >= canvasRect[0] and pixelQueue[0][0] < canvasRect[2] + canvasRect[0] and pixelQueue[0][1] > 0 and pixelQueue[0][1] <= canvasRect[3] + canvasRect[1] and screen.get_at(pixelQueue[0]) == startCol:
    
                screen.set_at((pixelQueue[0]),colour) # Fills the actual pixel with the colour
                # Checks the pixel above, below, right and left
                pixelQueue.append((pixelQueue[0][0], pixelQueue[0][1]-1))
                pixelQueue.append((pixelQueue[0][0], pixelQueue[0][1]+1))
                pixelQueue.append((pixelQueue[0][0]-1, pixelQueue[0][1]))
                pixelQueue.append((pixelQueue[0][0]+1, pixelQueue[0][1]))
                
            del pixelQueue[0] # Deleting the filled pixel from the list
            
    return mx, my

# Rectangle Tool
def rectTool(colour, mx, my):
    screen.blit(back, (0,0)) # Makes sure program doesn't draw multiple rectangles on the canvas
    
    if rectFill == False:
        draw.rect(screen, colour, (start[0], start[1], mx-start[0], my-start[1]), 2) # Draw the rectangle
    if rectFill == True:
        draw.rect(screen, colour, (start[0], start[1], mx-start[0], my-start[1])) # Draw the filled rectangle

    return mx, my

# Ellipse Tool
def circTool(colour, mx, my):
    screen.blit(back, (0,0)) # Makes sure program doesn't draw multiple ellipses on the canvas

    try: # Since the width always starts bigger than ellipse radius, we need try, except statement
        if circFill == False:
            # Draw the ellipse
            draw.ellipse(screen, colour, (min(start[0], mx), min(start[1], my), abs(mx-start[0]), abs(my-start[1])), 2)
        if circFill == True:
            # Draw the filled ellipse
            draw.ellipse(screen, colour, (min(start[0], mx), min(start[1], my), abs(mx-start[0]), abs(my-start[1])))
    except:
        pass
    
    return mx, my

# Line Tool
def lineTool(colour, mx, my):
    screen.blit(back,(0,0)) # Makes sure program doesn't draw multiple lines on the canvas
    draw.line(screen, colour ,(start[0], start[1]), (mx, my), 2) # Draw the line

    return mx, my

# Pen Tool
def penTool(colour, mx, my, size):
    dx, dy = omx-mx, omy-my # Calculates delta x and y from current mouse position and old position
    dist = max(abs(dx),abs(dy)) # Gets distance between old and new points
    for i in range(dist):
        x = int(mx+i/dist*dx) # Calculates the position of the circle for drawing
        y = int(my+i/dist*dy)
        draw.line(screen, colour, (x-size//2, y-1*size), (x+size//2, y+1*size), size) # Draw the line

    return mx, my

# Render Text
def rerender_text():
    for surface, pos in text_rendered:
        screen.blit(surface, pos)  # Display text

# Stamp Tool
def stampTool(mx, my):
    if canvasRect.collidepoint(mx, my) and mb[0] == 1: # Checks if mouse in on canvas and left mouse button is down
        screen.set_clip(canvasRect) # So the stamp can't be blit outside the canvas
        if stampSelected == "Smash":
            screen.blit(back, (0,0)) # Clear canvas
            screen.blit(transform.scale(stamp1, (w, h)), (mx, my)) # Adjust width and height of stamp based on size
        if stampSelected == "Mario":
            screen.blit(back, (0,0)) # Clear canvas
            screen.blit(transform.scale(stamp2, (w, h)), (mx, my)) # Adjust width and height of stamp based on size
        if stampSelected == "Link":
            screen.blit(back, (0,0)) # Clear canvas
            screen.blit(transform.scale(stamp3, (w, h)), (mx, my)) # Adjust width and height of stamp based on size
        if stampSelected == "Pikachu":
            screen.blit(back, (0,0)) # Clear canvas
            screen.blit(transform.scale(stamp4, (w, h)), (mx, my)) # Adjust width and height of stamp based on size
        if stampSelected == "Bowser":
            screen.blit(back, (0,0)) # Clear canvas
            screen.blit(transform.scale(stamp5, (w, h)), (mx, my)) # Adjust width and height of stamp based on size
        if stampSelected == "Megaman":
            screen.blit(back, (0,0)) # Clear canvas
            screen.blit(transform.scale(stamp6, (w, h)), (mx, my)) # Adjust width and height of stamp based on size
            
        screen.set_clip(None) # Release the clip
        
    return mx, my

# Redo Button
def redo():
    try:
        screen.blit(redoList[-1], (0, 0)) # Blit latest action onto canvas
        undoList.append(redoList[-1]) # Adds latest action to list
        del redoList[-1] # Delete the latest action from list
    except:
        pass

# Undo Button
def undo():
    try:
        redoList.append(undoList[-1]) # Adds latest action to list
        del undoList[-1] # Delete the latest action from list
        screen.blit(undoList[-1], (0, 0)) # Blit previous action onto canvas
    except:
        draw.rect(screen, WHITE, canvasRect) # No more actions, fill the canvas white
        pass
    
# Load Button
def load():
    try:
        # Prompt open file window
        attemptloadfile = filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")])
        loadFile = image.load(attemptloadfile) # Load the file
        drawArea.blit(loadFile, (0, 0)) # Blit the loaded file
    except:
        pass

# New Button
def new():
    screen.fill(WHITE) # Clears screen
    drawUI() # Redraw the UI
    draw.rect(screen, GREY, (0,0,1280,720)) # Redraw the background
    drawArea.fill(WHITE) # Fill the canvas white


# Gameloop ------------------------------------------------------------------------------------------
while running:

    clock.tick()  # Advances the clock for FPS
    display.flip()  # Updates the screen
    
    click = False  # Resets momentary click
    unclick = False
    
    # Mouse location
    mx, my = mouse.get_pos()
    # Mouse click status
    mb = mouse.get_pressed()

    # Event Loop
    for e in event.get():
        if e.type == QUIT:
            running = False
            
        if e.type == MOUSEBUTTONDOWN: # If mouse is clicked
            start = e.pos
            back = screen.copy()

            if tool == "Text" and canvasRect.collidepoint(mx, my) and mb[0] == 1:
                screen.blit(textSurf, (mx, my))
                text_rendered.append((useFont, (mx, my)))
            else:
                textContent = ""

            # Scroll wheel for size change
            if e.button == 4:
                if size < 50:
                    size += 1 # Increase size
                    w += 1 # Increase width and height
                    h += 1
                    
            if e.button == 5:
                if size > 1:
                    size -= 1 # Decrease size
                    w -= 1 # Decrease width and height
                    h -= 1
                    
        # If the mouse button is clicked down
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            click = True

        # If mouse button is released
        if e.type == MOUSEBUTTONUP and e.button == 1:
            unclick = True
                    
        if e.type == MOUSEBUTTONUP: # If mouse button is released
            textContent = "" # Clear text contents
            
            if canvasRect.collidepoint(mx, my) and tool != "": # Makes sure it doesn't record tool switches
                action = screen.copy() # Saves a copy of whatever in on canvas
                undoList.append(action) # Adds the copy to undo list
            
            
        if e.type == USEREVENT: # If the music ends
            musicList.insert(0, musicList.pop()) # Take the last item in playlist and move to front
            mixer.music.load(musicList[-1]) # Load new muic
            mixer.music.play() # Play it
            
        if e.type == KEYDOWN: # If a keyboard key is down
            if key.get_pressed()[K_ESCAPE] and helpOn == True: # If escape key is down and help is on
                screen.fill(WHITE) # Clear screen
                drawUI() # Draw UI
                draw.rect(screen, GREY, (0,0,1280,720)) # Draw background
                screen.blit(back, (0,0)) # Blit whatever the canvas had
                helpOn = False # Turn off help
                
            if tool == "Text" and canvasRect.collidepoint(mx, my): # Checks that current tool is text and mosue is on canvas
                keys = list(key.get_pressed()) # Adds pressed key to a list
                index = keys.index(1) # Gets index of pressed key
                
                if key.get_pressed()[K_BACKSPACE]: # If backspace key is pressed
                    textContent = textContent[:-1] # Removes last letter
                else:
                    textContent += e.unicode # Adds letter
        
    # Menu screen selected
    if currentScreen == "Menu": # Menu Screen Selected  
        screen.blit(newFile2, (400, 270))  # Adds new file button
        screen.blit(loadFile2, (700, 270))  # Adds load file button
        
        # Check if mouse is on new file button
        if newFile2Rect.collidepoint(mx,my):
            screen.blit(newFile2G, (400,270))
            if mb[0] == 1:
                fileName = "Untitled"  # Gives the file the name "Untitled"
                currentScreen = "Drawing" # Goes to Drawing Screen

        # Check if mouse is on load file button    
        if loadFile2Rect.collidepoint(mx,my):
            screen.blit(loadFile2G, (700,270))
            if click: # Prompt open file window
                attemptLoadFile = filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")])

            if attemptLoadFile: # Checks that loaded file is valid
                loadFile = image.load(attemptLoadFile) # Load the file
                imageLoaded = True
            else:
                attemptLoadFile = None

            if attemptLoadFile != None: # If the file type is valid
                fileName = attemptLoadFile # Sets file name
                currentScreen = "Drawing" # Goes to Drawing Screen

    elif currentScreen == "Drawing": # Drawing Screen Selected
        drawUI() # Calls the function drawUI
        if not UI: # Makes sure UI is only drawn once
            UI = True
            draw.rect(screen, GREY, (0,0,1280,720)) # Draw background
            drawArea.fill(WHITE) # Fill canvas white
            
        # Loads the image if user clicked on Load File Button
        if attemptLoadFile and Loaded != True:
            Loaded = True
            drawArea.blit(loadFile, (0,0))

        # Colour picker    
        if colourRect.collidepoint((mx ,my)) and mb[0] == 1: # If mouse is on colour gradiant
            colour = screen.get_at((mx, my)) # Get the colour at mouse position
        
        draw.circle(screen, colour, (1084,27), 20) # Update the current colour circle
        
        # Thickness Number
        sizeFont = font.Font("fonts/smash.ttf", 28) # Font for info panel
        render = sizeFont.render("Size: " + str(size), False, BLACK) # Render the size
        screen.blit(render, (100, 365)) # Blit render text

        # Detecting when user has clicked on a tool or has hovered over one
        if brushRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, brushRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[0], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[0], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[0], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[0], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Brush"
        if eraserRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, eraserRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[1], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[1], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[1], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[1], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Eraser"
        if dropperRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, dropperRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[2], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[2], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[2], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[2], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Dropper"
        if polygonRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, polygonRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[3], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[3], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[3], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[3], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Polygon"
        if textRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, textRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[4], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[4], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[4], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[4], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Text"       
        if sprayRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, sprayRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[5], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[5], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[5], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[5], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Spray"
        if stampRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, stampRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[6], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[6], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[6], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[6], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Stamp"
        if fillRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, fillRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[7], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[7], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[7], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[7], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Fill"
        if pencilRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, pencilRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[11], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[11], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[11], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[11], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Pencil"
        if markerRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, markerRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[12], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[12], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[12], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[12], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Marker"
        if rectRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, rectRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[14], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[14], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[14], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[14], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Rect"
        if circRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, circRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[15], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[15], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[15], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[15], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Circ"
        if lineRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, lineRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[16], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[16], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[16], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[16], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Line"
        if penRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, penRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[13], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[13], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[13], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[13], True, BLACK), (98, 130))
            if mb[0] == 1:
                tool="Pen"
        if undoRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, undoRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[17], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[17], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[17], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[17], True, BLACK), (98, 130))
            if click:
                undo()
        if redoRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, redoRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[18], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[18], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[18], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[18], True, BLACK), (98, 130))
            if click:
                redo()
        if loadRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, loadRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[19], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[19], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[19], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[19], True, BLACK), (98, 130))
            if click:
                load()
        if newRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, newRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[20], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[20], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[20], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[20], True, BLACK), (98, 130))
            if click:
                new()
        if saveRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, saveRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[21], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[21], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[21], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[21], True, BLACK), (98, 130))
            if click:
                if fileName == "Untitled": # Prompt save file window
                    saveFile = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png'), ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])  # Ask to get a name

                if saveFile:  # Checks if the set name is valid
                    image.save(drawArea, saveFile)  # Saves the photo
                    fileName = saveFile  # Sets as the file name
                    
        if saveasRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, saveasRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[22], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[22], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[22], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[22], True, BLACK), (98, 130))
            if click: # Prompt save file window
                saveFile = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png'), ('JPEG / JFIF','*.jpg'),('Windows Bitmap','*.bmp')])  # Ask to get a name

                if saveFile:  # Checks if the set name is valid
                    image.save(drawArea, saveFile)  # Saves the photo
                    fileName = saveFile  # Sets as the file name
 
        if helpRect.collidepoint(mx,my):
            draw.rect(screen, WHITE, helpRect, 2) # White outline around tool rectangle when hovered over
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[23], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[23], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[23], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[23], True, BLACK), (98, 130))
            if click:
                helpOn = True
                
        # Changing Selected Tool Outline and help content
        if tool == "Brush":
            draw.rect(screen, WHITE, brushRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[0], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[0], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[0], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[0], True, BLACK), (98, 130))
        if tool == "Eraser":
            draw.rect(screen, WHITE, eraserRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[1], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[1], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[1], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[1], True, BLACK), (98, 130))
        if tool == "Dropper":
            draw.rect(screen, WHITE, dropperRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[2], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[2], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[2], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[2], True, BLACK), (98, 130))
        if tool == "Polygon":
            draw.rect(screen, WHITE, polygonRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(fillShapeBox,(97,236)) # Blit the fill shape buttons
            screen.blit(nofillShapeBox,(97,286))
            draw.rect(screen, BLACK, yesfillRect, 2) # Blit the fill shape buttons rects
            draw.rect(screen, BLACK, nofillRect, 2)
            screen.blit(helpFont.render(helpText1[3], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[3], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[3], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[3], True, BLACK), (98, 130))

            if yesfillRect.collidepoint(mx, my): # If fill is toggled on
                draw.rect(screen, WHITE, yesfillRect, 2)
                if click:
                    polyFill = True
            if nofillRect.collidepoint(mx, my): # If fill is toggled off
                draw.rect(screen, WHITE, nofillRect, 2)
                if click:
                    polyFill = False
                    
        if tool == "Text":
            draw.rect(screen, WHITE, textRect, 2)
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[4], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[4], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[4], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[4], True, BLACK), (98, 130))
            screen.blit(smashFBox,(97,226)) # Blit the font buttons
            screen.blit(calibriFBox,(97,266))
            screen.blit(tnrFBox,(97,306))
            draw.rect(screen, BLACK, smashFRect, 2) # Blit the font button rects
            draw.rect(screen, BLACK, calibriFRect, 2)
            draw.rect(screen, BLACK, tnrFRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted

            # Checks which font the user has clicked on
            if smashFRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, smashFRect, 2)
                if mb[0] == 1:
                    textFont = "Smash"
            if calibriFRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, calibriFRect, 2)
                if mb[0] == 1:
                    textFont = "Calibri"
            if tnrFRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, tnrFRect, 2)
                if mb[0] == 1:
                    textFont = "TimesNewRoman"
                    
        if tool == "Spray":
            draw.rect(screen, WHITE, sprayRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[5], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[5], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[5], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[5], True, BLACK), (98, 130))
        if tool == "Stamp":
            draw.rect(screen, WHITE, stampRect, 2)
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[6], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[6], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[6], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[6], True, BLACK), (98, 130))
            screen.blit(smashStamp,(97,224)) # Blit the stamp buttons
            screen.blit(marioStamp,(167,224))
            screen.blit(linkStamp,(237,224))
            screen.blit(pikachuStamp,(167,288))
            screen.blit(bowserStamp,(97,288))
            screen.blit(megamanStamp,(237,288))
            draw.rect(screen, BLACK, smashRect, 2) # Blit the stamp button rects
            draw.rect(screen, BLACK, marioRect, 2)
            draw.rect(screen, BLACK, linkRect, 2)
            draw.rect(screen, BLACK, pikachuRect, 2)
            draw.rect(screen, BLACK, bowserRect, 2)
            draw.rect(screen, BLACK, megamanRect, 2)
            textFont = "" # Makes sure no outline from text tool is blitted

            # Checks which stamp the user has clicked on
            if smashRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, smashRect, 2)
                if click:
                    stampSelected = "Smash"
            if marioRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, marioRect, 2)
                if click:
                    stampSelected = "Mario"
            if linkRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, linkRect, 2)
                if click:
                    stampSelected = "Link"
            if pikachuRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, pikachuRect, 2)
                if click:
                    stampSelected = "Pikachu"
            if bowserRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, bowserRect, 2)
                if click:
                    stampSelected = "Bowser"
            if megamanRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, megamanRect, 2)
                if click:
                    stampSelected = "Megaman"
                
        if tool == "Fill":
            draw.rect(screen, WHITE, fillRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[7], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[7], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[7], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[7], True, BLACK), (98, 130))
        if tool == "Pencil":
            draw.rect(screen, WHITE, pencilRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[11], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[11], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[11], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[11], True, BLACK), (98, 130))
        if tool == "Marker":
            draw.rect(screen, WHITE, markerRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[12], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[12], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[12], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[12], True, BLACK), (98, 130))
        if tool == "Rect":
            draw.rect(screen, WHITE, rectRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(fillShapeBox,(97,236)) # Blit the fill shape buttons
            screen.blit(nofillShapeBox,(97,286))
            draw.rect(screen, BLACK, yesfillRect, 2) # Blit the fill shape buttons rects
            draw.rect(screen, BLACK, nofillRect, 2)
            screen.blit(helpFont.render(helpText1[14], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[14], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[14], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[14], True, BLACK), (98, 130))

            if yesfillRect.collidepoint(mx, my): # If fill is toggled on
                draw.rect(screen, WHITE, yesfillRect, 2)
                if click:
                    rectFill = True
            if nofillRect.collidepoint(mx, my): # If fill is toggled off
                draw.rect(screen, WHITE, nofillRect, 2)
                if click:
                    rectFill = False
                    
        if tool == "Circ":
            draw.rect(screen, WHITE, circRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(fillShapeBox,(97,236)) # Blit the fill shape buttons
            screen.blit(nofillShapeBox,(97,286))
            draw.rect(screen, BLACK, yesfillRect, 2) # Blit the fill shape buttons rects
            draw.rect(screen, BLACK, nofillRect, 2)
            screen.blit(helpFont.render(helpText1[15], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[15], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[15], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[15], True, BLACK), (98, 130))

            if yesfillRect.collidepoint(mx, my): # If fill is toggled on
                draw.rect(screen, WHITE, yesfillRect, 2)
                if click:
                    circFill = True
            if nofillRect.collidepoint(mx, my): # If fill is toggled off
                draw.rect(screen, WHITE, nofillRect, 2)
                if click:
                    circFill = False
                    
        if tool == "Line":
            draw.rect(screen, WHITE, lineRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[16], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[16], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[16], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[16], True, BLACK), (98, 130))
        if tool == "Pen":
            draw.rect(screen, WHITE, penRect, 2)
            stampSelected = "" # Makes sure no outline from stamp tool is blitted
            textFont = "" # Makes sure no outline from text tool is blitted
            screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
            screen.blit(redraw2, (0, 0))
            screen.blit(helpFont.render(helpText1[13], True, BLACK), (98, 70)) # Blit help lines
            screen.blit(helpFont.render(helpText2[13], True, BLACK), (98, 90))
            screen.blit(helpFont.render(helpText3[13], True, BLACK), (98, 110))
            screen.blit(helpFont.render(helpText4[13], True, BLACK), (98, 130))
        
        # Tool Functions
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect) # Makes sure you can only paint on canvas
            if tool == "Brush" and mb[0] == 1:
                mx, my = brushTool(colour, mx, my, size)
            if tool == "Eraser" and mb[0] == 1:
                mx, my = eraserTool(mx, my, size)
            if tool == "Dropper" and mb[0] == 1:
                colour = dropperTool(colour, mx, my)
            if tool == "Polygon":
                if click and len(polygonList) == 0:  # Gets the starting polygon location
                    mx, my = polygonTool(colour, mx, my)

                if unclick:
                    mx, my = polygonTool(colour, mx, my)  # Gets the points after that

                if not click and len(polygonList) > 0:  # If the mouse is not clicked, draw the cursor along with the segments
                    screen.blit(back, (0, 0))  # Clears canvas

                    for i in range(len(polygonList) - 1):  # Draws the lines being drawn
                        draw.line(screen, colour, polygonList[i], polygonList[i + 1], 3)

                # If the right mouse is clicked or line returns to orgin, clear list
                if (mb[2] == 1 and len(polygonList) > 0) or len(polygonList) > 2 and polygonList[0][0] - 5 < polygonList[-1][0] < polygonList[0][0] + 5 and polygonList[0][1] - 5 < polygonList[-1][1] < polygonList[0][1] + 5:
                    screen.blit(back, (0, 0))  # Clears canvas
                    
                    if len(polygonList) < 1: # If no points, clear canvas
                        screen.blit(back, (0, 0))  # Clears canvas

                    if polyFill == True:
                        draw.polygon(screen, colour, polygonList)  # Draws the filled polygon
                    if polyFill == False:
                        draw.polygon(screen, colour, polygonList, 2)  # Draws the polygon 

                    polygonList = []  # Resets list
                    
            if tool == "Pencil" and mb[0] == 1:
                mx, my = pencilTool(colour, mx, my)
            if tool == "Marker" and mb[0] == 1:
                mx, my = markerTool(colour, mx, my, size)
            if tool == "Spray" and mb[0] == 1:
                mx, my = sprayTool(colour, mx, my)
            if tool == "Fill" and mb[0] == 1:
                mx, my = fillTool(mx, my, colour)
            if tool == "Rect" and mb[0] == 1:
                mx, my = rectTool(colour, mx, my)
            if tool == "Circ" and mb[0] == 1:
                mx, my = circTool(colour, mx, my)
            if tool == "Line" and mb[0] == 1:
                mx, my = lineTool(colour, mx, my)
            if tool == "Pen" and mb[0] == 1:
                mx, my = penTool(colour, mx, my, size)
            if tool == "Stamp" and mb[0] == 1:        
                mx, my = stampTool(mx, my)
                        
            screen.set_clip(None) # Release clip

        # Stamp box outlines
        if stampSelected == "Smash":
            draw.rect(screen, WHITE, smashRect, 2)
        if stampSelected == "Mario":
            draw.rect(screen, WHITE, marioRect, 2)
        if stampSelected == "Link":
            draw.rect(screen, WHITE, linkRect, 2)
        if stampSelected == "Pikachu":
            draw.rect(screen, WHITE, pikachuRect, 2)
        if stampSelected == "Bowser":
            draw.rect(screen, WHITE, bowserRect, 2)
        if stampSelected == "Megaman":
            draw.rect(screen, WHITE, megamanRect, 2)

        # Text box outlines
        if textFont == "Smash":
            draw.rect(screen, WHITE, smashFRect, 2)
            useFont = font.Font("fonts/smash.ttf", size)
        if textFont == "TimesNewRoman":
            draw.rect(screen, WHITE, tnrFRect, 2)
            useFont = font.Font("fonts/tnr.ttf", size)
        if textFont == "Calibri":
            draw.rect(screen, WHITE, calibriFRect, 2)
            useFont = font.Font("fonts/calibri.ttf", size)
                
        if music: # If music is enabled
            if muteRect.collidepoint(mx,my):
                draw.rect(screen, WHITE, muteRect, 2)
                screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
                screen.blit(redraw2, (0, 0))
                screen.blit(helpFont.render(helpText1[8], True, BLACK), (98, 70)) # Blit help lines
                screen.blit(helpFont.render(helpText2[8], True, BLACK), (98, 90))
                screen.blit(helpFont.render(helpText3[8], True, BLACK), (98, 110))
                screen.blit(helpFont.render(helpText4[8], True, BLACK), (98, 130))
                if click:
                    mixer.music.set_volume(0) # Mute music
                    
            if downRect.collidepoint(mx,my): # Volume down
                draw.rect(screen, WHITE, downRect, 2) # White outline around tool rectangle when hovered over
                screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
                screen.blit(redraw2, (0, 0))
                screen.blit(helpFont.render(helpText1[9], True, BLACK), (98, 70)) # Blit help lines
                screen.blit(helpFont.render(helpText2[9], True, BLACK), (98, 90))
                screen.blit(helpFont.render(helpText3[9], True, BLACK), (98, 110))
                screen.blit(helpFont.render(helpText4[9], True, BLACK), (98, 130))
                if volume > 0.1 and click:
                    volume -= 0.1  # Decreases volume and updates
                    mixer.music.set_volume(volume)
                    
            if upRect.collidepoint(mx,my): # Volume up
                draw.rect(screen, WHITE, upRect, 2) # White outline around tool rectangle when hovered over
                screen.blit(redraw1, (0, 0)) # Redraw the help and info boxes
                screen.blit(redraw2, (0, 0))
                screen.blit(helpFont.render(helpText1[10], True, BLACK), (98, 70)) # Blit help lines
                screen.blit(helpFont.render(helpText2[10], True, BLACK), (98, 90))
                screen.blit(helpFont.render(helpText3[10], True, BLACK), (98, 110))
                screen.blit(helpFont.render(helpText4[10], True, BLACK), (98, 130))
                if volume < 1 and click:
                    volume += 0.1  # Increases volume and updates
                    mixer.music.set_volume(volume) 
                    
    # Render text on screen
    if len(textContent) >= 1 and canvasRect.collidepoint(mx, my): # Renders once user enters letters      
        screen.blit(back, (0,0))
        textSurf = useFont.render(textContent, True, colour)  # Render Text
        rerender_text()
        screen.blit(textSurf, (mx, my))  # Display text

    # Help Screen
    if helpOn == True:
        screen.fill(WHITE)
        screen.blit(helpScr, (0, 0)) # Blit the help window

    omx, omy = mx, my # Old mouse position
    
    clock.tick()  # Advances the clock for FPS
    display.flip()  # Updates the screen

quit()









