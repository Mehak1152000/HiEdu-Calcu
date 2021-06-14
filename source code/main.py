from tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox
import math as m
import pyttsx3

# some useful variable
font = ('Arial', 22, 'bold')

# important functions
def talk():
    engine = pyttsx3.init()
    v = engine.getProperty('voices')
    engine.setProperty('voice',v[1].id)
    ex = textField.get()
    ex = ex[len(ex)-1]
    engine.say(ex)
    engine.runAndWait()

def all_clear():
    textField.delete(0, END)
    engine = pyttsx3.init()
    v = engine.getProperty('voices')
    engine.setProperty('voice',v[1].id)
    engine.say("clear")
    engine.runAndWait()

def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0, END)
    textField.insert(0, ex)
    engine = pyttsx3.init()
    v = engine.getProperty('voices')
    engine.setProperty('voice',v[1].id)
    engine.say("clear last digit")
    engine.runAndWait()

def click_btn_function(event):
    print("button clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
            engine = pyttsx3.init()
            v = engine.getProperty('voices')
            engine.setProperty('voice',v[1].id)
            engine.say("equals to")
            ans = textField.get()
            engine.say(ans)
            engine.runAndWait()
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    if text == 'x':
        textField.insert(END, "*")
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("multiply")
        engine.runAndWait()
        return

    if text == "-":
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("minus")
        engine.runAndWait()

    if text == ".":
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("point")
        engine.runAndWait()

    textField.insert(END, text)


# creating a window
window = Tk()
window.title('HiEdu Calcu')
window.configure(background="powder blue")

app_width=475
app_height=490
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


heading = Label(text="HiEdu Calcu",font=font,fg="blue",bg="powder blue")
heading.pack(side=TOP,pady=10)

# textfield
textField =Entry(window,font=font,justify=RIGHT,borderwidth = 15)
textField.pack(side=TOP,pady=10,fill=X)

# buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)


# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5,command=talk,
                     activebackground='red', activeforeground='white')
        btn.grid(row=i, column=j, padx=3, pady=3)
        temp = temp+1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text="0", font=font, width=5,command=talk,
                 activebackground='red', activeforeground='white')
zeroBtn.grid(row=3, column=0, padx=3, pady=3)

dotBtn = Button(buttonFrame, text=".", font=font, width=5,command=talk,
                activebackground='red', activeforeground='white')
dotBtn.grid(row=3, column=1, padx=3, pady=3)

equalBtn = Button(buttonFrame, text="=", font=font, width=5,bg="powder blue",
                  activebackground='red', activeforeground='white')
equalBtn.grid(row=3, column=2, padx=3, pady=3)

plusBtn = Button(buttonFrame, text="+", font=font, width=5,bg="powder blue",command=talk,
                 activebackground='red', activeforeground='white')
plusBtn.grid(row=0, column=3, padx=3, pady=3)

minusBtn = Button(buttonFrame, text="-", font=font, width=5,bg="powder blue",
                  activebackground='red', activeforeground='white')
minusBtn.grid(row=1, column=3, padx=3, pady=3)

multBtn = Button(buttonFrame, text="x", font=font, width=5,bg="powder blue",
                 activebackground='red', activeforeground='white')
multBtn.grid(row=2, column=3, padx=3, pady=3)

divideBtn = Button(buttonFrame, text=chr(247), font=font, width=5,bg="powder blue",command=talk,
                   activebackground='red', activeforeground='white')
divideBtn.grid(row=3, column=3, padx=3, pady=3)

clearBtn = Button(buttonFrame, text="CE", font=font, width=11,bg="powder blue",
                  activebackground='red', activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

allClearBtn = Button(buttonFrame, text="C", font=font, width=11,bg="powder blue",
                     activebackground='red', activeforeground='white', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2, padx=3, pady=3)

# binding all buttons
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)

# adding some scientific calculator features
scFrame = Frame(window) 

sqrtBtn = Button(scFrame, text="√", font=font, width=5,bg="powder blue",
                 activebackground='red', activeforeground='white')
sqrtBtn.grid(row=0, column=0, padx=3, pady=3)

powBtn = Button(scFrame, text="^", font=font, width=5,bg="powder blue",
                activebackground='red', activeforeground='white')
powBtn.grid(row=0, column=1, padx=3, pady=3)

factBtn = Button(scFrame, text="x!", font=font, width=5,bg="powder blue",
                 activebackground='red', activeforeground='white')
factBtn.grid(row=0, column=2, padx=3, pady=3)

radBtn = Button(scFrame, text="toRad", font=font, width=5,bg="powder blue",
                activebackground='red', activeforeground='white')
radBtn.grid(row=0, column=3, padx=3, pady=3)

degBtn = Button(scFrame, text="toDeg", font=font, width=5,bg="powder blue",
                activebackground='red', activeforeground='white')
degBtn.grid(row=1, column=0, padx=3, pady=3)

sinBtn = Button(scFrame, text="sinΘ", font=font, width=5,bg="powder blue",
                activebackground='red', activeforeground='white')
sinBtn.grid(row=1, column=1, padx=3, pady=3)

cosBtn = Button(scFrame, text="cosΘ", font=font, width=5,bg="powder blue",
                activebackground='red', activeforeground='white')
cosBtn.grid(row=1, column=2, padx=3, pady=3)

tanBtn = Button(scFrame, text="tanΘ", font=font, width=5,bg="powder blue",
                activebackground='red', activeforeground='white')
tanBtn.grid(row=1, column=3, padx=3, pady=3)

# variable to check in which calculator we are
normalcalc = True

# scientific calculator functions

def calculator_sc(event):
    print("button click")
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print('cal degree')
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("radian equals to")
        ans = float(str(m.degrees(float(ex))))
        answer=round(ans,2)
        engine.say(answer)
        engine.say("degree")
        engine.runAndWait()

    elif text == 'toRad':
        print('radian')
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("degree equals to")
        ans = float(str(m.radians(float(ex))))
        answer=round(ans,2)
        engine.say(answer)
        engine.say("radian")
        engine.runAndWait()

    elif text == '^':
        print('cal power')
        base, power = ex.split(' ')
        print('base = ', base, 'power = ', power)
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        ex = textField.get()
        ex1 = ex[0]
        ex2 = ex[len(ex)-1]
        engine.say(ex1)
        engine.say("power")
        engine.say(ex2)
        answer = m.pow(int(base), int(power))
        engine.say("equals to")
        engine.say(answer)
        engine.runAndWait()

    elif text == '√':
        print('cal sqrt')
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("is square root of")
        ans = float(m.sqrt(int(ex)))
        answer=round(ans,2)
        engine.say(answer)
        engine.runAndWait()

    elif text == 'x!':
        print('cal factorial')
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("factorial")
        engine.say("equals to")
        answer = str(m.factorial(int(ex)))
        engine.say(answer)
        engine.runAndWait()

    elif text == 'sinΘ':
        print('cal sinΘ')
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("sin theta")
        engine.say("equals to")
        ans = float(str(m.sin(m.radians(int(ex)))))
        answer=round(ans,2)
        engine.say(answer)
        engine.runAndWait()

    elif text == 'cosΘ':
        print('cal cosΘ')
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("cos theta")
        engine.say("equals to")
        ans = float(str(m.cos(m.radians(int(ex)))))
        answer=round(ans,2)
        engine.say(answer)
        engine.runAndWait()

    elif text == 'tanΘ':
        print('cal tanΘ')
        engine = pyttsx3.init()
        v = engine.getProperty('voices')
        engine.setProperty('voice',v[1].id)
        engine.say("tan theta")
        engine.say("equals to")
        ans = float(str(m.tan(m.radians(int(ex)))))
        answer=round(ans,2)
        engine.say(answer)
        engine.runAndWait()

    textField.delete(0, END)
    textField.insert(0, answer)


def sc_click():
    global normalcalc
    print("scientific calculator clicked")
    if normalcalc:
        buttonFrame.pack_forget()
        # add scFrame
        scFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        app_width=475
        app_height=620
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)
        window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        print("show scientific calculator")
        normalcalc = False
    else:
        print("show normal calculator")
        scFrame.pack_forget()
        app_width=475
        app_height=490
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)
        window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        normalcalc = True


# binding buttons
sqrtBtn.bind("<Button-1>", calculator_sc)
powBtn.bind("<Button-1>", calculator_sc)
factBtn.bind("<Button-1>", calculator_sc)
radBtn.bind("<Button-1>", calculator_sc)
degBtn.bind("<Button-1>", calculator_sc)
sinBtn.bind("<Button-1>", calculator_sc)
cosBtn.bind("<Button-1>", calculator_sc)
tanBtn.bind("<Button-1>", calculator_sc)

def iExit() :
    iExit = tkinter.messagebox.askyesno("HiEdu Calcu","Confirm if you want to exit")
    if iExit>0 :
        window.destroy()
        return

# mode label
fontMenu = ('', 10)
menubar = Menu(window)

mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)
mode.add_separator()
mode.add_command(label="Exit",command=iExit)
menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)

window.mainloop()