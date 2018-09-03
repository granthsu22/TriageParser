import os
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename


def Parse(path):
    print("click\n")
    print(path)
    #print(size)
    #FileSize = 100 * 1024 * 1024
    DirName = "OutputLog"
    #SrcPath = "./TestSrc.txt"
    SrcPath = path
    count = 0
    #Creat the file dir
    if os.path.exists(DirName):
        count += 1
        TempDirName = DirName + str(count)
        while os.path.exists(TempDirName):
            count += 1
            TempDirName = DirName + str(count)
        DirName = DirName + str(count)
        os.mkdir(DirName)
    else:
        DirName = DirName
        os.mkdir(DirName)

    DestPath = "./" + DirName + "/EventLog.txt"
    #Open Src file
    SrcFile = open(SrcPath, 'r', encoding = 'UTF-8')
    DestFile = open(DestPath, 'w', encoding = 'UTF-8')

    section=''
    #Start to reverse the file
    for line in reversed(list(SrcFile)):
        section = line + section

        if '###Event Log' in line:
            DestFile.writelines(section)
            section=''
		
    SrcFile.close()
    DestFile.close()

def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        E1.insert(100,name)
    except:
        print("No file exists")

root = Tk()


#Row for size and file path
root.title("Parse Tool")
root.geometry('900x150');
L1 = Label(root, text= "SrcFile")
E1 = Entry(root, width=100)

L1.grid(row = 0)
E1.grid(row = 0, column=1)

Button2 = Button(root, text = "Dir", height=1, width=5)
Button2['command'] = lambda: OpenFile()
#Button2.config(height=100, width=100)
Button2.grid(padx = 10, pady=10,row = 0, column = 2)

#Button
Button1 = Button(root, text= "Start", height=1, width=5)
Button1['command'] = lambda: Parse(E1.get())
Button1.grid( padx = 10, pady=10, row = 2, column = 2)

root.mainloop()
