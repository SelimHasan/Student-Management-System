from tkinter import *
import time

import ttkthemes
from tkinter import ttk
from PIL import ImageTk

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('smog')
root.geometry('1060x685+265+0')
root.title('Student Management system')

backgroud = ImageTk.PhotoImage(file='image/rootbg.jpg')
backgroud_label = Label(root, image=backgroud)
backgroud_label.place(x=0, y=0)

upperframe = Frame(root, bg='#162f33')
upperframe.place(x=25, y=5, width=1004, height=60)


def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H :%M :%S')
    datetimelabel.config(text=f'{date}\n{currenttime}')
    datetimelabel.after(1000, clock)


datetimelabel = Label(upperframe, bg='#162f33', bd=6, foreground='white', font=("times new roman ", 12))
datetimelabel.place(x=13, y=5)
clock()
leftframe = Frame(root, bg="#162f33", bd=4)
leftframe.place(x=25, y=80, width=320, height=575)

s = 'Student Management System'
head_label = Label(upperframe, text=s, borderwidth=6, foreground='white', bg='#162f33',
                   font=('ribbon-condensed', 30, 'bold'))
head_label.place(x=240, y=0)
databasebutton = ttk.Button(upperframe, text='Connect to Database')
databasebutton.place(x=860.5, y=26)
rightframe = Frame(root, bg='white')
rightframe.place(x=370, y=80, width=658, height=575)

frame_logo = ImageTk.PhotoImage(file='image/graduates.png')
frame_logo_label = Label(leftframe, image=frame_logo, bg='#162f33')
frame_logo_label.place(x=120, y=5)

addbutton = ttk.Button(leftframe, text='  \tAdd Student', width=33)
addbutton.place(x=35, y=110)
searchbutton = ttk.Button(leftframe, text='  \tSearch Student', width=33)
searchbutton.place(x=35, y=170)
deletebutton = ttk.Button(leftframe, text='  \tDelete Student', width=33)
deletebutton.place(x=35, y=230)
updatebutton = ttk.Button(leftframe, text='  \tUpdate Student', width=33)
updatebutton.place(x=35, y=290)
showbutton = ttk.Button(leftframe, text='  \tShow Student', width=33)
showbutton.place(x=35, y=350)

exportbutton = ttk.Button(leftframe, text='  \tExport Student', width=33)
exportbutton.place(x=35, y=410)
exitbutton = ttk.Button(leftframe, text='  \tExit System', width=33)
exitbutton.place(x=35, y=470)

scrollBarx = Scrollbar(rightframe, orient=HORIZONTAL)
scrollBarx.pack(side=BOTTOM, fill=X)
scrollBary = Scrollbar(rightframe, orient=VERTICAL)
scrollBary.pack(side=RIGHT, fill=Y)

studenttable = ttk.Treeview(rightframe, columns=('ID', 'Name', 'Mobile', 'Address', 'Batch', 'Email', 'Gender', 'D.O.B',
                                                 'Added time', 'Added Date', 'Father Name'),
                            xscrollcommand=scrollBarx.set, yscrollcommand=scrollBary.set)
studenttable.pack(fill=BOTH, expand=1)

scrollBarx.config(command=studenttable.xview)
scrollBary.config(command=studenttable.yview)

studenttable.heading('ID', text='ID')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile', text='Mobile')
studenttable.heading('Address', text='Address')
studenttable.heading('Batch', text='Batch')
studenttable.heading('Email', text='Email')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added time', text='Added time')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Father Name', text='Father Name')
studenttable.config(show='headings')

root.mainloop()
