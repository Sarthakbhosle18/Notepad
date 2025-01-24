from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
import os,sys
win=Tk()
selectinword = ''
def newwin():
    new=Toplevel(win)
    new.title("notepad")

def copy(): 
        global selectinword
        selectinword= main.get(SEL_FIRST, SEL_LAST)

def paste():
    global selectinword
    main.insert(INSERT,selectinword)

path=''
def openfile():
    global path
    content=main.get(0.0,END)
    if len(content)<=1:
        file=filedialog.askopenfile(filetypes=[("text property","*.txt")])
        path=file.name
        file=open(path,"r")
        con=(file.read())
        main.delete(0.0,END)
        main.insert(0.0,con)
    else:
            Message=messagebox.askyesnocancel(message="Do yo want to save",title="save or not" )
            if Message == True:
                save=filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("text property","*.txt")])
                savefiel=open(save.name,"w")
                con=savefiel.write(content)
                savefiel.close()
            elif Message==False:
                main.delete(0.0,END)
                openfile()
            
def save():
        global path 
        content=main.get(0.0,END)
        if path:
            file=open(path,"w")
            file.write(content)
            file.close()
        else:
            files=filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("text property","*.txt")])
            name=files.name
            file=open(name,"w")
            file.write(content)
            file.close()

def saveas():
    filepath=filedialog.asksaveasfile()
    print(filepath)

def exit():
    sys.exit()
navbar=Menu(win)



win.title("notepad")
win.config(menu=navbar)


fileMenu=Menu(navbar,tearoff=0)
navbar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New                            Ctrl+N")
fileMenu.add_command(label="New Window           Ctrl+Shift+N",command=newwin)
fileMenu.add_command(label="Open                         Ctrl+O",command=openfile)
win.bind("<Control-o>",openfile)
fileMenu.add_command(label="Save                         Ctrl+S",command=save)
fileMenu.add_command(label="Save As                    Ctrl+Shift+S",command=saveas)
win.bind("<Control-Shift-S>",saveas)
fileMenu.add_separator()
fileMenu.add_command(label="Page Setup")
fileMenu.add_command(label="Print                        Ctrl+P" )
fileMenu.add_command(label="Exit                         Ctrl+Q",command=exit)
win.bind("<Control-q>",exit)


editmenu=Menu(navbar,tearoff=0)
navbar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo                Ctrl+Z")
editmenu.add_command(label="Cut                 Ctrl+X")
editmenu.add_command(label="Copy                Ctrl+C", command=copy) 
win.bind("<Control-c>",copy)
editmenu.add_command(label="Paste               Ctrl+V", command=paste)
win.bind("<Control-v>",paste)
editmenu.add_command(label="Delete              Del")
win.bind("<Delete>")
editmenu.add_separator()
editmenu.add_command(label="Find                Ctrl+F")
editmenu.add_command(label="Find Next           F3")
editmenu.add_command(label="Find Previous       Shift+F3")
editmenu.add_command(label="Replace             Ctrl+H")
editmenu.add_command(label="Go To               Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All          Ctrl+A")
editmenu.add_command(label="Time/Date           F5")


formatmenu=Menu(navbar,tearoff=0)
navbar.add_cascade(label="Format",menu=formatmenu)
formatmenu.add_checkbutton(label="WordWrap")
formatmenu.add_command(label="Font")

viewmenu=Menu(navbar,tearoff=0)
navbar.add_cascade(label="View",menu=viewmenu)

zoommenu=Menu(viewmenu,tearoff=0)
viewmenu.add_cascade(label="Zoom",menu=zoommenu)
zoommenu.add_command(label="ZoomIn          Ctrl+Plus")
zoommenu.add_command(label="ZoomOut         Ctrl+Minus")
zoommenu.add_command(label="Defult                Ctrl+0")
viewmenu.add_checkbutton(label="Status Bar")

helpmenu=Menu(navbar, tearoff=0)
navbar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")
helpmenu.add_command(label="Send Feedback")
helpmenu.add_separator()
helpmenu.add_command(label="About Notepad")


main=Text(win)
main.pack(fill=BOTH,expand=True)


win.mainloop()