from tkinter import *
import os

root = Tk()
root.geometry("700x450")
root.minsize(700, 450)
root.maxsize(700, 450)
root.title("Shutdown 2.0")
fr = Frame(root).pack()
Label(root, text="ShutDown 2.0", font=("helvetica", 35, "bold")).place(x=190, y=150)


def restart():
    os.system("shutdown -r -t 1")
    root.destroy()


Button(fr, text="Restart!", font=("Helvetica", 26, "bold"), bd=10, command=restart, fg="green").place(x=140, y=210)


def shutdown():
    os.system("Shutdown -s -t 1")
    root.destroy()


Button(fr, text="Shutdown!", font=("Helvetica", 26, "bold"), bd=10, command=shutdown, fg="navy blue").place(x=320, y=210)

Label(root, text="Program@Paras4902", font=("Times New Roman", 15, "bold")).pack(side="bottom", anchor="se")
root.mainloop()
