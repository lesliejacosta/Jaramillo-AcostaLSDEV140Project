"""
Program: Jaramillo-AcostaLSDEV140Project.py
Author: Leslie Jaramillo-Acosta
Last date modified: July 17th, 2023
Purpose: The office Trivia using a GUI
"""

from tkinter import * #importing tkinter which allows the GUI to run on python
from breezypythongui import EasyFrame #allows GUI to run smoothly
from PIL import ImageTk, Image #allows images to work in the code


class office(EasyFrame): #naming the class where all of the code will fall

    def __init__(self):

        EasyFrame.__init__(self, title='how well do you know the office?', background=None)
        #titling the window and setting the background to none

        self.setSize(width=1500, height=1000) #setting the size of the window that will open


        #a popup message will show up explaining how to use the program
        self.messageBox(title="Welcome", message=
                                                 "\n1)Open application to full screen"
                                                 " \n2)Turn off night or dark mode"
                                                "\n3)Have fun!", width=40, height=10)




        self.addButton(text="New Game", row=38, column=4, command=self.newGame)
        #a button to restart or start a new game. It resets everything to its original spot


        self.addButton(text="Exit", row=38, column=5, command=self.Exit)
        #closes the window(s)


        self.addButton(text="Calculate Score", row=38, column=3, command=self.calc)
        #calculates the user's score


        self.questAnswered=0 #questAnswered is a variable which counts how many questions the user has answered
        self.points=0 #points is a variable which counts how many questions the user has answered correctly
        self.wrongPoints=0 #wrongPoints is a variable which counts how many questions the user has answered incorrectly



        # question 1
        self.labela = self.addLabel("1) What did Kevin spill on the carpet?", row=4, column=0, font=('American Typewriter', 15), background=None)
        #adding the question as a label

        # adds button options and when they're clicked the command will follow
        self.addButton(text="Chili", row=6,column=2, command=self.right1)
        self.addButton(text="M&Ms", row=6, column=0,command=self.wrong1)
        self.addButton(text="Soup", row=5, column=2, command=self.wrong1)
        self.addButton(text="Broccoli", row=5, column=0, command=self.wrong1)

        self.label1 = self.addLabel(text="", row=7, column=0, rowspan=1 )
        # makes the space where the outcome of the answer will appear


        # question 2
        self.labelb =self.addLabel(text="2) Who were the original members of the PPC?", row=10, column=0, font=('American Typewriter',15), background=None)
        # adding the question as a label

        # adds button options and when they're clicked the command will follow
        self.addButton(text="Pam, Angela, and Phylis", row=11, column=0, command=self.right2)
        self.addButton(text="Michael, Pam, and Kelly", row=12, column=0, command=self.wrong2)
        self.addButton(text="Jim, Dwight, and Michael", row=11, column=2, command=self.wrong2)
        self.addButton(text="Kelly, Pam, and Stanley", row=12, column=2, command=self.wrong2)

        self.label2 = self.addLabel(text=" ", row=13, column=0)
        # makes the space where the outcome of the answer will appear


        # question 3
        self.labelc =self.addLabel(text="3) Who actually came up with the idea for WUPHF.com?", row=15, column=0, font=('American Typewriter',15), background=None)
        # adding the question as a label

        # adds button options and when they're clicked the command will follow
        self.addButton(text="Pam", row=16, column=0, command=self.wrong3)
        self.addButton(text="Kelly", row=16, column=2, command=self.right3)
        self.addButton(text="Jim", row=17, column=0, command=self.wrong3)
        self.addButton(text="Ryan", row=17, column=2, command=self.wrong3)

        self.label3 = self.addLabel(text=" ", row=18, column=0)
        # makes the space where the outcome of the answer will appear


        # question 4
        self.labeld =self.addLabel(text="4) Why does Dwight use brown and grey balloons for Kelly's birthday party?"
                                   , row=20, column=0, font=('American Typewriter',15), background=None)
        # adding the question as a label

        # adds button options and when they're clicked the command will follow
        self.addButton(text="They match the carpet", row=22, column=0, command=self.right4)
        self.addButton(text="They're Kelly's favorite colors", row=21, column=0, command=self.wrong4)
        self.addButton(text="They're Dwight's favorite colors", row=21, column=2, command=self.wrong4)
        self.addButton(text="The colors symbolize wisdom", row=22, column=2, command=self.wrong4)

        self.label4 = self.addLabel(text=" ", row=23, column=0)
        # makes the space where the outcome of the answer will appear

        # question 5
        self.labele =self.addLabel(text="5) What is Michael's middle name?", row=25, column=0, font=('American Typewriter',15), background=None)
        # adding the question as a label

        # adds button options and when they're clicked the command will follow
        self.addButton(text="Gary", row=26, column=0, command=self.right5)
        self.addButton(text="James", row=27, column=0, command=self.wrong5)
        self.addButton(text="Kurt", row=26, column=2, command=self.wrong5)
        self.addButton(text="Larry", row=27, column=2, command=self.wrong5)

        self.label5 = self.addLabel(text=" ", row=28, column=0)
        # makes the space where the outcome of the answer will appear


        # question 6
        self.labelf =self.addLabel(text="6) What do Stanley and Dwight gain from Jim's prank?", row=30, column=0, font=('American Typewriter',15), background=None)
        # adding the question as a label

        # adds button options and when they're clicked the command will follow
        self.addButton(text="customers", row=31, column=0, command=self.wrong6)
        self.addButton(text="meatballs", row=31, column=2, command=self.right6)
        self.addButton(text="pens", row=32, column=0, command=self.wrong6)
        self.addButton(text="eggs", row=32, column=2, command=self.wrong6)

        self.label6 = self.addLabel(text=" ", row=33, column=0)
        # makes the space where the outcome of the answer will appear

        # question 7
        self.labelg =self.addLabel(text="7) What is Karen's Husband's name?", row=35, column=0, font=('American Typewriter',15), background=None)
        # adding the question as a label

        # adds button options and when they're clicked the command will follow
        self.addButton(text="Jim", row=36, column=0, command=self.wrong7)
        self.addButton(text="Dan", row=37, column=0, command=self.right7)
        self.addButton(text="Tim", row=36, column=2, command=self.wrong7)
        self.addButton(text="Brad", row=37, column=2, command=self.wrong7)

        self.label7 = self.addLabel(text=" ", row=38, column=0)
        # makes the space where the outcome of the answer will appear

        #scoring
        self.labelScore = self.addLabel(text="Score:", row=5, column=4, font=('American Typewriter', 30), background=None)
        #places "score" on the right side of the screen for the user to see what their score was at the end of the game

        self.labelFinal= self.addLabel(text="", row=10, column=4)
        #adds a space for the outcome of the user's score to appear



    #right commands for each question

    #when the right answer to the first question is clicked
    def right1(self):
        #disables the buttons so the user can't change their answer
        self.addButton(text="Chili", row=6, column=2, state='disabled')
        self.addButton(text="M&Ms", row=6, column=0, state='disabled')
        self.addButton(text="Soup", row=5, column=2, state='disabled')
        self.addButton(text="Broccoli", row=5, column=0, state='disabled')


        self.questAnswered=self.questAnswered+1 #adds one to the amount of questions the user has answered
        self.points = self.points + 1 #adds one to the amount of questions the user has answered correctly

        #if there is an error or the user hasn't restarted the game correctly there will be to many questions answered
        #and the user will be asked to restart the game again
        if self.questAnswered >= 7:
            self.label1["text"] = "Number of answers given are invalid, click 'New Game' at the bottom right of the " \
                                  "screen"

        #else the program will tell the user they have gotten the question correct and how many points they've
        #gotten in total
        else:
            self.label1['text'] = "correct, total points: " + str(self.points)


    # when the right answer to the second question is clicked
    def right2(self):
        # disables the buttons so the user can't change their answer
        self.addButton(text="Pam, Angela, and Phylis", row=11, column=0, state='disabled')
        self.addButton(text="Michael, Pam, and Kelly", row=12, column=0, state='disabled')
        self.addButton(text="Jim, Dwight, and Michael", row=11, column=2, state='disabled')
        self.addButton(text="Kelly, Pam, and Stanley", row=12, column=2, state='disabled')



        self.questAnswered = self.questAnswered + 1 #adds one to the amount of questions the user has answered
        self.points = self.points + 1 #adds one to the amount of questions the user has answered correctly

        # if there is an error or the user hasn't restarted the game correctly there will be to many questions answered
        # and the user will be asked to restart the game again
        if self.questAnswered>=7:
            self.label2["text"] = "Number of answers given are invalid, click 'New Game' at the bottom right of the " \
                                  "screen"

        # else the program will tell the user they have gotten the question correct and how many points they've
        # gotten in total
        else:
            self.label2['text']="correct, total points: "+ str(self.points)

    # when the right answer to the third question is clicked
    def right3(self):
        # disables the buttons so the user can't change their answer
        self.addButton(text="Pam", row=16, column=0, state='disabled')
        self.addButton(text="Kelly", row=16, column=2, state='disabled')
        self.addButton(text="Jim", row=17, column=0, state='disabled')
        self.addButton(text="Ryan", row=17, column=2, state='disabled')

        self.questAnswered = self.questAnswered + 1 #adds one to the amount of questions the user has answered
        self.points = self.points + 1 #adds one to the amount of questions the user has answered correctly

        # if there is an error or the user hasn't restarted the game correctly there will be to many questions answered
        # and the user will be asked to restart the game again
        if self.questAnswered >= 7:
            self.label3["text"] = "Number of answers given are invalid, click 'New Game' at the bottom right of " \
                                  "the screen"

        # else the program will tell the user they have gotten the question correct and how many points they've
        # gotten in total
        else:
            self.label3['text'] = "correct, total points: " + str(self.points)



    # when the right answer to the fourth question is clicked
    def right4(self):
        # disables the buttons so the user can't change their answer
        self.addButton(text="They match the carpet", row=22, column=0, state='disabled')
        self.addButton(text="They're Kelly's favorite colors", row=21, column=0, state='disabled')
        self.addButton(text="They're Dwight's favorite colors", row=21, column=2, state='disabled')
        self.addButton(text="The colors symbolize wisdom", row=22, column=2, state='disabled')

        self.questAnswered = self.questAnswered + 1 #adds one to the amount of questions the user has answered
        self.points = self.points + 1 #adds one to the amount of questions the user has answered correctly

        # if there is an error or the user hasn't restarted the game correctly there will be to many questions answered
        # and the user will be asked to restart the game again
        if self.questAnswered >= 7:
            self.label4["text"] = "Number of answers given are invalid, click 'New Game' at the bottom right of " \
                                  "the screen"

        # else the program will tell the user they have gotten the question correct and how many points they've
        # gotten in total
        else:
            self.label4['text'] = "correct, total points: " + str(self.points)



    # when the right answer to the fifth question is clicked
    def right5(self):
        # disables the buttons so the user can't change their answer
        self.addButton(text="Gary", row=26, column=0, state='disabled')
        self.addButton(text="James", row=27, column=0, state='disabled')
        self.addButton(text="Kurt", row=26, column=2, state='disabled')
        self.addButton(text="Larry", row=27, column=2, state='disabled')

        self.questAnswered = self.questAnswered + 1 #adds one to the amount of questions the user has answered
        self.points = self.points + 1 #adds one to the amount of questions the user has answered correctly

        # if there is an error or the user hasn't restarted the game correctly there will be to many questions answered
        # and the user will be asked to restart the game again
        if self.questAnswered >= 7:
            self.label5["text"] = "Number of answers given are invalid, click 'New Game' at the bottom right of" \
                                  " the screen"

        # else the program will tell the user they have gotten the question correct and how many points they've
        # gotten in total
        else:
            self.label5['text'] = "correct, total points: " + str(self.points)


    # when the right answer to the sixth question is clicked
    def right6(self):
        # disables the buttons so the user can't change their answer
        self.addButton(text="customers", row=31, column=0, state='disabled')
        self.addButton(text="meatballs", row=31, column=2, state='disabled')
        self.addButton(text="pens", row=32, column=0, state='disabled')
        self.addButton(text="eggs", row=32, column=2, state='disabled')

        self.questAnswered = self.questAnswered + 1 #adds one to the amount of questions the user has answered
        self.points = self.points + 1 #adds one to the amount of questions the user has answered correctly

        # if there is an error or the user hasn't restarted the game correctly there will be to many questions answered
        # and the user will be asked to restart the game again
        if self.questAnswered >= 7:
            self.label6["text"] = "Number of answers given are invalid, click 'New Game' at the bottom right of the" \
                                  " screen"

        # else the program will tell the user they have gotten the question correct and how many points they've
        # gotten in total
        else:
            self.label6['text'] = "correct, total points: " + str(self.points)


    # when the right answer to the seventh question is clicked
    def right7(self):
        # disables the buttons so the user can't change their answer
        self.addButton(text="Jim", row=36, column=0, state='disabled')
        self.addButton(text="Dan", row=37, column=0, state='disabled')
        self.addButton(text="Tim", row=36, column=2, state='disabled')
        self.addButton(text="Brad", row=37, column=2, state='disabled')

        self.questAnswered = self.questAnswered + 1#adds one to the amount of questions the user has answered
        self.points = self.points + 1#adds one to the amount of questions the user has answered correctly

        # if there is an error or the user hasn't restarted the game correctly there will be to many questions answered
        # and the user will be asked to restart the game again
        if self.questAnswered > 7:
            self.label7["text"] = "Click 'New Game' at the bottom right of the screen"

        # else the program will tell the user they have gotten the question correct and how many points they've
        # gotten in total
        else:
            self.label7['text'] = "correct, total points: " + str(self.points) + ".  Click 'Calculate' to get score"




    #commands for all of the wrong answers clicked

    def wrong1(self):
        self.questAnswered=self.questAnswered+1 #adds 1 to questAnswered
        self.wrongPoints=self.wrongPoints+1 #adds 1 to wrongPoints

        #tells the user they've gotten the question wrong
        self.label1['text']='wrong answer, continue onto the next questions'

        #disables buttons
        self.addButton(text="Chili", row=6, column=2, state='disabled')
        self.addButton(text="M&Ms", row=6, column=0, state='disabled')
        self.addButton(text="Soup", row=5, column=2, state='disabled')
        self.addButton(text="Broccoli", row=5, column=0, state='disabled')


    def wrong2(self):
        self.questAnswered=self.questAnswered+1 #adds 1 to questAnswered
        self.wrongPoints=self.wrongPoints+1 #adds 1 to wrongPoints

        # tells the user they've gotten the question wrong
        self.label2['text']='wrong answer, continue onto the next questions'

        # disables buttons
        self.addButton(text="Pam, Angela, and Phylis", row=11, column=0, state='disabled')
        self.addButton(text="Michael, Pam, and Kelly", row=12, column=0, state='disabled')
        self.addButton(text="Jim, Dwight, and Michael", row=11, column=2, state='disabled')
        self.addButton(text="Kelly, Pam, and Stanley", row=12, column=2, state='disabled')


    def wrong3(self):
        self.questAnswered=self.questAnswered+1 #adds 1 to questAnswered
        self.wrongPoints=self.wrongPoints+1 #adds 1 to wrongPoints

        # tells the user they've gotten the question wrong
        self.label3['text']='wrong answer, continue onto the next questions'

        # disables buttons
        self.addButton(text="Pam", row=16, column=0, state='disabled')
        self.addButton(text="Kelly", row=16, column=2, state='disabled')
        self.addButton(text="Jim", row=17, column=0, state='disabled')
        self.addButton(text="Ryan", row=17, column=2, state='disabled')



    def wrong4(self):
        self.questAnswered=self.questAnswered+1 #adds 1 to questAnswered
        self.wrongPoints=self.wrongPoints+1 #adds 1 to wrongPoints

        # tells the user they've gotten the question wrong
        self.label4['text']='wrong answer, continue onto the next questions'

        # disables buttons
        self.addButton(text="They match the carpet", row=22, column=0, state='disabled')
        self.addButton(text="They're Kelly's favorite colors", row=21, column=0, state='disabled')
        self.addButton(text="They're Dwight's favorite colors", row=21, column=2, state='disabled')
        self.addButton(text="The colors symbolize wisdom", row=22, column=2, state='disabled')


    def wrong5(self):

        self.questAnswered=self.questAnswered+1 #adds 1 to questAnswered
        self.wrongPoints=self.wrongPoints+1#adds 1 to wrongPoints

        # tells the user they've gotten the question wrong
        self.label5['text']='wrong answer, continue onto the next questions'

        # disables buttons
        self.addButton(text="Gary", row=26, column=0, state='disabled')
        self.addButton(text="James", row=27, column=0, state='disabled')
        self.addButton(text="Kurt", row=26, column=2, state='disabled')
        self.addButton(text="Larry", row=27, column=2, state='disabled')


    def wrong6(self):
        self.questAnswered=self.questAnswered+1 #adds 1 to questAnswered
        self.wrongPoints=self.wrongPoints+1 #adds 1 to wrongPoints

        # tells the user they've gotten the question wrong
        self.label6['text']='wrong answer, continue onto the next questions'

        # disables buttons
        self.addButton(text="customers", row=31, column=0, state='disabled')
        self.addButton(text="meatballs", row=31, column=2, state='disabled')
        self.addButton(text="pens", row=32, column=0, state='disabled')
        self.addButton(text="eggs", row=32, column=2, state='disabled')


    def wrong7(self):
        self.questAnswered=self.questAnswered+1 #adds 1 to questAnswered
        self.wrongPoints=self.wrongPoints+1 #adds 1 to wrongPoints

        # tells the user they've gotten the question wrong
        self.label7['text']="wrong answer, click 'Calculate' to get score"

        # disables buttons
        self.addButton(text="Jim", row=36, column=0, state='disabled')
        self.addButton(text="Dan", row=37, column=0, state='disabled')
        self.addButton(text="Tim", row=36, column=2, state='disabled')
        self.addButton(text="Brad", row=37, column=2, state='disabled')



    def newGame(self):
        #resetting all variables
        self.questAnswered=0
        self.wrongPoints=0
        self.points=0

        #resetting labels
        self.label1['text']=""
        self.label2['text'] = ""
        self.label3['text']=""
        self.label4['text'] = ""
        self.label5['text'] = ""
        self.label6['text'] = ""
        self.label7['text'] = ""

        self.labelFinal= self.addLabel(text="                                                       "
                                       "                                               ", row=10, column=4)
        self.labelFinal['background']='white'


        #question 1 reset
        self.addButton(text="Chili", row=6, column=2, command=self.right1, state='normal')
        self.addButton(text="M&Ms", row=6, column=0, command=self.wrong1, state='normal')
        self.addButton(text="Soup", row=5, column=2, command=self.wrong1, state='normal')
        self.addButton(text="Broccoli", row=5, column=0, command=self.wrong1, state='normal')

        #question 2 reset
        self.addButton(text="Pam, Angela, and Phylis", row=11, column=0, command=self.right2, state='normal')
        self.addButton(text="Michael, Pam, and Kelly", row=12, column=0, command=self.wrong2, state='normal')
        self.addButton(text="Jim, Dwight, and Michael", row=11, column=2, command=self.wrong2, state='normal')
        self.addButton(text="Kelly, Pam, and Stanley", row=12, column=2, command=self.wrong2, state='normal')

        #question 3 reset
        self.addButton(text="Pam", row=16, column=0, command=self.wrong3, state='normal')
        self.addButton(text="Kelly", row=16, column=2, command=self.right3, state='normal')
        self.addButton(text="Jim", row=17, column=0, command=self.wrong3, state='normal')
        self.addButton(text="Ryan", row=17, column=2, command=self.wrong3, state='normal')


        #question 4 reset
        self.addButton(text="They match the carpet", row=22, column=0, command=self.right4, state='normal')
        self.addButton(text="They're Kelly's favorite colors", row=21, column=0, command=self.wrong4, state='normal')
        self.addButton(text="They're Dwight's favorite colors", row=21, column=2, command=self.wrong4, state='normal')
        self.addButton(text="The colors symbolize wisdom", row=22, column=2, command=self.wrong4, state='normal')

        #question 5 reset
        self.addButton(text="Gary", row=26, column=0, command=self.right5, state='normal')
        self.addButton(text="James", row=27, column=0, command=self.wrong5, state='normal')
        self.addButton(text="Kurt", row=26, column=2, command=self.wrong5, state='normal')
        self.addButton(text="Larry", row=27, column=2, command=self.wrong5, state='normal')

        #question 6 reset
        self.addButton(text="customers", row=31, column=0, command=self.wrong6, state='normal')
        self.addButton(text="meatballs", row=31, column=2, command=self.right6, state='normal')
        self.addButton(text="pens", row=32, column=0, command=self.wrong6, state='normal')
        self.addButton(text="eggs", row=32, column=2, command=self.wrong6, state='normal')

        #question 7 reset
        self.addButton(text="Jim", row=36, column=0, command=self.wrong7, state='normal')
        self.addButton(text="Dan", row=37, column=0, command=self.right7, state='normal')
        self.addButton(text="Tim", row=36, column=2, command=self.wrong7, state='normal')
        self.addButton(text="Brad", row=37, column=2, command=self.wrong7, state='normal')





    #command when the user clicks the 'Calculate' button
    def calc(self):
        self.finalScore = self.points / self.questAnswered

        #if user got 1/7 questions right
        if self.finalScore==1/7:
            self.addLabel(text="1/7 questions answered correctly         ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            #window will pop up with corresponding image
            global my_img1
            top = Toplevel()
            top.title("1/7: have you even watched the office?")
            my_img1 = ImageTk.PhotoImage(Image.open(r'angela.gif'))
            Label(top, image=my_img1).pack()

        # if user got 2/7 questions right
        elif self.finalScore==(2/7):
            self.addLabel(text="2/7 questions answered correctly          ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            # window will pop up with corresponding image
            global my_img2
            top = Toplevel()
            top.title("2/7: time for a recharge")
            my_img2 = ImageTk.PhotoImage(Image.open(r'kelly.gif'))
            Label(top, image=my_img2).pack()

        # if user got 3/7 questions right
        elif self.finalScore==(3/7):
            self.addLabel(text="3/7 questions answered correctly           ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            # window will pop up with corresponding image
            global my_img3
            top = Toplevel()
            top.title("3/7: in need of a rewatch?")
            my_img3 = ImageTk.PhotoImage(Image.open(r'hollyflax.gif'))
            Label(top, image=my_img3).pack()

        # if user got 4/7 questions right
        elif self.finalScore==(4/7):
            self.addLabel(text="4/7 questions answered correctly           ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            # window will pop up with corresponding image
            global my_img4
            top = Toplevel()
            top.title("4/7: 'you're right, its not my best'")
            my_img4 = ImageTk.PhotoImage(Image.open(r'jimdis.gif'))
            Label(top, image=my_img4).pack()

        # if user got 5/7 questions right
        elif self.finalScore==(5/7):
            self.addLabel(text="5/7 questions answered correctly           ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            # window will pop up with corresponding image
            global my_img5
            top = Toplevel()
            top.title("5/7: very close")
            my_img5 = ImageTk.PhotoImage(Image.open(r'6out7.gif'))
            Label(top, image=my_img5).pack()

        # if user got 6/7 questions right
        elif self.finalScore==(6/7):
            self.addLabel(text="6/7 questions answered correctly           ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            # window will pop up with corresponding image
            global my_img6
            top = Toplevel()
            top.title("6/7: 'the only time I set the bar low is for limbo'")
            my_img6 = ImageTk.PhotoImage(Image.open(r'limbo.gif'))
            Label(top, image=my_img6).pack()


        # if user got 7/7 questions right
        elif self.finalScore==(7/7):
            self.addLabel(text="7/7 questions answered correctly           ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            # window will pop up with corresponding image
            global my_img7
            top = Toplevel()
            top.title("7/7: 'I feel God in this Chili's tonight'")
            my_img7 = ImageTk.PhotoImage(Image.open(r'pamwins.gif'))
            Label(top, image=my_img7).pack()


        # if user got 0 questions right
        #making sure that all questions were answered 
        elif self.finalScore==0 and self.questAnswered==7:
            self.addLabel(text="0 questions answered correctly           ", row=10, column=4, background=None,
                          font=('American Typewriter', 16))

            # window will pop up with corresponding image
            global my_img0
            top = Toplevel()
            top.title("shame")
            my_img0 = ImageTk.PhotoImage(Image.open(r'zeroscore.gif'))
            Label(top, image=my_img0).pack()

        #makes sure the user answers all the questions before calculating score
        else:
            self.addLabel(text="answer all the questions before calculating score", row=10, column=4, background=None,
                          font=('American Typewriter', 15))




    #command when the user clicks the exit button, which closes the windows the user has up
    def Exit(self):
        exit(0)


def main():
    office().mainloop()

if __name__ == '__main__': #allows the code to run
    main()

