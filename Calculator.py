#Tkinter Calculator

from tkinter import *

def click(event):
    global datavar
    val=event.widget.cget('text')
    if val=='=':
        if datavar.get().isdigit():
            value=int(datavar.get())
        else :
            try :
                value=eval(datavar.get())
            except Exception as ep:
                value='Error'
                
        datavar.set(value)
        Inputfield.update()
    elif val=='C':
        datavar.set('')
        Inputfield.update()
    else:
        datavar.set(datavar.get()+val)
        Inputfield.update()

def enterfun(event):
    if datavar.get().isdigit():
        value=int(datavar.get())
    else:
        try:
            value=eval(datavar.get())
        except Exception as ep:
            value='Error'
    datavar.set(value)
    Inputfield.update()

root=Tk()
root.geometry('270x355')
root.title('Calculator')
root.wm_iconbitmap(r'C:\Users\Anonymous\Downloads\Calc\2.ico')

#Tkinter Variable Class which will hold the data entered by user
datavar=StringVar()
datavar.set('')

#Creating Entrywidget
Inputfield=Entry(root,textvariable=datavar,font='arial 14 bold')
Inputfield.grid(columnspan=4,padx=5,ipadx=18,pady=5)
Inputfield.bind('<Return>',enterfun)

#Creating Buttons:
#First Row
bt1=Button(text='1',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt1.grid(row=1,column=0)
bt1.bind('<Button-1>',click)

bt2=Button(text='2',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt2.grid(row=1,column=1)
bt2.bind('<Button-1>',click)

bt3=Button(text='3',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt3.grid(row=1,column=2)
bt3.bind('<Button-1>',click)

bt4=Button(text='+',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='red')
bt4.grid(row=1,column=3)
bt4.bind('<Button-1>',click)

#Second Row

bt5=Button(text='4',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt5.grid(row=2,column=0,pady=7)
bt5.bind('<Button-1>',click)

bt6=Button(text='5',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt6.grid(row=2,column=1)
bt6.bind('<Button-1>',click)

bt7=Button(text='6',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt7.grid(row=2,column=2)
bt7.bind('<Button-1>',click)

bt8=Button(text='-',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='red')
bt8.grid(row=2,column=3)
bt8.bind('<Button-1>',click)

#Third Row

bt9=Button(text='7',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt9.grid(row=3,column=0)
bt9.bind('<Button-1>',click)

bt10=Button(text='8',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt10.grid(row=3,column=1)
bt10.bind('<Button-1>',click)

bt11=Button(text='9',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt11.grid(row=3,column=2)
bt11.bind('<Button-1>',click)

bt12=Button(text='*',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='red')
bt12.grid(row=3,column=3)
bt12.bind('<Button-1>',click)

#Fourth Row

bt13=Button(text='0',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt13.grid(row=4,column=0,pady=7)
bt13.bind('<Button-1>',click)

bt14=Button(text='(',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='red')
bt14.grid(row=4,column=1)
bt14.bind('<Button-1>',click)

bt15=Button(text=')',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='red')
bt15.grid(row=4,column=2)
bt15.bind('<Button-1>',click)

bt16=Button(text='/',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='red')
bt16.grid(row=4,column=3)
bt16.bind('<Button-1>',click)

#Fifth Row

bt17=Button(text='.',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='white')
bt17.grid(row=5,column=0)
bt17.bind('<Button-1>',click)

bt18=Button(text='%',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='red')
bt18.grid(row=5,column=1)
bt18.bind('<Button-1>',click)

bt19=Button(text='C',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='gold')
bt19.grid(row=5,column=2)
bt19.bind('<Button-1>',click)

bt20=Button(text='=',font='lucida 18 bold',padx=5,height=1,width=2,bg='black',fg='gold')
bt20.grid(row=5,column=3)
bt20.bind('<Button-1>',click)

#Status Bar
textvar=StringVar()
textvar.set('By Logical Coder')

l1=Label(root,textvar=textvar,relief=SUNKEN,anchor='w')
l1.grid(row=6,columnspan=4,ipadx=80,pady=10)


root.mainloop()
