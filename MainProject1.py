import tkinter as tk
window=tk.Tk()
window.title("System")
window.geometry("1250x700") 
window.resizable(False,False)
window.configure(bg="grey")
from PIL import ImageTk,Image
from tkinter import ttk
import screen_brightness_control as sbc



##########layout_tkinter.TclError: couldn't recognize data in image file "im.jpg"
from tkinter import *
Lhs=Frame(window,width=300,height=680)
Lhs.place(x=10,y=10)
Rhs=Frame(window,width=300,height=680,bg="skyblue")
Rhs.place(x=940,y=10)
Centre=Frame(window,width=610,height=680,bg="lightgrey")
Centre.place(x=320,y=10)




######system details in Lhs frame
import platform
ms=platform.uname()
l1=Label(Lhs,text=f"{ms.node}",bg="#cccccc",font=("Bold",18)
         ,width=20,height=2)
l1.place(x=7,y=5)
l2=Label(Lhs,text=f"OS :{ms.system}",font=("Bold",18),bg="#cccccc"
         ,width=20,height=2)
l2.place(x=7,y=250)
l3=Label(Lhs,text=f"Machine :{ms.machine}",bg="#cccccc"
         ,font=("Bold",18),width=20,height=2)
l3.place(x=7,y=310)
l4=Label(Lhs,text=f"{ms.processor}",bg="#cccccc",width=40,height=4)
l4.place(x=7,y=370)




######RAM & CPU Details in Lhs Frame
import psutil
svmem=psutil.virtual_memory()
a=svmem.total-svmem.available
b=round(a/svmem.total*100)
c=svmem.total/(1024**3)
l5=Label(Lhs,text="Ram Usage :{}%".format(b),bg="#cccccc",
         font=("Bold",18),width=20,height=3)
l5.place(x=7,y=430)
l6=Label(Lhs,text="Ram Installed :%.2f"%c,font=("Bold",18)
         ,bg="#cccccc",width=20,height=3)
l6.place(x=7,y=510)
l7=Label(Lhs,text="CPU Usage :{}".format(psutil.cpu_percent(5))
         ,bg="#cccccc",font=("Bold",18),width=20,height=3)
l7.place(x=7,y=590)
image_icon4=PhotoImage(file="windowsys.png")
Body=Label(Lhs,image=image_icon4,width=270,height=170)
Body.place(x=15,y=70)



from PIL import ImageTk,Image
######battery Details
def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"%(hours,minutes,seconds)
battery=psutil.sensors_battery()
def bs():
    window2=tk.Tk()
    window2.title("Battery Settings")
    window2.geometry("350x280")
    window2.resizable(False,False)
    window2.configure(background="grey")
    l8=Label(window2,text="Battery Percentage :{}%".format(battery.percent)
             ,font=("Bold",17),fg="Black",bg="grey",width=25,height=3)
    l8.place(x=20,y=90)
    l9=Label(window2,text="Power plugged in :{}".format(battery.power_plugged),
             font=("Bold",17),fg="Black",bg="grey",width=25,height=3)
    l9.place(x=20,y=10)
    l10=Label(window2,text="Remaining Time :{}".format(convertTime(battery.secsleft)),
              font=("Bold",17),fg="Black",bg="grey",width=25,height=3)
    l10.place(x=20,y=170)
image_icon1=PhotoImage(file="img1b1.png")
button1=Button(Centre,image=image_icon1,width=260,height=250,command=bs)
button1.place(x=20,y=20)



#######screen Resolution
def resolute():
    window1=tk.Tk()
    window1.title("Display Settings")
    window1.geometry("400x300")
    window1.resizable(False,False)
    window1.configure(background="grey")
    rl1=Label(window1,text="Width :{}".format(screen_width)
              ,font=("Bold",25),bg="grey",width=20,height=5)
    rl1.place(x=10,y=10)
    rl2=Label(window1,text="Height :{}".format(screen_height)
              ,font=("Bold",25),bg="grey",width=20,height=5)
    rl2.place(x=10,y=120)
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
image_icon=PhotoImage(file="display-size1.png")
button2=Button(Centre,image=image_icon,
               width=280,height=230,command=resolute)
button2.place(x=310,y=30)



##
#######Brightness
####
##from tkinter import ttk
##import screen_brightness_control as sbc
##cv=tk.DoubleVar()
##def get_cv():
##    return'{:.2f}'.format(cv.get())
##def brightness_changed(event):
##    sbc.set_brightness(get_cv())
##l11=Label(Centre,text="Brightness",font=("Bold",16),
##          bg="#bababa",width=25,height=6)
##l11.place(x=20,y=300)
##brightness=ttk.Scale(Centre,from_=0,to=100,orient="horizontal"
##                     ,command=brightness_changed,variable=cv)
##brightness.place(x=120,y=410)
##label_100=Label(Centre,text="100%",font=("Bold",16),
##                bg="#bababa",fg="Black",width=4,height=1)
##label_100.place(x=230,y=410)
##label_zero=Label(Centre,text="0%",font=("Bold",16),
##                 bg="#bababa",fg="Black",width=4,height=1)
##label_zero.place(x=70,y=410)
##label_level=Label(Centre,text="{}%".format(sbc.get_brightness()),font=("Bold",16),
##                  bg="#bababa",fg="Black",width=4,height=1)
##label_level.place(x=150,y=320)



#####Speaker
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
l12=Label(Centre,text="Speaker",font=("Bold",16),
          bg="#bababa",width=25,height=6)
l12.place(x=280,y=490)
vv=tk.DoubleVar()
def get_cvv():
    return "{:.2f}".format(vv.get())
def vc(event):
    devices=AudioUtilities.GetSpeakers()
    interface=devices.Activate(IAudioEndpointVolume._iid_
                               ,CLSCTX_ALL,None)
    volume=cast(interface,POINTER(IAudioEndpointVolume))
    volume=volume.SetMasterVolumeLevel(-float(get_cvv()),None)

vol=ttk.Scale(Centre,from_=30,to=0,orient="horizontal",
               command=vc,variable=vv)
vol.place(x=380,y=600)
label1_100=Label(Centre,text="100%",font=("Bold",16),
                bg="#bababa",fg="Black",width=4,height=1)
label1_100.place(x=490,y=600)
label1_zero=Label(Centre,text="0%",font=("Bold",16),
                bg="#bababa",fg="Black",width=4,height=1)
label1_zero.place(x=330,y=600)




######Clock
from tkinter import *
from time import strftime
def time1():
    root=Tk()
    root.title("Clock")
    root.resizable(False,False)
    def time():
        string=strftime("%H : %M :%S %p")
        lbl.configure(text=string)
        lbl.after(1000,time)
    lbl=Label(root,font=("calibri",40,"bold")
              ,background="grey",foreground="black")
    lbl.pack(anchor="center")
    time()
image_icon6=PhotoImage(file="alarm-clock.png")
button3=Button(Centre,image=image_icon6,width=200,height=190,command=time1)
button3.place(x=30,y=475)




####day
from tkinter import *
from datetime import datetime as dt
def Day():
    window7=Tk()
    window7.title("Day")
    window7.configure(background="grey")
    now=dt.now()
    s=now.strftime("%A %m %y")
    l19=Label(window7,text="{}".format(s),font=("bold",25),width=20,height=10
              ,fg="black",bg="grey")
    l19.pack()
    window7.mainloop()
image_icon7=PhotoImage(file="7-2-calendar-png-picture-thumb.png")
button7=Button(Centre,image=image_icon7,width=200,height=190,command=Day)
button7.place(x=360,y=280)



####Calendar
from tkinter import *
from PIL import ImageTk,Image
import calendar
from datetime import date
def calendar1():
    def displaycalendar():
        month=int(month_box.get())
        year=int(year_box.get())
        output_calendar=calendar.month(year,month)
        calendar_field.delete(1.0,"end")
        calendar_field.insert("end",output_calendar)
    def reset():
        calendar_field.delete(1.0,"end")
        month_var.set(current_month)
        year_var.set(current_year)
        month_box.config(textvariable=month_var)
        year_box.config(textvariable=year_var)
    def close():
        guiwindow.destroy()
    if __name__=="__main__":
        guiwindow=Tk()
        guiwindow.title("Calender")
        guiwindow.geometry("500x550+650+250")
        guiwindow.configure(bg="#B0E0E6")
        guiwindow.resizable(False,False)
        header_frame=Frame(guiwindow,bg="#B0E0E6")
        entry_frame=Frame(guiwindow,bg="#B0E0E6")
        result_frame=Frame(guiwindow,bg="#B0E0E6")
        button_frame=Frame(guiwindow,bg="#B0E0E6")
        header_frame.pack(expand=True,fill="both")
        entry_frame.pack(expand=True,fill="both")
        result_frame.pack(expand=True,fill="both")
        button_frame.pack(expand=True,fill="both")
        header_label=Label(header_frame,text="Calendar",font=("verdana",25,"bold"),bg="#B0E0E6",fg="#191970")
        header_label.pack(expand=True,fill="both")
        month_label=Label(entry_frame,text="Month:",font=("consolas",10,"bold"),
                          bg="#B0E0E6",fg="#000000")
        year_label=Label(entry_frame,text="Year:",font=("consolas",10,"bold"),bg="#B0E0E6",fg="#000000")
        month_label.place(x=120,y=0)
        year_label.place(x=268,y=0)
        month_var=IntVar(entry_frame)
        year_var=IntVar(entry_frame)
        current_month=date.today().month
        current_year=date.today().year
        month_var.set(current_month)
        year_var.set(current_year)
        month_box=Spinbox(entry_frame,from_=1,to=12,width=5,textvariable=month_var)
        year_box=Spinbox(entry_frame,from_=0000,to=3000,width=5,textvariable=year_var)
        month_box.place(x=180,y=0)
        year_box.place(x=320,y=0)
        calendar_field=Text(result_frame,width=20,height=8,font=("consolsl",14),relief=RIDGE,borderwidth=2)
        calendar_field.pack(expand=False,fill=None)
        display_button=Button(button_frame,text="Display",bg="#191970",fg="#E0FFFF",command=displaycalendar)
        reset_button=Button(button_frame,text="Reset",bg="#191970",fg="#E0FFFF",command=reset)
        close_button=Button(button_frame,text="Close",bg="#191970",fg="#E0FFFF",command=close)
        display_button.place(x=140,y=0)
        reset_button.place(x=230,y=0)
        close_button.place(x=305,y=0)
        guiwindow.mainloop()
##button4=Button(Centre,text="Calendar",font=("Bold",16),bg="pink"
##               ,width=150,height=70,command=calendar1)
##button4.place(x=360,y=280)




##age calci
def agecalc():
    from datetime import date
    today=date.today()
    def exit():
        window6.destroy()
    def get_age():
        d=int(e1.get())
        m=int(e2.get())
        y=int(e3.get())
        age=today.year-y-((today.month,today.day)<(m,d))
        t1.config(state="normal")
        t1.delete("1.0",tk.END)
        t1.insert(tk.END,age)
        t1.config(state="disabled")
    import tkinter as tk
    window6=tk.Tk()
    window6.geometry("400x300")
    window6.config(bg="skyblue")
    window6.resizable(False,False)
    window6.title("Age Calculator")
    l1=tk.Label(window6,text="The Age Calculator",font=("Arial",20),fg="black",bg="skyblue")
    l2=tk.Label(window6,font=("Arial",12),text="Enter your BDay Date",fg="black",bg="skyblue")
    l_d=tk.Label(window6,text="Date:",font=("Arial",12,"bold"),fg="Darkblue",bg="skyblue")
    l_m=tk.Label(window6,text="Month:",font=("Arial",12,"bold"),fg="Darkblue",bg="skyblue")
    l_y=tk.Label(window6,text="Year:",font=("Arial",12,"bold"),fg="Darkblue",bg="skyblue")
    e1=tk.Entry(window6,width=5)
    e2=tk.Entry(window6,width=5)
    e3=tk.Entry(window6,width=5)
    b1=tk.Button(window6,text="Calculate Age",font=("Arial",13),command=get_age)
    l3=tk.Label(window6,text="The Calculated Age is:",font=("Arial",12,"bold"),fg="Darkblue",bg="skyblue")
    t1=tk.Text(window6,width=5,height=0,state="disabled")
    b2=tk.Button(window6,text="Exit",font=("Arial",13),command=exit)
    l1.place(x=70,y=5)
    l2.place(x=100,y=40)
    l_d.place(x=100,y=70)
    l_m.place(x=100,y=95)
    l_y.place(x=100,y=120)
    e1.place(x=180,y=70)
    e2.place(x=180,y=95)
    e3.place(x=180,y=120)
    b1.place(x=100,y=150)
    l3.place(x=50,y=200)
    t1.place(x=240,y=203)
    b2.place(x=100,y=230)
    window6.mainloop()
##button5=Button(Rhs,text="Age Cal",font=("Bold",16),bg="pink"
##               ,width=17,height=7,command=agecalc)
##button5.place(x=0,y=10)


#####STopWatch
from tkinter import *
from datetime import datetime
def stwatch():
    counter=66600
    running=False
    def counter_label(label):
        def count():
            if running:
                global counter
                if counter==66600:
                    display="Starting..."
                else:
                    tt=datetime.fromtimestamp(counter)
                    string=tt.strftime("%H :%M :%S")
                    display=string
                label["text"]=display
                label.after(1000,count)
                counter+=1
        count()
    def Start(label):
        global running
        running=True
        counter_label(label)
        start["state"]="disabled"
        stop["state"]="normal"
        reset["state"]="normal"
    def Stop():
        global running
        start["state"]="normal"
        stop["state"]="disabled"
        reset["state"]="normal"
        running=False
    def Reset(label):
        global counter
        counter=66600
        if running==False:
            reset["state"]="disabled"
            label["text"]="Welcome"
        else:
            label["text"]="starting..."
    root=Tk()
    root.title("StopWatch")
    root.minsize(width=250,height=70)
    label=Label(root,text="Welcome",fg="black",font=("Verdana",30,"bold"))
    label.pack()
    f=Frame(root)
    start=Button(f,text="Start",width=6,command=lambda:Start(label))
    stop=Button(f,text="Stop",width=6,state="disabled",command=Stop)
    reset=Button(f,text="Reset",width=6,state="disabled",command=lambda: Reset(label))
    f.pack(anchor="center",pady=5)
    start.pack(side="left")
    stop.pack(side="left")
    reset.pack(side="left")
    root.mainloop()
##button6=Button(Rhs,text="Stop Watch",font=("Bold",16),bg="red"
##               ,width=17,height=7,command=stwatch)
##button6.place(x=90,y=70)

def calcul():
    winc = Tk()
    winc.geometry("312x324")
    winc.resizable(0, 0)
    winc.title("Calculator")
    def btn_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)
    def bt_clear(): 
        global expression 
        expression = "" 
        input_text.set("")
    def bt_equal():
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = " "
     
    expression = " "
    input_text = StringVar()
    input_frame = Frame(winc, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
    input_frame.pack(side=TOP)
    input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)     
    input_field.grid(row=0, column=0)     
    input_field.pack(ipady=10)
    btns_frame = Frame(winc, width=312, height=272.5, bg="grey")     
    btns_frame.pack()
    # first row
    clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
     
    divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
     
    # second row
     
    seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
     
    eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
     
    nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
     
    multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
     
    # third row
     
    four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
     
    five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
     
    six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
     
    minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
     
    # fourth row
     
    one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
     
    two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
     
    three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
     
    plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
     
    # fourth row
     
    zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
     
    point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
     
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
     
    winc.mainloop()


##def weightc():
##    # Creating a GUI Window
##    windowwgh = Tk()
##    def from_kg():
##        gram = float(e2_value.get())*1000
##        pound = float(e2_value.get())*2.20462
##        ounce = float(e2_value.get())*35.274
##        t1.delete("1.0",END)
##        t1.insert(END, gram)
##        t2.delete("1.0", END)
##        t2.insert(END, pound)
##        t3.delete("1.0", END)
##        t3.insert(END, ounce)
##
##    e1 = Label(windowwgh, text="Input the weight in KG")
##    e2_value = StringVar()
##    e2 = Entry(windowwgh, textvariable=e2_value)
##    e3 = Label(windowwgh, text="Gram")
##    e4 = Label(windowwgh, text="Pound")
##    e5 = Label(window, text="Ounce")
##
##    t1 = Text(windowwgh, height=5, width=30)
##    t2 = Text(windowwgh, height=5, width=30)
##    t3 = Text(windowwgh, height=5, width=30)
##
##    b1 = Button(windowwgh, text="Convert", command=from_kg)
##
##    e1.grid(row=0, column=0)
##    e2.grid(row=0, column=1)
##    e3.grid(row=1, column=0)
##    e4.grid(row=1, column=1)
##    e5.grid(row=1, column=2)
##    t1.grid(row=2, column=0)
##    t2.grid(row=2, column=1)
##    t3.grid(row=2, column=2)
##    b1.grid(row=0, column=2)
##
##    windowwgh.mainloop()


##def stwatch1():
##    import tkinter as tink
##    count = -1
##    run = False
##    def var_name(mark):
##       def value():
##          if run:
##             global count
##             # Just beore starting
##             if count == -1:
##                show = "Starting"
##             else:
##                show = str(count)
##             mark['text'] = show
##             #Increment the count after
##             #every 1 second
##             mark.after(1000, value)
##             count += 1
##       value()
##    # While Running
##    def Start(mark):
##       global run
##       run = True
##       var_name(mark)
##       start['state'] = 'disabled'
##       stop['state'] = 'normal'
##       reset['state'] = 'normal'
##    # While stopped
##    def Stop():
##       global run
##       start['state'] = 'normal'
##       stop['state'] = 'disabled'
##       reset['state'] = 'normal'
##       run = False
##    # For Reset
##    def Reset(label):
##       global count
##       count = -1
##       if run == False:
##          reset['state'] = 'disabled'
##          mark['text'] = 'Welcome'
##       else:
##          mark['text'] = 'Start'
##
##    base = tink.Tk()
##    base.title("PYTHON STOPWATCH")
##    base.minsize(width=300, height=200)
##    mark = tink.Label(base, text="Welcome", fg="blue", font="Times 25 bold",bg="white")
##    mark.pack()
##    start = tink.Button(base, text='Start',width=25, command=lambda: Start(mark))
##    stop = tink.Button(base, text='Stop', width=25, state='disabled', command=Stop)
##    reset = tink.Button(base, text='Reset',width=25, state='disabled', command=lambda: Reset(mark))
##    start.pack()
##    stop.pack()
##    reset.pack()
##    base.mainloop()


#####chrome
def chr():
    import os
    #os.system("chrome.exe")
    os.startfile("chrome.exe")
#####gmail
def mail():
    import os
    os.startfile("https://mail.google.com/mail/u/0/#inbox")
###fb
def facebo():
    import os
    os.startfile("https://www.facebook.com/login/")
###instagram
def insta():
    import os
    os.startfile("https://www.instagram.com/accounts/login/")
##whatsapp
def whapp():
    import os
    os.startfile("https://web.whatsapp.com/%F0%9F%8C%90/en")







##image_icon8=PhotoImage(file="experimental-calendar-arcade.png")
##icon1=Button(Rhs,image=image_icon8,command=calendar1)
##icon1.place(x=10,y=30)
##image_icon9=PhotoImage(file="clock (1).png")
##icon2=Button(Rhs,image=image_icon9,command=stwatch)
##icon2.place(x=160,y=30)
##image_icon10=PhotoImage(file="calculator.png")
##icon3=Button(Rhs,image=image_icon10,command=calcul)
##icon3.place(x=10,y=190)
image_icon11=PhotoImage(file="images1.png")
icon4=Button(Rhs,image=image_icon11,command=agecalc)
icon4.place(x=5,y=5)
image_icon12=PhotoImage(file="download (5).png")
icon5=Button(Rhs,image=image_icon12,command=chr)
icon5.place(x=10,y=225)
image_icon13=PhotoImage(file="important-mail.png")
icon6=Button(Rhs,image=image_icon13,command=mail)
icon6.place(x=160,y=120)
image_icon14=PhotoImage(file="whapp.png")
icon7=Button(Rhs,image=image_icon14,command=whapp)
icon7.place(x=160,y=540)
image_icon15=PhotoImage(file="instagram-new--v2.png")
icon8=Button(Rhs,image=image_icon15,command=insta)
icon8.place(x=10,y=450)
image_icon16=PhotoImage(file="facebook-new.png")
icon9=Button(Rhs,image=image_icon16,command=facebo)
icon9.place(x=160,y=340)




window.mainloop()




















