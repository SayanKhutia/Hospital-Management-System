import tkinter
from window2 import menu

# root=login page
# root1=menu
# rootp=patient form

# variables
root = None
userbox = None
passbox = None
topframe = None
bottomframe = None
frame3 = None
login = None


# command for login button
def GET():
    global userbox, passbox, error
    S1 = userbox.get()
    S2 = passbox.get()
    if (S1 == 'sayan' and S2 == 'sayan@03'):
        menu()
    elif (S1 == 'rohit' and S2 == 'eldrago123'):
        menu()
    else:
        error = tkinter.Label(bottomframe, text="Wrong Id / Password \n TRY AGAIN", fg="red", font="bold")
        error.pack()


# LOGIN PAGE WINDOW
def Entry():
    global userbox, passbox, login, topframe, bottomframe, image_1
    root = tkinter.Tk()
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe = tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO  LANNISTERS HOSPITAL", bg='white', fg='orange',
                            font='Times 16 bold italic')
    username = tkinter.Label(topframe, text="USERNAME")
    userbox = tkinter.Entry(topframe)
    password = tkinter.Label(bottomframe, text="PASSWORD")
    passbox = tkinter.Entry(bottomframe, show="*")
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET, font="arial 8 bold")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()


Entry()
