from tkinter import *
from tkinter.messagebox import *
import mysql.connector
import re

oyna = Tk()
# oyna.geometry("300x500+500+20")
oyna.geometry("1000x600+80+50")
oyna.title("Registration")
oyna.resizable(False, False)
oyna.configure(bd=2)
oyna.iconbitmap("icon_oyna.ico")
img=PhotoImage(file='background.png')
Label(oyna, image=img).pack()

img_btn=PhotoImage(file='buttons.png')
img_btn2=PhotoImage(file='button (1).png')

back_g = Frame(oyna, width=300, height=450, bg='white')
back_g.place(x=350,y=80)

Label(back_g, text='Welcome', font=('Segoe Script',22), fg='black', bg='white').place(x=80,y=20)
Label(back_g,image=img_btn, bd=0, bg='white').place(x=10,y=130)
Label(back_g,image=img_btn, bd=0, bg='white').place(x=10,y=180)

db = mysql.connector.connect(
    host="localhost",
    user='root',
    database='new_data_base_db',
    password=''
)
cursor = db.cursor()

def add_user_data(username, email, login, password, phone):
    sql = "INSERT INTO newdatabase(username, email, login, password, phone) VALUES (%s, %s, %s, %s, %s)"
    values = (username, email, login, password, phone)
    cursor.execute(sql, values)
    db.commit()


def get_user_log(login):
    sql = "SELECT * FROM newdatabase WHERE login=%s"
    cursor.execute(sql, (login,))
    data = cursor.fetchone()
    return data

def get_user_pass(password):
    sql = "SELECT * FROM newdatabase WHERE login=%s"
    cursor.execute(sql, (password,))
    data = cursor.fetchone()
    return data

entrytxt1 = StringVar()
Entry(back_g, textvariable=entrytxt1, width=18, font=('Segoe Script', 14),bg='#F3F3F3', bd=0, justify=CENTER).place(x=21, y=135)

entrytxt2 = StringVar()
Entry(back_g, textvariable=entrytxt2, width=18, font=('Segoe Script', 14), bg='#F3F3F3', show='*', bd=0 ,justify=CENTER).place(x=21, y=185)


def click1():
    top = Toplevel()
    top.geometry('400x500+550+60')
    top.title("Sign up")
    top.configure(bg='white')
    top.iconbitmap('icon_oyna.ico')
    Label(top, text='Sign up', font=('Segoe Script', 22), bg='white', fg='black').place(x=140, y=10)
    first_name = Label(top, text='First name', font=('Segoe Script', 14), bg='white', fg='black')
    first_name.place(x=5, y=70)
    email = Label(top, text='E-mail', font=('Segoe Script', 14), bg='white', fg='black')
    email.place(x=5, y=120)
    login = Label(top, text='Login', font=('Segoe Script', 14), bg='white', fg='black')
    login.place(x=5, y=170)
    password = Label(top, text='Password', font=('Segoe Script', 14), bg='white', fg='black')
    password.place(x=5, y=220)
    phone_num = Label(top, text='Phone num', font=('Segoe Script', 14), bg='white', fg='black')
    phone_num.place(x=5, y=270)

    Label(top,image=img_btn2, bd=0, bg='white').place(x=139,y=70)
    Label(top,image=img_btn2, bd=0, bg='white').place(x=139,y=120)
    Label(top,image=img_btn2, bd=0, bg='white').place(x=139,y=170)
    Label(top,image=img_btn2, bd=0, bg='white').place(x=139,y=220)
    Label(top,image=img_btn2, bd=0, bg='white').place(x=139,y=270)
    entry1 = StringVar()
    entry2 = StringVar()
    entry3 = StringVar()
    entry4 = StringVar()
    entry5 = StringVar()
    Entry(top, textvariable=entry1,bg='#F3F3F3', width=20,bd=0, font=('Segoe Script', 11), justify=CENTER).place(x=146, y=75)
    Entry(top, textvariable=entry2,bg='#F3F3F3', width=20,bd=0, font=('Segoe Script', 11), justify=CENTER).place(x=146, y=125)
    Entry(top, textvariable=entry3,bg='#F3F3F3', width=20,bd=0, font=('Segoe Script', 11), justify=CENTER).place(x=146, y=175)
    Entry(top, textvariable=entry4,bg='#F3F3F3', width=20,bd=0, font=('Segoe Script', 11), justify=CENTER).place(x=146, y=225)
    Entry(top, textvariable=entry5,bg='#F3F3F3', width=20,bd=0, font=('Segoe Script', 11), justify=CENTER).place(x=146, y=275)


    def Done():
        add_user_data(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get())
        top.destroy()

    Button(top, text='Done!', font=('Segoe Script', 15), bd=0, bg='white', activebackground='white', command=Done).place(x=160, y=390)


btn1 = Button(back_g, text='Sign up', font=('Segoe Script', 15),activebackground='white', bd=0, bg='white', command=click1)
btn1.place(x=105, y=380)

countclick = 0
clicktext = "X"
userX_score = 0
userO_score = 0
playerX = ''
def Done1():
    global playerX, get_user_log
    login = entrytxt1.get()
    password = entrytxt2.get()

    user_data = get_user_log(login)
    if user_data is not None and user_data[3] == password:
        oyna = Toplevel()
        oyna.geometry('650x550+900+200')
        countclick = 0
        clicktext = "X"

        def givetxt(btnclicked):
            global countclick, clicktext, user_data
            if btnclicked['text'] == '':
                if countclick % 2 == 0:
                    btnclicked['text'] = "X"
                    countclick += 1
                else:
                    btnclicked['text'] = "O"
                    countclick += 1

        def restart_andclear():
            global countclick, clicktext
            btn1['text'] = ''
            btn2['text'] = ''
            btn3['text'] = ''
            btn4['text'] = ''
            btn5['text'] = ''
            btn6['text'] = ''
            btn7['text'] = ''
            btn8['text'] = ''
            btn9['text'] = ''
            btn1['bg'] = btn2['bg'] = btn3['bg'] = btn4['bg'] = btn5['bg'] = btn6['bg'] = btn7['bg'] = btn8['bg'] = \
            btn9['bg'] = '#f3f3f3'


        def givecolor(t1, t2, t3, t4, t5, t6, t7, t8):
            if t1:
                btn1['bg'] = btn2['bg'] = btn3['bg'] = "yellow"
            elif t2:
                btn4['bg'] = btn5['bg'] = btn6['bg'] = "yellow"
            elif t3:
                btn7['bg'] = btn8['bg'] = btn9['bg'] = "yellow"
            elif t4:
                btn1['bg'] = btn4['bg'] = btn7['bg'] = "yellow"
            elif t5:
                btn2['bg'] = btn5['bg'] = btn8['bg'] = "yellow"
            elif t6:
                btn3['bg'] = btn6['bg'] = btn9['bg'] = "yellow"
            elif t7:
                btn1['bg'] = btn5['bg'] = btn9['bg'] = "yellow"
            elif t8:
                btn3['bg'] = btn5['bg'] = btn7['bg'] = "yellow"

        def findwinner(btnclicked):
            global countclick, clicktext, userX_score, userO_score, playerX
            t1 = (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X') or (
            (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O'))
            t2 = (btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X') or (
            (btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O'))
            t3 = (btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X') or (
            (btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O'))

            t4 = (btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X') or (
            (btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O'))
            t5 = (btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X') or (
            (btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O'))
            t6 = (btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X') or (
            (btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'))

            t7 = (btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X') or (
            (btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O'))
            t8 = (btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X') or (
            (btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'))

            if t1 or t2 or t3 or t4 or t5 or t6 or t7 or t8:
                winner = btnclicked['text']
                if winner == 'X':
                    userX_score += 1
                    lblX_score['text'] = str(userX_score)
                    restart_andclear()
                elif winner == 'O':
                    userO_score += 1
                    lblO_score['text'] = str(userO_score)
                givecolor(t1, t2, t3, t4, t5, t6, t7, t8)
                showinfo("Winner!", f"Winner! {user_data[2]}")
                restart_andclear()
            elif countclick == 9:
                showinfo("Draw!", f"Draw!")
                restart_andclear()

        def click(btnclicked):
            global user_data
            givetxt(btnclicked)
            findwinner(btnclicked)

        framebtn = Frame(oyna)

        btn1 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn1))
        btn2 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn2))
        btn3 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn3))

        btn4 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn4))
        btn5 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn5))
        btn6 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn6))

        btn7 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn7))
        btn8 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn8))
        btn9 = Button(framebtn, width=10, height=5, text='', font=('Arial', 16), command=lambda: click(btn9))

        lblX_txt = Label(oyna, text=f"{user_data[2]}", font=('Arial', 12))
        lblX_score = Label(oyna, text='0', font=('Arial', 12))


        lblO_txt = Label(oyna, text='Opponent:', font=('Arial', 12))
        lblO_score = Label(oyna, text='0', font=('Arial', 12))

        btn1.grid(row=0, column=0)
        btn2.grid(row=0, column=1)
        btn3.grid(row=0, column=2)

        btn4.grid(row=1, column=0)
        btn5.grid(row=1, column=1)
        btn6.grid(row=1, column=2)

        btn7.grid(row=2, column=0)
        btn8.grid(row=2, column=1)
        btn9.grid(row=2, column=2)

        framebtn.place(x=50, y=65)
        lblX_txt.place(x=450, y=230)
        lblX_score.place(x=570, y=230)
        lblO_txt.place(x=450, y=290)
        lblO_score.place(x=570, y=290)

    else:
        showerror("Error", "Login or password is incorrect!")


btn2 = Button(back_g, text='Done!', font=('Segoe Script', 15), bd=0, activebackground='white', bg='white', command=Done1)
btn2.place(x=115, y=240)

oyna.mainloop()