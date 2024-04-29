# import required module
import os

# assign directory


import tkinter as tk
from tkinter import filedialog

from tkinter import *

filesFound = []

directories = ["C:/Users/peter/Downloads/Testing"]


# create root window
root = Tk()
want = "folder.txt"
def selectDir():
    for i in range(len(directories)):
        globals()['string%s' % i].destroy()
    dir = filedialog.askdirectory(initialdir="/", title="Select a File")
    if(dir != ""):
        directories.append(dir)
    updateList()



def updateList():

    for i in range(len(directories)):
        globals()['string%s' % i] = tk.Label(text=directories[i])
        globals()['string%s' % i].pack()
        globals()['string%s' % i].place(x=450,y=(280 + i * 30))

threshHold = 0.75
def filesFinds(directory):

    global filesFound
    global threshHold
    alreadyAdded = False
    for filename in os.listdir(directory):
        target = FileNameText.get("1.0", 'end-1c')
        f = directory + "/" + filename
        if os.path.isfile(f):
            if (not case.get()):
                if(not exte.get()):
                    if (filename.lower() == target.lower()):
                        filesFound.append(directory + "/" + filename)
                        print("here")
                else:
                    if (filename.lower().split(".")[0] == target.lower().split(".")[0]):
                        filesFound.append(directory + "/" + filename)
                        print("here")
            if (not exte.get()):
                if(filename == target):
                    print(target)
                    filesFound.append(directory + "/" + filename)
            else:
                if (filename.split(",")[0] == target.split(",")[0]):
                    print(target)
                    filesFound.append(directory + "/" + filename)
            if(sim.get() == True):
                if (filename == target):
                    filesFound.append(directory + "/" + filename)
                for i in range(len(filename)):
                    try:
                        if(filename[i] == target[0]):
                            valuesMatch = 0
                            current = 0
                            while(True):
                                try:
                                    if(filename[i + current] == target[0 + current]):
                                        valuesMatch += 1
                                    current += 1
                                except:
                                    break

                            if(valuesMatch/len(target.split(".")[0]) > threshHold):
                                filesFound.append(directory + "/" + filename + " | Similar")
                    except:
                        pass
            elif(doc.get()):
                try:
                    a = open(f, "r")
                    fileRead = a.read()
                    print(fileRead)
                    for b in range(len(fileRead)):
                        if(fileRead[b] == target[0]):
                            valueMatched = 0
                            while(True):
                                try:
                                    if(fileRead[b + valueMatched] == target[valueMatched]):
                                        valueMatched += 1
                                    else:
                                        break
                                except:
                                    break
                            print(valueMatched)
                            print(target)
                            if(valueMatched == len(target)):
                                filesFound.append(directory + "/" + filename + " | FOUND IN FILE")
                except:
                    pass


        elif(os.path.isdir(directory + "/" + filename)):
                filesFinds(directory + "/" + filename)




def filesFind():
    global filesFound
    for i in range(len(filesFound)):
        globals()['One%s' % i].destroy()

    filesFound = []

    for directory in directories:
        filesFinds(directory)
    filesFound = list(set(filesFound))

    for i in range(len(filesFound)):
        globals()['One%s' % i] = tk.Label(text=filesFound[i])
        globals()['One%s' % i].pack()
        globals()['One%s' % i].place(x=5, y=(280 + i * 30))

updateList()

# root window title and dimension
root.title("Findthon")
# Set geometry (widthxheight)
root.geometry('700x500')

mainTitle = tk.Label(text="Findthon!")
mainTitle.pack()
mainTitle.place(x=100, y=10)

FileName = tk.Label(text="Enter File Name")
FileName.pack()
FileName.place(x=100, y=40)

FileNameText = tk.Text(width="20", height="5")
FileNameText.pack()
FileNameText.insert("end-1c", "folder.txt")
FileNameText.place(x=100, y=60)

buttonSearch = tk.Button(command=filesFind, text="Search!")
buttonSearch.pack()
buttonSearch.place(x=50, y=240)

case = tk.BooleanVar()
checkCase = tk.Checkbutton(text = "Case Sensitive?", variable=case)
checkCase.pack()
checkCase.place(x=180, y=150)

sim = tk.BooleanVar()
checkClose = tk.Checkbutton(text = "Check for Similar?", variable=sim)
checkClose.pack()
checkClose.place(x=180, y=170)

doc = tk.BooleanVar()
checkDoc = tk.Checkbutton(text = "Search Text Documents?", variable=doc)
checkDoc.pack()
checkDoc.place(x=180, y=190)

exte = tk.BooleanVar()
checkExte = tk.Checkbutton(text = "Ignore Extension?", variable=exte)
checkExte.pack()
checkExte.place(x=180, y=210)

button = tk.Button(command=selectDir, text="Enter Directory")
button.pack()
button.place(x=300, y=240)
# all widgets will be here
# Execute Tkinter
root.mainloop()














