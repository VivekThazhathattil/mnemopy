import collections
import random
import time 
import tkinter as tk
from PIL import ImageTk, Image

###############################################################
#TODO 1) Remove the lag in loading Speed Cards
#TODO 2) Add a generic timer useful for all events
#TODO 3) Complete scripting for 5-minute numbers
###############################################################

window = tk.Tk()
window.title("Mnemopy by Vivek")
window.geometry('800x500')  # set window size
window.resizable(0, 0)  # fix window

frame = tk.Frame(window)
frame.pack()

running = False
begun = False

###############################################################

def update_clock():
    clock_label = tk.Label(frame)
    now = time.strftime("%H:%M:%S")
    clock_label.configure(text=now)
    after(1000, self.update_clock)

def main_menu():
    clearFrame()

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

    im1 = None 

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

    photos = []
    for j in images:
        img = ImageTk.PhotoImage(Image.open(j).resize((150, 250)))
        photos = photos + [img]
    card_label = tk.Label(frame)
    card_label.photos = photos
    card_label.counter = 0

#-------------------------------------------------------------

    def StartButton():
        global running
        global begun

        if TimeDelayText:
            TimeDelayEntry.destroy()
            TimeDelayText.destroy()
            TimeDelayEnterButton.destroy()

        if not begun:
            print("Process begun")
            QuitToMenuButton['text'] = "Quit"
            begun = True
            running = True
            next_pic()

        else:
            print("Process terminated")
            running = False
            begun = False
            main_menu()

#-------------------------------------------------------------

    def StopButton_cards():
        global running
        global begun
        if running and begun:
            print("Paused!")
            running = not running
        elif not running and begun:
            print("Unpaused!")
            running = not running
            next_pic()
        elif running and not begun:
            running = not running
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

    next_pic()
    
###############################################################

def driver():
    main_menu()
    window.mainloop()

###############################################################

driver()
