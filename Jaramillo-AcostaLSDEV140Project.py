"""
Program: Jaramillo-AcostaLSDEV140Project.py
Author: Leslie Jaramillo-Acosta
Last date modified: July 17th, 2023
Purpose: The office Trivia using a GUI
"""



from tkinter import *
import tkinter as tk
import tkinter.messagebox



class office:
    def __init__(self, main):
        self.main = main
        self.main.title ('how well do you know the office?') #making the title of the window
        main.geometry("%sx%s+%s+%s" % (800, 800, 800, 800))

        #question 1
        tk.Label(self.main, text="1) What did Kevin spill on the carpet?", justify="left").grid(row=4,column=0)
        Button(self.main, text="Chili", justify="left").grid(row=5)
        Button(self.main, text="M&Ms", justify="left").grid(row=6)
        Button(self.main, text="Soup", justify="left").grid(row=5, column=2)
        Button(self.main, text="Broccoli").grid(row=6, column=2)


        self.label1 = tk.Label(self.main, text=" ")  # makes the space where the answer will appear
        self.label1.grid(row=7, column=0)  # places the label

        #question 2
        tk.Label(self.main, text="2) Who were the original members of the PPC?", justify="left").grid(row=10, column=0)
        Button(self.main, text="Pam, Angela, and Phylis", justify="left").grid(row=11)
        Button(self.main, text="Michael, Pam, and Kelly", justify="left").grid(row=12)
        Button(self.main, text="Jim, Dwight, and Michael", justify="left").grid(row=11, column=2)
        Button(self.main, text="Kelly, Pam, and Stanley").grid(row=12, column=2)

        self.label2 = tk.Label(self.main, text=" ")  # makes the space where the answer will appear
        self.label2.grid(row=13, column=0)  # places the label

        #question 3
        tk.Label(self.main, text="3) Who came up with WUPHF.com?",justify="left").grid(row=15, column=0)
        Button(self.main, text="Pam", justify="left").grid(row=16)
        Button(self.main, text="Kelly", justify="left").grid(row=17)
        Button(self.main, text="Jim", justify="left").grid(row=16, column=2)
        Button(self.main, text="Ryan").grid(row=17, column=2)

        self.label3 = tk.Label(self.main, text=" ")  # makes the space where the answer will appear
        self.label3.grid(row=18, column=0)  # places the label

        # question 4
        tk.Label(self.main, text="4) Why does Dwight use brown and grey balloons for Kelly's birthday party?", justify="left").grid(row=20, column=0)
        Button(self.main, text="They match the carpet", justify="left").grid(row=21)
        Button(self.main, text="They're Kelly's favorite colors", justify="left").grid(row=22)
        Button(self.main, text="They're Dwight's favorite colors", justify="left").grid(row=21, column=2)
        Button(self.main, text="The colors symbolize wisdom").grid(row=22, column=2)

        self.label4 = tk.Label(self.main, text=" ")  # makes the space where the answer will appear
        self.label4.grid(row=23, column=0)  # places the label

        # question 5
        tk.Label(self.main, text="5) What is Michael's middle name?",
                 justify="left").grid(row=25, column=0)
        Button(self.main, text="Gary", justify="left").grid(row=26)
        Button(self.main, text="James", justify="left").grid(row=27)
        Button(self.main, text="Kurt", justify="left").grid(row=26, column=2)
        Button(self.main, text="Larry").grid(row=27, column=2)

        self.label5 = tk.Label(self.main, text=" ")  # makes the space where the answer will appear
        self.label5.grid(row=28, column=0)  # places the label

        # question 6
        tk.Label(self.main, text="6) What do Stanley and Dwight gain from Jim's prank?",
                 justify="left").grid(row=30, column=0)
        Button(self.main, text="customers", justify="left").grid(row=31)
        Button(self.main, text="meatballs", justify="left").grid(row=32)
        Button(self.main, text="pens", justify="left").grid(row=31, column=2)
        Button(self.main, text="eggs").grid(row=32, column=2)

        self.label6 = tk.Label(self.main, text=" ")  # makes the space where the answer will appear
        self.label6.grid(row=33, column=0)  # places the label

        # question 7
        tk.Label(self.main, text="7) What is Karen's Husband's name??",
                 justify="left").grid(row=35, column=0)
        Button(self.main, text="Jim", justify="left").grid(row=36)
        Button(self.main, text="Dan", justify="left").grid(row=37)
        Button(self.main, text="Tim", justify="left").grid(row=36, column=2)
        Button(self.main, text="Brad").grid(row=37, column=2)

        self.label7 = tk.Label(self.main, text=" ")  # makes the space where the answer will appear
        self.label7.grid(row=38, column=0)  # places the label

    #def right(self): #command isnt working
        #if 0 == 0:
            #self.label1['text'] = "correct answer"




if __name__ == '__main__': #allows the code to run
    main = Tk()
    application = office(main)
    main.mainloop()
