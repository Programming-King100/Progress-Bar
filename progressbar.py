from tkinter import *
from tkinter.ttk import *
import time

root=Tk()

root.title("progress Bar!")

root.geometry("300x300")

progress= Progressbar(root,orient=HORIZONTAL,length=200, mode='determinate')

def progress_bar():
    
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=40
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=80
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=100
    root.update_idletasks()
    time.sleep(1)
    
progress.place(x=70, y=100)
    

Button(root,text="Load",command=progress_bar).place(x=150,y=150)










root.mainloop()