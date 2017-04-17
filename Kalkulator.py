from tkinter import *

root = Tk()
frame = Frame(root)
display = Entry(root, width=1, justify="right", bg="white", font = ("Arial", 20), borderwidth=0)
root.resizable(0, 0)

class Kalkulator:

    def __init__(self):
        root.title("Kalkulator")
        root.geometry("265x310")
        display.insert(0, "0")
        self.spr1 = ""
        self.spr2 = ""
        self.operacija = 0
        self.trenutno = 0
        self.konec = 0

    def število(self, vpis):
        if self.trenutno is 0:
            self.spr1 = str(vpis)
            display.delete(0, END)
            display.insert(0, self.spr1)
        else:
            self.spr2 = str(vpis)
            display.delete(0, END)
            display.insert(0, self.spr2)

    def določanje(self, rac):
        self.operacija = rac
        if self.trenutno is 0:
            self.trenutno = self.trenutno+1
        display.delete(0, END)
        
        if self.operacija is plus:
            display.insert(0, "+")
        elif self.operacija is minus:
            display.insert(0, "-")
        elif self.operacija is krat:
            display.insert(0, "*")
        elif self.operacija is deljeno:
            display.insert(0, "/")

    def opr(self):
        if self.operacija is plus:
            self.konec = float(self.spr1) + float(self.spr2)
        elif self.operacija is minus:
            self.konec = float(self.spr1) - float(self.spr2)
        elif self.operacija is krat:
            self.konec = float(self.spr1) * float(self.spr2)
        elif self.operacija is deljeno:
            self.konec = float(self.spr1) / float(self.spr2)
        if self.konec == int(self.konec):
            self.konec = int(self.konec)
            
        display.delete(0, END)
        display.insert(0, self.konec)

    def clear(self):
        display.delete(0, END)
        self.__init__()
            

c = Kalkulator()

display.grid(row=1, column=0, columnspan=5, sticky="NWNESWSE")

g0 = Button(root, text="0", command=lambda: c.število(0),padx=16, pady=16, font=15)
g0.grid(row=5, column=0)

g1 = Button(root, text="1",command=lambda: c.število(1),padx=16, pady=16, font=15)
g1.grid(row=4, column=0)

g2 = Button(root, text="2",command=lambda: c.število(2),padx=16, pady=16, font=15)
g2.grid(row=4, column=1)

g3 = Button(root, text="3",command=lambda: c.število(3),padx=16, pady=16, font=15)
g3.grid(row=4, column=2)

g4 = Button(root, text="4",command=lambda: c.število(4),padx=16, pady=16, font=15)
g4.grid(row=3, column=0)

g5 = Button(root, text="5",command=lambda: c.število(5),padx=16, pady=16, font=15)
g5.grid(row=3, column=1)

g6 = Button(root, text="6",command=lambda: c.število(6),padx=16, pady=16, font=15)
g6.grid(row=3, column=2)

g7 = Button(root, text="7",command=lambda: c.število(7),padx=16, pady=16, font=15)
g7.grid(row=2, column=0)

g8 = Button(root, text="8",command=lambda: c.število(8),padx=16, pady=16, font=15)
g8.grid(row=2, column=1)

g9 = Button(root, text="9",command=lambda: c.število(9),padx=16, pady=16, font=15)
g9.grid(row=2, column=2)

cela = Button(root, text=".",command=lambda: c.število("."),padx=18, pady=16, font=15)
cela.grid(row=5, column=1)


plus = Button(root, text="+",command=lambda: c.določanje(plus),padx=14.5, pady=16, font=15)
plus.grid(row=2, column=3)

minus = Button(root, text="-",command=lambda: c.določanje(minus),padx=17, pady=16, font=15)
minus.grid(row=3, column=3)

krat = Button(root, text="*",command=lambda: c.določanje(krat),padx=16, pady=16, font=15)
krat.grid(row=4, column=3)

deljeno = Button(root, text="/",command=lambda: c.določanje(deljeno),padx=16, pady=16, font=15)
deljeno.grid(row=5, column=3)


je = Button(root, text="=",command=c.opr,padx=16, pady=16, font=15)
je.grid(row=1, column=5)

clear = Button(root, text="C",command=c.clear,padx=15, pady=16, font=15)
clear.grid(row=5, column=2)


root.mainloop()
