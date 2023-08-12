from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import pyautogui as pag

import datetime

class CalculatorAPP:

    def __init__(self):

        self.CalcWind = Tk()
        self.CalcWind.geometry("460x510+800+100")
        self.CalcWind.title("PS Calculator")
        self.CalcWind.resizable(0, 0)
        self.CalcWind.iconbitmap('logo.ico')

        self.calcVal = tk.StringVar()
        self.calcTmpVal = ''

        self.outputEntry = Entry(self.CalcWind, width=50, justify="right", font=("Arial", 20), textvariable=self.calcVal)
        self.outputEntry.pack(ipady=10)

        self.FrameOne = tk.Frame(self.CalcWind)
        self.FrameOne.pack(ipady=10)

        self.btnOne = Button(self.FrameOne, text='(', width=8, command=lambda:self.showVal('('))
        self.btnOne.pack(side="left", padx=10, ipady=10)

        self.btnTwo = Button(self.FrameOne, text=')', width=8, command=lambda:self.showVal(')'))
        self.btnTwo.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameOne, text='%', width=8, command=lambda:self.showVal('%'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameOne, text='AC', width=20, command=self.clearVal)
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.FrameTwo = tk.Frame(self.CalcWind)
        self.FrameTwo.pack(ipady=10)

        self.btnOne = Button(self.FrameTwo, text='9', width=8, command=lambda:self.showVal('9'))
        self.btnOne.pack(side="left", padx=10, ipady=10)

        self.btnTwo = Button(self.FrameTwo, text='8', width=8, command=lambda:self.showVal('8'))
        self.btnTwo.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameTwo, text='7', width=8, command=lambda:self.showVal('7'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameTwo, text='+', width=20, command=lambda:self.showVal('+'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.FrameThree = tk.Frame(self.CalcWind)
        self.FrameThree.pack(ipady=10)

        self.btnOne = Button(self.FrameThree, text='6', width=8, command=lambda:self.showVal('6'))
        self.btnOne.pack(side="left", padx=10, ipady=10)

        self.btnTwo = Button(self.FrameThree, text='5', width=8, command=lambda:self.showVal('5'))
        self.btnTwo.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameThree, text='4', width=8, command=lambda:self.showVal('4'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameThree, text='-', width=20, command=lambda:self.showVal('-'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.FrameFour = tk.Frame(self.CalcWind)
        self.FrameFour.pack(ipady=10)

        self.btnOne = Button(self.FrameFour, text='3', width=8, command=lambda:self.showVal('3'))
        self.btnOne.pack(side="left", padx=10, ipady=10)

        self.btnTwo = Button(self.FrameFour, text='2', width=8, command=lambda:self.showVal('2'))
        self.btnTwo.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameFour, text='1', width=8, command=lambda:self.showVal('1'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameFour, text='/', width=20, command=lambda:self.showVal('/'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.FrameFive = tk.Frame(self.CalcWind)
        self.FrameFive.pack(ipady=10)

        self.btnOne = Button(self.FrameFive, text='0', width=8, command=lambda:self.showVal('0'))
        self.btnOne.pack(side="left", padx=10, ipady=10)

        self.btnTwo = Button(self.FrameFive, text='.', width=8, command=lambda:self.showVal('.'))
        self.btnTwo.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameFive, text='*', width=8, command=lambda:self.showVal('*'))
        self.btnThree.pack(side="left", padx=10, ipady=10)

        self.btnThree = Button(self.FrameFive, text='=', width=20, command=self.getCalcVal)
        self.btnThree.pack(side="left", padx=10, ipady=10)

        chkCurrentYear = datetime.datetime.now().strftime("%Y")

        if int(chkCurrentYear) > 2023:
            cpyrightYear = "2023 - "+str(chkCurrentYear)
        else:
            cpyrightYear = "2023"

        self.authorLabel = Label(self.CalcWind, text='PS Thamizhan - © '+str(cpyrightYear)+'. V1.0', font=("Segoe UI", 7))
        self.authorLabel.pack(side=BOTTOM, ipady=20)

    def showVal(self, txtVal):
        self.calcTmpVal += txtVal
        self.calcVal.set(self.calcTmpVal)

    def clearVal(self):
        self.calcTmpVal = ''
        self.calcVal.set(self.calcTmpVal)

    def getCalcVal(self):
        try:
            if (len(self.calcTmpVal) > 0):
                res = eval(self.calcTmpVal)
                self.calcVal.set(res)
        except:
            self.calcTmpVal = ''
            self.calcVal.set('Error')

    def runModule(self):
        self.CalcWind.mainloop()

mod = CalculatorAPP()
mod.runModule()
