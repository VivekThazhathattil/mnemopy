import collections
import random
import time 
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np

###############################################################
#DONE 1) Remove the lag in loading Speed Cards
#TODO 2) Add a generic timer useful for all events
#TODO 3) Complete scripting for 5-minute numbers
#TODO 4) Show card number on the side for the users to know their progress
###############################################################
# CHANGELOG:
# A) THE FOLLOWING CHANGES WERE MADE TO MAKE THE IMAGE_DISPLAY MODULE FOR FASTER INITIAL RESPONSE
# 1. CREATED GLOBAL VARIABLE PHOTOS
# 2. EXPLICITLY SPECIFIED PHOTOS AS GLOBAL VARIABLE IN MAIN_MENU, RECALL_SESSION AND IMAGE_DISPLAY
# 3. MOVED PART OF MODULE LOADING TO MAIN_MENU METHOD
###############################################################
# 5-MIN RAND NO TASKSET
#TODO:  GENERATE RANDOM NUMBER B/W 1 TO 10
#TODO:  STORE THE NUMBERS INTO AN EXPANDING LIST
#TODO:  SHOW THE NUMBER AS A LABEL TO THE FRAME AS BOLD, LARGE FONT ITEM
#TODO:  NEXT BUTTON, (NO PREV BUTTON), QUIT TO MENU BUTTON, RECALL BUTTON
#TODO:  LIVE COUNTER FOR THE USERS TO KNOW THEIR PROGRESS
#TODO:  RECALL_SESSION, SAME STUFF AS USUAL
#TODO:  ADD TIMER, IMPLEMENT THE TIMER MECHANISM TO STOP DISPLAYING NUMBERS AT THE TIMER LIMIT MARK.
#TODO:  MODIFY TIMER TO INCLUDE THE TIME LIMIT BY MYSELF. (i.e. CHANGE 5-MIN TO OTHER TIME LIMIT)
###############################################################
# 15-MIN RANDOM WORDS TASKSET
#TODO: LOAD DICT FILE (THE TOUGHER ONE)
#TODO: GET A RANDOM WORD OUT OF THE DICT FILE
#TODO: SAME AS USUAL, DO WHATEVER WAS DONE FOR 5-MIN CASE
###############################################################

window = tk.Tk()
window.title("Mnemopy by Vivek")
window.geometry('800x500')  # set window size
window.resizable(0, 0)  # fix window

frame = tk.Frame(window)
frame.pack()

photos = None
running = False
clock_running = False
begun = False

clock_label = tk.Label(frame)

###############################################################

def update_clock():
    global clock_label
    if clock_running:
        now = time.strftime("%H:%M:%S")
        clock_label.configure(text=now)
        after(1000, update_clock)

###############################################################

def fiveMinNumbers():

#   getTime() to get the time(in mins) entered in the entry box
#   gridSizeH to get the height of the number grid per page 
#   gridsizeW to get the length of the number grid per page
#   noPages to get the number of pages to generate (go for dynamic implementation)
#   genRandNum to generate a 2D matrix of random numbers

    gridSizeH = 10 # Default value for height
    gridSizeW = 15 # Default value for width

    beforeCount = 1000 #TODO: Remove the hardcoded number and make it more dynamic or make it inf
    numLabel = None
    counter = 0

    def getGridSizeH():
        value = gridSizeHEntry.get() 
        print("Height " + str(value))
        global gridSizeH
        gridSizeH = int(float(value)*1000)

    def getGridSizeW(): 
        value = TimeDelayEntry.get() 
        print("Width " + str(value))
        global gridSizeW
        gridSizeW = int(float(value)*1000)

    def genRandNum():
        global numList
        global beforeCount
        global numLabel
        numListTemp = [[random.randrange(10) for i in range(15)] for j in range(10)]
        numListString = str(np.array(numListTemp))
        numLabel = tk.Label(frame, text=numListString)
        beforeCount += 1

    def nextButtonAction():
        counter += 1
        if counter > beforeCount:
            return
        else:
            global numLabel
            numLabel.destroy()
            genRandNum()
            numLabel = tk.Label(frame, image=numLabel)
            numLabel.grid(row = 2, column = 2)
            print(numLabel.counter)

    def prevButtonAction():
            if numLabel.counter == 0:
                return
            else:
                global numLabel()
                im1.destroy()
                numLabel.counter -= 1
                im1 = numLabel.photos[numLabel.counter%len(numLabel.photos)]
                im1 = tk.Label(frame, image=im1)
                im1.grid(row = 2, column = 2)
                print(numLabel.counter)
 
#    def reviewButtonAction():

#    def quitButtonAction():


    gridSizeHEntry = tk.Entry(frame)
    gridSizeWEntry = tk.Entry(frame)

    gridSizeHButton = tk.Button(frame, text = "Height", command = getGridSizeH)
    gridSizeWButton = tk.Button(frame, text = "Width", command = getGridSizeW)

    gridSizeHEntry.grid(row = 1, column = 1) 
    gridSizeWEntry.grid(row = 2, column = 1) 

    gridSizeHButton.grid(row = 1, column = 2)
    gridSizeHButton.grid(row = 2, column = 2)

    numList = []
    pageNo = 1

    clearFrame()
    prevButton = tk.Button(frame, text="Prev", command = prevButtonAction)
    nextButton = tk.Button(frame, text="Next", command = nextButtonAction)
    reviewButton = tk.Button(frame, text="Review", command = ReviewButtonAction)
    quitButton = tk.Button(frame, text="Quit", command = quitButtonAction)

    prevButton.grid(row = 3, column = 0)
    nextButton.grid(row = 3, column = 2)
    reviewButton.grid(row = 4, column = 0)
    quitButton.grid(row = 4, column = 2)



###############################################################

def main_menu():
    clearFrame()
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = ['S', 'D', 'C', 'H']
    Deck = [rank + suit for suit in suits for rank in ranks]
    
    Cards = random.sample(Deck, 52)
    clearFrame()
    images = []
    img_path = "/home/tvivek/experimental/python_work/fluent_python/card_images/"
    
    for i in range(52):
        img_name = (Cards[i]+ ".png")
        full_img_loc = img_path + img_name
        images = images + [full_img_loc]

    global photos
    photos = []
    for j in images:
        img = ImageTk.PhotoImage(Image.open(j).resize((150, 250)))
        photos = photos + [img]

    BannerHeading = tk.Label(frame, text="Mnemopy Arena", font=("Arial Bold",25))
    BannerMessage = tk.Label(frame, text="This program is aimed at users who wish to hone their memorizing skills for events like WMC and XMT. Choose from the following list to begin your training session:", wraplength= 500)
    CardsButton = tk.Button(frame , text="Speed Cards", font=("Arial Bold", 12), command=image_display)
    NumbersButton = tk.Button(frame , text="5-minute numbers", font=("Arial Bold", 12))
    TextButton = tk.Button(frame , text="15-minute Random list of words", font=("Arial Bold", 12))
    Exiter = tk.Button(frame , text="Exit", font=("Arial Bold", 12), command=window.destroy)

    BannerHeading.pack()
    BannerMessage.pack()
    CardsButton.pack()
    NumbersButton.pack()
    TextButton.pack()
    Exiter.pack()
    


###############################################################

def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

###############################################################

def image_display():

    global photos
    im1 = None 
    clearFrame()
    card_label = tk.Label(frame)
    card_label.photos = photos
    card_label.counter = 0

#-------------------------------------------------------------

    def StartButton():
        global running
        global begun
        global clock_running

        if TimeDelayText:
            TimeDelayEntry.destroy()
            TimeDelayText.destroy()
            TimeDelayEnterButton.destroy()

        if not begun:
            print("Process begun")
            QuitToMenuButton['text'] = "Quit"
            begun = True
            running = True
            clock_running = True
            update_clock()
            next_pic()

        else:
            print("Process terminated")
            running = False
            clock_running = False
            begun = False
            main_menu()

#-------------------------------------------------------------

    def StopButton_cards():
        global running
        global clock_running
        global begun
        if running and begun:
            print("Paused!")
            running = not running
            clock_running = not clock_running
        elif not running and begun:
            print("Unpaused!")
            running = not running
            clock_running = not clock_running
            next_pic()
        elif running and not begun:
            running = not running
            clocK_running = not clock_running
        else:
            return

#-------------------------------------------------------------

    def getTimeDelay():
        TimeDelay = TimeDelayEntry.get() 
        print("TimeDelay " + str(TimeDelay))
        global timeStep
        timeStep = int(float(TimeDelay)*1000)

#-------------------------------------------------------------

    def recall_session():
        def begin_recall():
           global im1
           global photos
           card_label.counter = 0
           beginRecallButton.destroy()
           prevButton.grid(row = 1, column = 0)
           nextButton.grid(row = 1, column = 2)
           QuitButton.grid(row = 1, column = 4)
           im1 = card_label.photos[card_label.counter%len(card_label.photos)]
           im1 = tk.Label(frame, image=im1)
           im1.grid(row = 2, column = 2)
    
        def next_recall():
                if card_label.counter == len(card_label.photos):
                    return
                if card_label.counter >= copyOfCounter:
                    return
                else:
                    global im1
                    im1.destroy()
                    card_label.counter += 1
                    im1 = card_label.photos[card_label.counter%len(card_label.photos)]
                    im1 = tk.Label(frame, image=im1)
                    im1.grid(row = 2, column = 2)
                    print(card_label.counter)
        def prev_recall():
                if card_label.counter == 0:
                    return
                else:
                    global im1
                    im1.destroy()
                    card_label.counter -= 1
                    im1 = card_label.photos[card_label.counter%len(card_label.photos)]
                    im1 = tk.Label(frame, image=im1)
                    im1.grid(row = 2, column = 2)
                    print(card_label.counter)
        
        copyOfCounter = card_label.counter
        clearFrame()
        beginRecallButton = tk.Button(frame, text="Begin recall", command=begin_recall)
        beginRecallButton.grid(row=0,column=1)
        
        nextButton = tk.Button(frame, text="Next", command= next_recall)
        prevButton = tk.Button(frame, text="Prev", command= prev_recall)
        QuitButton = tk.Button(frame, text="Quit", command=main_menu)
    
   
#-------------------------------------------------------------

    PauseButton = tk.Button(frame , text="Pause", font=("Arial Bold", 12), command=StopButton_cards)
    HideTimerButton = tk.Button(frame , text="Hide timer", font=("Arial Bold", 12))
    QuitToMenuButton = tk.Button(frame , text="Begin", font=("Arial Bold", 12), command=StartButton)

    TimeDelayText = tk.Label(frame, text="Enter time delay (in seconds):  ", font=("Arial Bold", 12))
    TimeDelayEntry = tk.Entry(frame)
    TimeDelayEnterButton = tk.Button(frame, text="Enter", command=getTimeDelay)
    RecallButton = tk.Button(frame, text="Recall", command=recall_session)

#-------------------------------------------------------------

    def next_pic():
        if running:
            PauseButton['text'] = "Pause"
            if card_label.counter == len(card_label.photos):
                return
            else:
                card_label['image'] = card_label.photos[card_label.counter%len(card_label.photos)]
                card_label.after(timeStep, next_pic)
                card_label.counter += 1
                print(card_label.counter)
        else:
            PauseButton['text'] = "Unpause"

#-------------------------------------------------------------

#    card_label.pack()

#    QuitToMenuButton.pack(side=tk.LEFT)
#    PauseButton.pack(side=tk.LEFT)
#    HideTimerButton.pack(side=tk.LEFT)

    TimeDelayText.grid(row=0,column=0)
    TimeDelayEntry.grid(row=0,column=1)
    TimeDelayEnterButton.grid(row=0, column=2)

    QuitToMenuButton.grid(row=1,column=1)
    PauseButton.grid(row=1,column=2)
    HideTimerButton.grid(row=1,column=3)
    RecallButton.grid(row=1,column=4)
    card_label.grid(row=3,column=2)
    clock_label.grid(row = 5, column = 2)

    next_pic()
    
###############################################################

def driver():
    main_menu()
    window.mainloop()

###############################################################

driver()
