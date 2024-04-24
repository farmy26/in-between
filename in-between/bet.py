#IN BETWEEN
# JESSIE RECIO AND SHAUN MISTULA
# NCP1 2021-2022

import os, random, sys, pygame, time
import tkinter as tk
from tktooltip import ToolTip
from tkinter.messagebox import *
from PIL import ImageTk, Image, ImageSequence

window = tk.Tk()
window.title('IN BETWEEN')
window.geometry('1280x720')
window.eval('tk::PlaceWindow . left')

pygame.mixer.init()
print('Game Startup')

#Bg in game
bg = Image.open('Images/Backgrounds/bgwow.jpg')
bg = ImageTk.PhotoImage(image= bg)

bgMain = Image.open('Images/Backgrounds/bgMain.jpg')
bgMain = ImageTk.PhotoImage(image= bgMain)
lblBgMain = tk.Label(window, image=bgMain)
lblBgMain.place(x=0,y=0)

print('-runnning splash screen '
      '\n Loading images '
      '\n Loading Game'
      '\n Loading buttons '
      '\n loading start screen')
#splash
slsh = Image.open('Images/Backgrounds/intro.gif')
lblslsh = tk.Label(window)
lblslsh.pack()

for slsh in ImageSequence.Iterator(slsh):
    slsh = (ImageTk.PhotoImage(image=slsh))
    lblslsh.config(image=slsh)
    window.update()
print('-Done showing splash')

#Images HERE
quitBG = Image.open('Images/Backgrounds/bgdimQuit.jpg')
quitBG = ImageTk.PhotoImage(image= quitBG)

rstBG = Image.open('Images/Backgrounds/bgdimRestart.jpg')
rstBG = ImageTk.PhotoImage(image= rstBG)

restartImg = Image.open('Images/Buttons/restart.jpg')
restartImg = ImageTk.PhotoImage(image=restartImg)

restartEnd = Image.open('Images/Buttons/endRestart.jpg')
restartEnd = ImageTk.PhotoImage(image=restartEnd)

quitImg = Image.open('Images/Buttons/quit.jpg')
quitImg = ImageTk.PhotoImage(image=quitImg)

quitEnd = Image.open('Images/Buttons/endQuit.jpg')
quitEnd = ImageTk.PhotoImage(image= quitEnd)

dealImg = Image.open('Images/Buttons/deal.jpg')
dealImg = ImageTk.PhotoImage(image=dealImg)

ndealImg = Image.open('Images/Buttons/NDeal.jpg')
ndealImg = ImageTk.PhotoImage(image=ndealImg)

lowerImg = Image.open('Images/Buttons/lower.jpg')
lowerImg = ImageTk.PhotoImage(image=lowerImg)

higherImg = Image.open('Images/Buttons/higher.jpg')
higherImg = ImageTk.PhotoImage(image=higherImg)

yesImg = Image.open('Images/Buttons/yes.jpg')
yesImg = ImageTk.PhotoImage(image=yesImg)

noImg = Image.open('Images/Buttons/no.jpg')
noImg = ImageTk.PhotoImage(image=noImg)

betImg = Image.open('Images/Buttons/bet.jpg')
betImg = ImageTk.PhotoImage(image=betImg)

start = Image.open('Images/Buttons/start.jpg')
start = ImageTk.PhotoImage(image=start)

about = Image.open('Images/Buttons/about.jpg')
about = ImageTk.PhotoImage(image=about)

exit = Image.open('Images/Buttons/exit.jpg')
exit = ImageTk.PhotoImage(image=exit)

aboutinf = Image.open('Images/Backgrounds/aboutInf.jpg')
aboutinf = ImageTk.PhotoImage(image=aboutinf)

backImg = Image.open('Images/Buttons/back.jpg')
backImg = ImageTk.PhotoImage(image=backImg)

backSImg = Image.open('Images/Buttons/backS.jpg')
backSImg = ImageTk.PhotoImage(image=backSImg)

cover = Image.open('Images/Banners/cover.jpg')
cover = ImageTk.PhotoImage(image=cover)

coverWon = Image.open('Images/Banners/youWin.jpg')
coverWon = ImageTk.PhotoImage(image=coverWon)

coverLose = Image.open('Images/Banners/youLose.jpg')
coverLose = ImageTk.PhotoImage(image=coverLose)

audOn = Image.open('Images/Buttons/audOn.jpg')
audOn = ImageTk.PhotoImage(image=audOn)

audOff = Image.open('Images/Buttons/audOff.jpg')
audOff = ImageTk.PhotoImage(image=audOff)

audOns = Image.open('Images/Buttons/audONs.jpg')
audOns = ImageTk.PhotoImage(image=audOns)

audOffs = Image.open('Images/Buttons/audOffs.jpg')
audOffs = ImageTk.PhotoImage(image=audOffs)

revealImg = Image.open('Images/Buttons/reveal.jpg')
revealImg = ImageTk.PhotoImage(image=revealImg)

menuImg = Image.open('Images/Backgrounds/menu.jpg')
menuImg = ImageTk.PhotoImage(image=menuImg)

menubtnImg = Image.open('Images/Buttons/menubtn.jpg')
menubtnImg = ImageTk.PhotoImage(image=menubtnImg)

helpbtnImg = Image.open('Images/Buttons/HELP.jpg')
helpbtnImg = ImageTk.PhotoImage(image=helpbtnImg)

helpimg = Image.open('Images/Banners/helpinfo.jpg')
helpimg = ImageTk.PhotoImage(image=helpimg)

resultSrn0 = Image.open('Images/Backgrounds/resultsreen0.jpg')
resultSrn0 = ImageTk.PhotoImage(image=resultSrn0)

resultSrn1 = Image.open('Images/Backgrounds/resultsreen1.jpg')
resultSrn1 = ImageTk.PhotoImage(image=resultSrn1)

resultSrn2 = Image.open('Images/Backgrounds/resultsreen2.jpg')
resultSrn2 = ImageTk.PhotoImage(image=resultSrn2)

resultSrn3 = Image.open('Images/Backgrounds/resultsreen3.jpg')
resultSrn3 = ImageTk.PhotoImage(image=resultSrn3)

#Card images
#Non-striped
card1 = Image.open('Images/Cards/card1.jpg')
card1 = ImageTk.PhotoImage(image= card1)

card2 = Image.open('Images/Cards/card2.jpg')
card2 = ImageTk.PhotoImage(image= card2)

card3 = Image.open('Images/Cards/card3.jpg')
card3 = ImageTk.PhotoImage(image= card3)

card4 = Image.open('Images/Cards/card4.jpg')
card4 = ImageTk.PhotoImage(image= card4)

card5 = Image.open('Images/Cards/card5.jpg')
card5 = ImageTk.PhotoImage(image= card5)

card6 = Image.open('Images/Cards/card6.jpg')
card6 = ImageTk.PhotoImage(image= card6)

card7 = Image.open('Images/Cards/card7.jpg')
card7 = ImageTk.PhotoImage(image= card7)

card8 = Image.open('Images/Cards/card8.jpg')
card8 = ImageTk.PhotoImage(image= card8)

card9 = Image.open('Images/Cards/card9.jpg')
card9 = ImageTk.PhotoImage(image= card9)

card10 = Image.open('Images/Cards/card10.jpg')
card10 = ImageTk.PhotoImage(image= card10)

card11 = Image.open('Images/Cards/card11.jpg')
card11 = ImageTk.PhotoImage(image= card11)

card12 = Image.open('Images/Cards/card12.jpg')
card12 = ImageTk.PhotoImage(image= card12)

card13 = Image.open('Images/Cards/card13.jpg')
card13 = ImageTk.PhotoImage(image= card13)

#Striped
card1s = Image.open('Images/Cards/Stripe/card1S.jpg')
card1s = ImageTk.PhotoImage(image= card1s)

card2s = Image.open('Images/Cards/Stripe/card2S.jpg')
card2s = ImageTk.PhotoImage(image= card2s)

card3s = Image.open('Images/Cards/Stripe/card3S.jpg')
card3s = ImageTk.PhotoImage(image= card3s)

card4s = Image.open('Images/Cards/Stripe/card4S.jpg')
card4s = ImageTk.PhotoImage(image= card4s)

card5s = Image.open('Images/Cards/Stripe/card5S.jpg')
card5s = ImageTk.PhotoImage(image= card5s)

card6s = Image.open('Images/Cards/Stripe/card6S.jpg')
card6s = ImageTk.PhotoImage(image= card6s)

card7s = Image.open('Images/Cards/Stripe/card7S.jpg')
card7s = ImageTk.PhotoImage(image= card7s)

card8s = Image.open('Images/Cards/Stripe/card8S.jpg')
card8s = ImageTk.PhotoImage(image= card8s)

card9s = Image.open('Images/Cards/Stripe/card9S.jpg')
card9s = ImageTk.PhotoImage(image= card9s)

card10s = Image.open('Images/Cards/Stripe/card10S.jpg')
card10s = ImageTk.PhotoImage(image= card10s)

card11s = Image.open('Images/Cards/Stripe/card11S.jpg')
card11s = ImageTk.PhotoImage(image= card11s)

card12s = Image.open('Images/Cards/Stripe/card12S.jpg')
card12s = ImageTk.PhotoImage(image= card12s)

card13s = Image.open('Images/Cards/Stripe/card13S.jpg')
card13s = ImageTk.PhotoImage(image= card13s)

#BLANK CARD
cardBLK = Image.open('Images/Cards/cardBLANK.jpg')
cardBLK = ImageTk.PhotoImage(image= cardBLK)

print('-Images loaded')

#IDLE CARD STATE
lblcard1ID = tk.Label(window,
                  image=cardBLK)
lblcard1ID.place(x=100,y=220)
lblcard2ID = tk.Label(window,
                   image=cardBLK)
lblcard2ID.place(x=150,y=230)

lblcard3ID = tk.Label(window,
                   image=cardBLK)
lblcard3ID.place(x=200,y=240)

#Bet HERE
entBet = tk.Entry(window,
                  font=('Crete Round',100),
                  fg='white',
                  bg='black',
                  justify='center',
                  width=5)
entBet.place(x=860,y=260)

#COINS WHAT
lblCoins = tk.Label(window,text='2000',font=("Crete Round", 15), fg='white',bg='black')
lblCoins.place(x=1131,y=141)

ToolTip(lblCoins,
        msg="Your coins!",

        parent_kwargs={"bg": "black", "padx": 5, "pady": 5},
        fg="#ffffff",
        bg="#1c1c1c",
        padx=10, pady=10)

#Insert functions here
list_rand = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#list_rand = [1]
def card1rng():
  randa = random.choice(list_rand)
  return randa

def card2rng():
  randa = random.choice(list_rand)
  return randa

def card3rng():
  randa = random.choice(list_rand)
  return randa

def mainGame():
    global btnDeal, btnNDeal, btnMenu, coins
    print('-'*30,'\nPC generated random cards \n User revealed the two Cards!\n')

    try:
        btnReveal.destroy()
        btnReveal1.destroy()
    except:
        pass

    btnDeal = tk.Button(window,
                        image= dealImg,
                        height=59,
                        width=137,
                        command=lambda : [(processing())])
    btnDeal.config(borderwidth=0,
                    highlightthickness = -100)
    btnDeal.place(x=490,y=650)

    btnNDeal = tk.Button(window,
                         image= ndealImg,
                         height=59,
                         width=137,
                         command= lambda :[(noDeal(),clearText())])
    btnNDeal.config(borderwidth=0,
                     highlightthickness = -100)
    btnNDeal.place(x=660,y=650)

    def processing():
        try: #AAA
            int(entBet.get())
            if (int(entBet.get()) <= coins):
                if int(entBet.get()) <= 0:
                    showwarning(message="You cannot enter 0 as BET!")
                else:
                    if int(entBet.get()) <= 50:
                        showwarning(message="Sorry you cannot enter a BET lower or equal to a 50!!")
                    else:
                        click = pygame.mixer.Sound ('Audio/click.mp3')
                        click.play()
                        print('ornord im processing')
                        if (card1d < card3d and card2d > card3d) or (card1d > card3d and card2d < card3d):
                            btnDeal.destroy()
                            btnNDeal.destroy()
                            btnMenu.destroy()
                            #win thingy
                            window.after(2000)
                            lblresult = tk.Label(window,
                                        image=coverWon,
                                        height=400,
                                        width=425)
                            lblresult.place(x=98,y=210)
                            window.after(3000, lblresult.destroy)

                            print('aye the user won')
                            showThirdCard()
                            click = pygame.mixer.Sound ('Audio/winSound.mp3')
                            click.play()
                            click = pygame.mixer.Sound ('Audio/addCoins.mp3')\

                            window.after(2000,click.play)
                            window.after(2000,winCoins)
                            window.after(4000,coinsDefColor)
                            clearText()
                            print('Middle card is in between : ',card1d,card3d,card2d)
                            lblcard.destroy()
                            lblcard2.destroy()
                            lblcard3.destroy()
                            window.after(3500,roundCheckPoint)
                        elif (card1d == card2d):
                            print('same card, different statements')
                            btnDeal.destroy()
                            btnNDeal.destroy()
                            btnMenu.destroy()
                            global btnLower, btnHigher
                            btnLower = tk.Button(window,
                                                image= lowerImg,
                                                height=59,
                                                width=137,
                                                command= lambda :[(lowerChoice())])
                            btnLower.config(borderwidth=0,
                                            highlightthickness = -100)
                            btnLower.place(x=490,y=650)

                            btnHigher = tk.Button(window,
                                                 image= higherImg,
                                                 height=59,
                                                 width=137,
                                                 command=lambda :[(higherChoice())])
                            btnHigher.config(borderwidth=0,
                                             highlightthickness = -100)
                            btnHigher.place(x=660,y=650)
                        else:
                            btnDeal.destroy()
                            btnNDeal.destroy()
                            btnMenu.destroy()
                            window.after(2000)
                            lblresult = tk.Label(window,
                                        image=coverLose,
                                        height=400,
                                        width=425)
                            lblresult.place(x=98,y=210)
                            lblcard.destroy()
                            lblcard2.destroy()
                            lblcard3.destroy()
                            window.after(3000, lblresult.destroy)
                            print('oh no the user loss')
                            showThirdCard()
                            click = pygame.mixer.Sound ('Audio/loseSound.mp3')
                            click.play()
                            click = pygame.mixer.Sound ('Audio/minusCoins.mp3')

                            window.after(2000,click.play)
                            window.after(2000,loseCoins)
                            window.after(4000,coinsDefColor)

                            print('Middle card is not in between : ',card1d,card3d,card2d)
                            window.after(3500,roundCheckPoint)
                            clearText()
                        print('ornord process done\n','-'*30)
            else:
                showwarning(message="Your bet is higher than your coins")
        except: #AAA
            showinfo(title="Error Input",message="Oops, it seems like you haven't entered you BET!!")

    cardChanger()

    btnMenu = tk.Button(window,
                        image= menubtnImg,
                        height=40,
                        width=95,
                        command=menu)
    btnMenu.config(borderwidth=0,
                   highlightthickness = -100)
    btnMenu.place(x=110,y=650)

    ToolTip(btnMenu,
        msg="more options",
        delay=0.75,
        parent_kwargs={"bg": "black", "padx": 5, "pady": 5},
        fg="#ffffff",
        bg="#1c1c1c",
        padx=10, pady=10)

    highEarn()
    print('main game running\n waiting for the deal\n\t\t 0_0')
    #return run

def helpME():
    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()
    def closeHelp():
        click = pygame.mixer.Sound ('Audio/click.mp3')
        click.play()
        lblHelpMe.destroy()
        btnBackM.destroy()
    lblHelpMe = tk.Label(window, image=helpimg)
    lblHelpMe.place(x=0,y=0)
    btnBackM = tk.Button(window,
                        image= backSImg,
                        height=40,
                        width=95,
                         command=closeHelp)
    btnBackM.config(borderwidth=0,
                   highlightthickness = -100)
    btnBackM.place(x=190,y=630)

def cardChanger():
        global card1d, card2d, card3d, lblcard

        card1d = card1rng()
        print(card1d,'i am card 1\n')
        card2d = card2rng()
        print(card2d,'i am card 2\n')
        card3d = card3rng()
        print(card3d,'i am the hidden card\n')


        if card1d == 1:
            window.after(5000)
            lblcard = tk.Label(window,
                               image=card1)
            lblcard.place(x=110,y=210)
            print('i ran to the door i said awoo')
        elif card1d == 2:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card2s)
            lblcard.place(x=110,y=210)
            print('i ran to the door i said awoo')

        elif card1d == 3:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card3)
            lblcard.place(x=110,y=210)

        elif card1d == 4:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card4s)
            lblcard.place(x=110,y=210)

        elif card1d == 5:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card5)
            lblcard.place(x=110,y=210)

        elif card1d == 6:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card6s)
            lblcard.place(x=110,y=210)

        elif card1d == 7:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card7)
            lblcard.place(x=110,y=210)

        elif card1d == 8:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card8s)
            lblcard.place(x=110,y=210)

        elif card1d == 9:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card9)
            lblcard.place(x=110,y=210)

        elif card1d == 10:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card10s)
            lblcard.place(x=110,y=210)

        elif card1d == 11:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card11)
            lblcard.place(x=110,y=210)

        elif card1d == 12:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card12s)
            lblcard.place(x=110,y=210)

        elif card1d == 13:
            window.after(2000)
            lblcard = tk.Label(window,
                                image=card13)
            lblcard.place(x=110,y=210)

        else:
            pass

        def cardtwoCH():
            global lblcard2
            if card2d == 1:
                lblcard2 = tk.Label(window,
                                    image=card1s)
                lblcard2.place(x=230,y=240)
                print('i ran to the door i said awoo')
            elif card2d == 2:
                lblcard2 = tk.Label(window,
                           image=card2)
                lblcard2.place(x=230,y=240)
                print('i ran to the door i said awoo')

            elif card2d == 3:
                lblcard2 = tk.Label(window,
                           image=card3s)
                lblcard2.place(x=230,y=240)

            elif card2d == 4:
                lblcard2 = tk.Label(window,
                           image=card4)
                lblcard2.place(x=230,y=240)

            elif card2d == 5:
                lblcard2 = tk.Label(window,
                           image=card5s)
                lblcard2.place(x=230,y=240)

            elif card2d == 6:
                lblcard2 = tk.Label(window,
                           image=card6)
                lblcard2.place(x=230,y=240)

            elif card2d == 7:
                lblcard2 = tk.Label(window,
                           image=card7s)
                lblcard2.place(x=230,y=240)

            elif card2d == 8:
                lblcard2 = tk.Label(window,
                           image=card8)
                lblcard2.place(x=230,y=240)

            elif card2d == 9:
                lblcard2 = tk.Label(window,
                           image=card9s)
                lblcard2.place(x=230,y=240)

            elif card2d == 10:
                lblcard2 = tk.Label(window,
                           image=card10)
                lblcard2.place(x=230,y=240)

            elif card2d == 11:
                lblcard2 = tk.Label(window,
                           image=card11s)
                lblcard2.place(x=230,y=240)

            elif card2d == 12:
                lblcard2 = tk.Label(window,
                           image=card12)
                lblcard2.place(x=230,y=240)

            elif card2d == 13:
                lblcard2 = tk.Label(window,
                           image=card13s)
                lblcard2.place(x=230,y=240)

            else:
                pass

        def card3Hidden():
            global lblcard3
            lblcard3 = tk.Label(window,
                                   image=cardBLK)
            lblcard3.place(x=540,y=230)

            ToolTip(lblcard3,
            msg="Click deal to see if this card is IN-BETWEEN!",
            #delay=0.75,
            parent_kwargs={"bg": "black", "padx": 5, "pady": 5},
            fg="#ffffff",
            bg="#1c1c1c",
            padx=10, pady=10)

        window.after(0x400, card3Hidden)
        window.after(0x200, cardtwoCH)
        cards = pygame.mixer.Sound ('Audio/cards.mp3')
        cards.play()
        print('PC SHOWED THE CARDS\n')

def showThirdCard():
    if card3d == 1:
        lblcard3 = tk.Label(window,
                            image=card1)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

        print('i ran to the door i said awoo')
    elif card3d == 2:
        lblcard3 = tk.Label(window,
                   image=card2s)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)
        print('i ran to the door i said awoo')

    elif card3d == 3:
        lblcard3 = tk.Label(window,
                   image=card3)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 4:
        lblcard3 = tk.Label(window,
                   image=card4s)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 5:
        lblcard3 = tk.Label(window,
                   image=card5)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 6:
        lblcard3 = tk.Label(window,
                   image=card6s)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 7:
        lblcard3 = tk.Label(window,
                   image=card7)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 8:
        lblcard3 = tk.Label(window,
                   image=card8s)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 9:
        lblcard3 = tk.Label(window,
                   image=card9)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 10:
        lblcard3 = tk.Label(window,
                            image=card10s)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 11:
        lblcard3 = tk.Label(window,
                        image=card11)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 12:
        lblcard3 = tk.Label(window,
                            image=card12s)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    elif card3d == 13:
        lblcard3 = tk.Label(window,
                            image=card13)
        lblcard3.place(x=540,y=230)
        window.after(4000, lblcard3.destroy)

    else:
        pass
    window.after(3000,lblcard3.destroy)

def lowerChoice():
    try:
         if int(entBet.get()) <= coins:
             int(entBet.get())
             btnHigher.destroy()
             btnLower.destroy()
             if (card3d < card1d) or (card3d < card2d):
                 lblresult = tk.Label(window,
                                      image=coverWon,
                                      height=400,
                                      width=425)
                 lblresult.place(x=98,y=210)

                 click = pygame.mixer.Sound ('Audio/winSound.mp3')
                 click.play()
                 click = pygame.mixer.Sound ('Audio/addCoins.mp3')
                 lblcard.destroy()
                 lblcard2.destroy()
                 lblcard3.destroy()

                 window.after(2000,click.play)
                 window.after(2000,winCoins)
                 window.after(4000,coinsDefColor)
                 # window.after(3000,lblshowcards.destroy)
                 window.after(3000,lblresult.destroy)
                 print('LOWER win')
             else:
                lblresult = tk.Label(window,
                                     image=coverLose,
                                     height=400,
                                     width=425)
                lblresult.place(x=98,y=210)
                click = pygame.mixer.Sound ('Audio/loseSound.mp3')
                click.play()
                click = pygame.mixer.Sound ('Audio/minusCoins.mp3')
                lblcard.destroy()
                lblcard2.destroy()
                lblcard3.destroy()
                window.after(2000,click.play)
                window.after(2000,loseCoins)
                window.after(4000,coinsDefColor)
                # window.after(3000, lblshowcards.destroy)
                window.after(3000, lblresult.destroy)
             showThirdCard()
             window.after(3500,roundCheckPoint)
         else:
             showwarning(message="Your bet is higher than your coins!!")
    except:
        showinfo(title="Error in input", message="Oops, There is something wrong with your input ")
    highEarn()
    clearText()

def higherChoice():
    global coins

    try: #AAA
        int(entBet.get())
        if int(entBet.get()) <= coins:
            btnHigher.destroy()
            btnLower.destroy()
            if (card3d > card1d) or (card3d > card2d):
                lblresult = tk.Label(window,
                                    image=coverWon,
                                    height=400,
                                    width=425)
                lblresult.place(x=98,y=210)
                click = pygame.mixer.Sound ('Audio/winSound.mp3')
                click.play()
                click = pygame.mixer.Sound ('Audio/addCoins.mp3')
                lblcard.destroy()
                lblcard2.destroy()
                lblcard3.destroy()
                window.after(2000,click.play)
                window.after(2000,winCoins)
                window.after(4000,coinsDefColor)

                window.after(2000)
                window.after(3000, lblresult.destroy)
                print('HIGHER win')
            else:
                showThirdCard()
                lblresult = tk.Label(window,
                                    image=coverLose,
                                    height=400,
                                    width=425)
                lblresult.place(x=98,y=210)
                click = pygame.mixer.Sound ('Audio/loseSound.mp3')
                click.play()
                click = pygame.mixer.Sound ('Audio/minusCoins.mp3')
                lblcard.destroy()
                lblcard2.destroy()
                lblcard3.destroy()
                window.after(2000,click.play)
                window.after(2000,loseCoins)
                window.after(4000,coinsDefColor)

                window.after(3000, lblresult.destroy)
            showThirdCard()
            window.after(3500,roundCheckPoint)
        else:
            showwarning(message="Your bet is higher than your coins!!")
    except:
        showinfo(title="Error in input", message="Oops, There is something wrong with your input!!")
    highEarn()
    clearText()

def noDeal():
    print('User dont want no deal :(')
    btnDeal.destroy()
    btnNDeal.destroy()
    btnMenu.destroy()
    lblresult = tk.Label(window,
                         image=coverLose,
                         height=400,
                         width=425)
    lblresult.place(x=98,y=210)
    window.after(3000, lblresult.destroy)
    showThirdCard()
    click = pygame.mixer.Sound ('Audio/loseSound.mp3')
    click.play()
    click = pygame.mixer.Sound ('Audio/minusCoins.mp3')
    lblcard.destroy()
    lblcard2.destroy()
    lblcard3.destroy()
    window.after(2000,click.play)
    window.after(2000,coinsND) #NEW
    window.after(4000,coinsDefColor) #NEW
    print(card1d,card3d,card2d)
    print('User lost coins')
    window.after(4000,mainGame)

def coinsDefColor(): #AAA
    global coins, lblCoins
    lblCoins.config(text=coins, fg='white')

def coinsND(): #AAA
    global coins, lblCoins
    calcu = round(coins * 0.10)
    coins -= calcu
    lblCoins.config(fg='red')
    lblCoins['text'] = coins

def winCoins(): #AAA
    global coins, lblCoins
    usrBet = int(entBet.get())
    coins += usrBet
    featureCoins()
    lblCoins.config(fg='lime')
    lblCoins['text'] = coins

def loseCoins(): #AAA
    global coins, lblCoins
    usrBet = int(entBet.get())
    coins -= usrBet
    lblCoins.config(fg='red')
    lblCoins['text'] = coins

def featureCoins(): #LAST
    global coins, featureScore
    if coins >= 20000 and featureScore == 0:
        newCoins = round(coins * 0.30)
        coins += newCoins
        lblPopup = tk.Label(window, text="ADDITIONAL 30% :)", fg='white', bg='green', font=('Crete Round', 15))
        lblPopup.place(x=1090, y=100)
        featureScore += 1
        window.after(2000, lblPopup.destroy)
    else:
        pass

def highEarn(): #LAST
    global coins, earning
    if coins > earning:
        earning *= 0
        earning += coins
    else:
        pass

earning = 0

def clearText():
    def clearing():
        entBet.delete(0, 'end')

    window.after(2000,clearing)

word_rand = ['8 ball?, more like 8cards!','Mi Hombre?','Ahhhhs it bit me','Hit the deal button for me.','Tkinter,surpassing its limit',
             'NORDDDDDDDDDDDDD','ORNORDDDDDDDDDDD','From the creators of JackEnTJ!']
def newRand():
    try:
        lblWords.config(text=random.choice(word_rand), font=('Crete Round',15))

        window.after(5000,newRand)
    except:
        pass

def gameStart():
    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()
    try:
        lblcard1ID.destroy()
        lblcard2ID.destroy()
        lblcard3ID.destroy()
    except:
        pass
    mainGame()

def roundCheckPoint():
    if coins <= 50:
        resultTrue()
    else:
        mainGame()

def resultTrue():
    global lblresultSrn, lblroundTkn, btnRestartRE, btnQuitRE
    if earning >= 20000:
        lblresultSrn = tk.Label(window, image=resultSrn3)
        lblresultSrn.place(x=0,y=0)
    elif earning >= 11000:
        lblresultSrn = tk.Label(window, image=resultSrn2)
        lblresultSrn.place(x=0,y=0)
    elif earning >= 5500:
         lblresultSrn = tk.Label(window, image=resultSrn1)
         lblresultSrn.place(x=0,y=0)
    else:
        lblresultSrn = tk.Label(window, image=resultSrn0)
        lblresultSrn.place(x=0,y=0)
    btnRestartRE = tk.Button(window,
                        image=restartEnd,
                        width=133,
                        height=54,
                        command= restartEndCmd)
    btnRestartRE.place(x=490,y=650)

    btnQuitRE = tk.Button(window,
                        image=quitEnd,
                        width=133,
                        height=54,
                        command= sys.exit)
    btnQuitRE.place(x=660,y=650)

    lblroundTkn = tk.Label(window, text=('HIGHEST COINS : ' + str(earning)), fg='white', bg='black', font=('Crete Round', 50))
    lblroundTkn.pack(pady=300)
    print('User had less than 50 coins!\n User lost!\n', '-'*30)
def restartEndCmd():
    try:
        lblresultSrn.destroy()
    except:
        pass

    lblroundTkn.destroy()
    btnRestartRE.destroy()
    btnQuitRE.destroy()
    resetData()

def quitBtn():
    def usrNo():
        click = pygame.mixer.Sound ('Audio/click.mp3')
        click.play()
        lblqst.destroy()
        btnYes.destroy()
        btnNo.destroy()
    def usrYes():
        click = pygame.mixer.Sound ('Audio/click.mp3')
        click.play()
        time.sleep(0.1)
        sys.exit()

    click = pygame.mixer.Sound('Audio/click.mp3') #aaa
    click.play()

    #Quit opt in main game
    lblqst = tk.Label(window,
                      image=quitBG)
    lblqst.place(x=0,y=0)

    btnYes = tk.Button(window,
                       image=yesImg,
                       command=sys.exit)
    btnYes.config(borderwidth=0,
                  highlightthickness = -100,
                  height=59,
                  width=137,
                  command= usrYes)
    btnYes.place(x=410,y=460)

    btnNo = tk.Button(window,
                      image=noImg,
                      command= usrNo)
    btnNo.config(borderwidth=0,
                 highlightthickness = -100)
    btnNo.place(x=740,y=460)

def restart():
    def usrYes():
        backMenu()
        try:
            lblcard1ID.destroy()
            lblcard2ID.destroy()
            lblcard3ID.destroy()
        except:
            pass
        lblqst.destroy()
        btnYes.destroy()
        btnNo.destroy()
        resetData()
        print('User resetted the game! \n\n X_X \n',"-" * 30)

    def usrNo():
        click = pygame.mixer.Sound ('Audio/click.mp3')
        click.play()
        lblqst.destroy()
        btnYes.destroy()
        btnNo.destroy()

    lblqst = tk.Label(window,
                      image=rstBG)
    lblqst.place(x=0,y=0)

    btnYes = tk.Button(window,
                       image=yesImg,
                       command= usrYes)
    btnYes.config(borderwidth=0,
                  highlightthickness = -100)
    btnYes.place(x=410,y=460)


    btnNo = tk.Button(window,
                      image=noImg,
                      command= usrNo)
    btnNo.config(borderwidth=0,
                 highlightthickness = -100)
    btnNo.place(x=740,y=460)
    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()

def resetData():
    global btnReveal1, lblcard, lblcard2,lblcard1ID, lblcard2ID, lblcard3ID, coins, earning, swth
    swth = False
    musicTog()
    lblcard1ID = tk.Label(window,
                      image=cardBLK)
    lblcard1ID.place(x=100,y=220)
    lblcard2ID = tk.Label(window,
                       image=cardBLK)
    lblcard2ID.place(x=150,y=230)
    lblcard3ID = tk.Label(window,
                        image=cardBLK)
    lblcard3ID.place(x=200,y=240)
    try:
        lblcard.destroy()
        lblcard2.destroy()
        lblcard3.destroy()
        btnDeal.destroy()
        btnNDeal.destroy()
        btnMenu.destroy()
    except:
        pass

    btnReveal1 = tk.Button(window,
                           image= revealImg,
                           height=59,
                           width=137,
                           command=lambda :[(gameStart())])
    btnReveal1.config(borderwidth=0,
                      highlightthickness = -100)
    btnReveal1.place(x=600,y=650)

    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()#AAA
    time.sleep(0.1)
    lblreload = tk.Label(window, image=slsh)
    lblreload.place(x=0,
                    y=0)
    addCoins()
    lblCoins.config(text='2000')
    earning = 0

    window.after(2000,pygame.mixer.music.play)
    window.after(2000,lblreload.destroy)

def addCoins(): #NEW
    global coins
    if coins == 0:
        coins += 2000
    else:
        coins *= 0
        coins += 2000

#For Global
coins = 2000
rounds = 0
featureScore = 0
remCoin = 2000

#Switch
global swth_on
swth = True

def musicTog():
    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()
    global swth
    if swth is True:
        btnAudio.config(image=audOffs)
        try:
            btnOnOff.config(image=audOff)
        except:
            pass
        pygame.mixer.music.pause()
        swth = False
    else:
        btnAudio.config(image=audOns)
        try:
            btnOnOff.config(image=audOn)
        except:
            pass
        pygame.mixer.music.play()
        swth = True

print('-Game Function Loaded')
#EMERGENCY LABEL
lblWords = tk.Label(window,text='Hello World',font=('Crete Round',15),bg='maroon',fg='white')
lblWords.pack()

def menu():
    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()
    global lblmenu,btnRst,btnHelpme,btnBackM,btnQuit
    lblmenu = tk.Label(window, image=menuImg)
    lblmenu.place(x=0,y=0)
    #Restart
    btnRst = tk.Button(window,
                       image= restartImg,
                       height=40,
                       width=95,
                       command=restart)
    btnRst.config(borderwidth=0,
                  highlightthickness = -100)
    btnRst.place(x=190,y=330)

    btnHelpme = tk.Button(window,
                          image= helpbtnImg,
                          height=40,
                          width=95,
                          command= helpME)
    btnHelpme.config(borderwidth=0,
                   highlightthickness = -100)
    btnHelpme.place(x=190,y=430)

    btnBackM = tk.Button(window,
                        image= backSImg,
                        height=40,
                        width=95,
                         command=backMenu)
    btnBackM.config(borderwidth=0,
                   highlightthickness = -100)
    btnBackM.place(x=190,y=530)

    #Quit
    btnQuit = tk.Button(window,
                        image= quitImg,
                        height=40,
                        width=95,
                        command=quitBtn)
    btnQuit.config(borderwidth=0,
                   highlightthickness = -100)
    btnQuit.place(x=190,y=630)

def backMenu():
    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()
    lblmenu.destroy()
    btnRst.destroy()
    btnHelpme.destroy()
    btnBackM.destroy()
    btnQuit.destroy()

#Game buttons anyone?
#Reveal
btnReveal = tk.Button(window,
                      image= revealImg,
                      height=59,
                      width=137,
                      command=lambda :[(gameStart(), addCoins())])
btnReveal.config(borderwidth=0,
                highlightthickness = -100)
btnReveal.place(x=600,y=650)


#Music toggle
btnAudio = tk.Button(window,
                   image=audOns,
                   height=40,
                   width=95,
                   command=musicTog)
btnAudio.config(borderwidth=0,
                   highlightthickness = -100)
btnAudio.place(x=1110,y=650)

lblcvr = tk.Label(window, image=bg)
lblcvr.place(x=0,y=0)
print('-Buttons loaded')

#Startscreen
def startnow():
    click = pygame.mixer.Sound('Audio/click.mp3')
    click.play()
    lblstart.destroy()
    btnStart.destroy()
    btnAboutst.destroy()
    btnOnOff.destroy()
    btnExit.destroy()
    window.after(1500, lblcvr.destroy)
    window.after(1500, lblslsh.destroy)

    lblGreet = tk.Label(window, image=slsh)
    lblGreet.place(x=0,y=0)
    print("User wanted to play!\n WELCOME TO IN-BETWEEN!\n")
    window.after(2000, lblGreet.destroy)

#About us
def aboutInfo():
    def back():
        click = pygame.mixer.Sound('Audio/click.mp3')
        click.play()
        lblAbout.destroy()
        btnBack.destroy()
    lblAbout = tk.Label(window, image=aboutinf)
    lblAbout.place(x=0,y=0)

    btnBack = tk.Button(window,
                        image=backImg,
                        width=133,
                        height=54,
                        command= back)
    btnBack.place(x=600,y=610)

    click = pygame.mixer.Sound ('Audio/click.mp3')
    click.play()

#Startscreen buttons
lblstart = tk.Label(window, image=bg)
lblstart.place(x=0,y=0)
btnStart = tk.Button(window,
                     image=start,
                     command=startnow,
                     width=133,
                     height=54)
btnStart.place(x=340,y=415)

btnAboutst = tk.Button(window,
                       image=about,
                       width=133,
                       height=54,
                       command=aboutInfo)
btnAboutst.place(x=240,y=280)

btnExit = tk.Button(window,
                    image=exit,
                    width=133,
                    height=54,
                    command=quitBtn)
btnExit.place(x=240,y=550)

btnOnOff = tk.Button(window,
                     image=audOn,
                     width=133,
                     height=54,
                     command=musicTog)
btnOnOff.place(x=120,y=415)

print('-startscreen has been loaded')

pygame.mixer.music.load('Audio/bgm.mp3')
pygame.mixer.music.play()

ToolTip(entBet,
        msg="Enter your bet here",
        #delay=0.75,
        parent_kwargs={"bg": "black", "padx": 5, "pady": 5},
        fg="#ffffff",
        bg="#1c1c1c",
        padx=10, pady=10)


print('-Game is running')

window.after(5000,newRand) #TESTING
window.resizable(False, False)
window.mainloop()
