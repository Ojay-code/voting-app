import customtkinter as ctk
import time
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3 as sl

# Setting default theme and appearance mode
ctk.set_default_color_theme("green") 
ctk.set_appearance_mode('dark')

#create databases
def database_president(vin, user_choice):
        con = sl.connect('Presidential.db')
        c = con.cursor()
        
        c.execute('CREATE TABLE IF NOT EXISTS presidential(vin text, choice text)')
        
        c.execute('INSERT INTO presidential(vin, choice) VALUES(?,?)',(vin, user_choice))
        
        con.commit()
        con.close()
        
def database_governor(vin, user_choice):
        con = sl.connect('Governorship.db')
        c = con.cursor()
        
        c.execute('CREATE TABLE IF NOT EXISTS Governorship(vin text, choice text)')
        
        c.execute('INSERT INTO Governorship(vin, choice) VALUES(?,?)',(vin, user_choice))
        
        con.commit()
        con.close()
        
def database_house_of_rep(vin, user_choice):
        con = sl.connect('House_of_Rep.db')
        c = con.cursor()
        
        c.execute('CREATE TABLE IF NOT EXISTS House_of_Rep(vin text, choice text)')
        
        c.execute('INSERT INTO House_of_Rep(vin, choice) VALUES(?,?)',(vin, user_choice))
        
        con.commit()
        con.close()

#create frame label
def label ():
    global label_2, label_button
    label_2= ctk.CTkLabel(root, text='Welcome To\nThe Strings\nVoting System',width= 270, height=450,
                          font=('Geometr415 Blk BT', 26), bg_color= "#000E0E")
    label_button = ctk.CTkButton(root, text=' NEXT >>',font=('Geometr415 Blk BT',12 ),corner_radius=15,bg_color= "#000E0E",fg_color="#00787E", command=main)
    label_button.place(x= 85, y= 350)
    label_2.place(x= 150, y= 245,anchor= ctk.CENTER)
    

#create frame widget
def main():
    global label_3, frame, label_4,entry_1,button_1
    label_2.place_forget()
    label_button.place_forget()
    frame = ctk.CTkFrame(master=root, width=250, height=210, corner_radius=15, bg_color="#000",fg_color="#000E0E")
    frame.place(x=150, y=255, anchor=ctk.CENTER)
   
    label_3 = ctk.CTkLabel(master=frame, text="Register", font=('Geometr415 Blk BT', 20))
    label_3.place(x=85, y=20)
    label_4 = ctk.CTkLabel(master=frame, text="Type in your VIN for PVC Confirmation",
                          font=('Geometr415 Blk BT', 9))
    label_4.place(x=45, y=45)

    entry_1 = ctk.CTkEntry(master=frame, width=200, placeholder_text="Enter VIN",
                          font=('Geometr415 Blk BT', 9), corner_radius=15, fg_color="#000")
    entry_1.place(x=25, y=95)

    button_1 = ctk.CTkButton(master=frame, width=180, text="Get Started", font=('Geometr415 Blk BT', 13),
                            corner_radius=15, fg_color="#00787E", command= buttons_component)
    button_1.place(x=33, y=140)

#buttons for the width
def buttons_component():
    global lbl_1,frame1
    if entry_1.get() == '':
        messagebox.showerror('Error', 'Input VIN inside the entry box')
    else:   
        frame.place_forget()
        frame1= ctk.CTkFrame(master=label_1, width=280, height=460, bg_color="#000E0E",fg_color="#000E0E")
        frame1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        lbl_1= ctk.CTkLabel(master=frame1, text= "PARTY POSITION",font=('Geometr415 Blk BT', 20))
        lbl_1.place(x= 63, y= 100)

        but_1= ctk.CTkButton(master= frame1,text='PRESIDENTIAL\nPARTY', width=225,height=50,font=('Geometr415 Blk BT',10),fg_color="#00787E",command=component_widget_1)
        but_1.place(x= 30, y= 140)

        but_2= ctk.CTkButton(master= frame1, text='GOVERNORSHIP\nPARTY', width= 225,height=50,font=('Geometr415 Blk BT',10), fg_color="#00787E",command=component_widget_2)
        but_2.place(x= 30, y= 200)

        but_3= ctk.CTkButton(master= frame1, text= "HOUSE OF\nRESPRESENTATIVES", width=225,height=50,font=('Geometr415 Blk BT',10),fg_color="#00787E",command=component_widget_3)
        but_3.place(x= 30, y= 260)

def component_widget_1():
        global butt_1, butt_2, butt_3, butt_4
        frame.place_forget()
        frame1= ctk.CTkFrame(master=label_1, width=280, height=460, bg_color="#000E0E",fg_color="#000E0E")
        frame1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        lbl_2 = ctk.CTkLabel(master=frame1, text="PRESIDENTIAL PARTY", font=('Geometr415 Blk BT', 20))
        lbl_2.place(x=35, y=100)


        LP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\LP.png").resize((60,60),Image.LANCZOS))
        butt_1= ctk.CTkButton(master=frame1, image= LP_Vote,text="LP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_presidential(butt_1,butt_2,butt_3,butt_4))
        butt_1.place(x=90, y=140)
        
        PDP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\PDP.png").resize((60,60),Image.LANCZOS))
        butt_2= ctk.CTkButton(master=frame1, image= PDP_Vote,text="PDP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_presidential(butt_1,butt_2,butt_3,butt_4))
        butt_2.place(x=90, y=200)

        APC_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\APC.png").resize((60,60),Image.LANCZOS))
        butt_3= ctk.CTkButton(master=frame1, image= APC_Vote,text="APC", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_presidential(butt_1,butt_2,butt_3,butt_4))
        butt_3.place(x=90, y=260)
        
        NNPP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\nnpp.png").resize((60,60),Image.LANCZOS))
        butt_4= ctk.CTkButton(master=frame1, image= NNPP_Vote,text="NNPP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_presidential(butt_1,butt_2,butt_3,butt_4))
        butt_4.place(x=90, y=320)

def disable(lp_btn, pdp_btn, apc_btn, nnpp_btn):
        lp_btn.configure(state= tk.DISABLED)
        pdp_btn.configure(state= tk.DISABLED)
        apc_btn.configure(state= tk.DISABLED)
        nnpp_btn.configure(state= tk.DISABLED)

# Button
def initialize_presidential(lp_btn, pdp_btn, apc_btn, nnpp_btn):
        global entry_1
        user_value = entry_1.get()
        try:
                vote_1 = lp_btn.cget("text")
                vote_2 = pdp_btn.cget("text")
                vote_3 = apc_btn.cget("text")
                vote_4 = nnpp_btn.cget("text")
                
                if vote_1 == "LP":
                        print(user_value)
                        print(vote_1)
                        database_president(user_value, vote_1)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_2 == "PDP":
                        database_president(user_value, vote_2)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_3 == "APC":
                        database_president(user_value, vote_3)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_4 == "NNPP":
                        database_president(user_value, vote_4)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
                
                
        except Exception as e:
                messagebox.showerror("Error","There was an error")
                print(e)

def initialize_governorship(lp_btn, pdp_btn, apc_btn, nnpp_btn):
        global entry_1
        user_value = entry_1.get()
        try:
                vote_1 = lp_btn.cget("text")
                vote_2 = pdp_btn.cget("text")
                vote_3 = apc_btn.cget("text")
                vote_4 = nnpp_btn.cget("text")
                
                if vote_1 == "LP":
                        print(user_value)
                        print(vote_1)
                        database_governor(user_value, vote_1)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_2 == "PDP":
                        database_governor(user_value, vote_2)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_3 == "APC":
                        database_governor(user_value, vote_3)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_4 == "NNPP":
                        database_governor(user_value, vote_4)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
                
                
        except Exception as e:
                messagebox.showerror("Error","There was an error")
                print(e)

def initialize_representative(lp_btn, pdp_btn, apc_btn, nnpp_btn):
        global entry_1
        user_value = entry_1.get()
        try:
                vote_1 = lp_btn.cget("text")
                vote_2 = pdp_btn.cget("text")
                vote_3 = apc_btn.cget("text")
                vote_4 = nnpp_btn.cget("text")
                
                if vote_1 == "LP":
                        print(user_value)
                        print(vote_1)
                        database_house_of_rep(user_value, vote_1)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_2 == "PDP":
                        database_house_of_rep(user_value, vote_2)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_3 == "APC":
                        database_house_of_rep(user_value, vote_3)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
        
                elif vote_4 == "NNPP":
                        database_house_of_rep(user_value, vote_4)
                        disable(lp_btn, pdp_btn, apc_btn, nnpp_btn)
                
                
        except Exception as e:
                messagebox.showerror("Error","There was an error")
                print(e)


def component_widget_2():
        frame.place_forget()
        frame1= ctk.CTkFrame(master=label_1, width=280, height=460, bg_color="#000E0E",fg_color="#000E0E")
        frame1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        lbl_3 = ctk.CTkLabel(master=frame1, text="GOVERNORSHIP PARTY", font=('Geometr415 Blk BT', 20))
        lbl_3.place(x=35, y=100)


        LP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\LP.png").resize((60,60),Image.LANCZOS))
        butt_1= ctk.CTkButton(master=frame1, image= LP_Vote,text="LP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_governorship(butt_1,butt_2,butt_3,butt_4))
        butt_1.place(x=90, y=140)

        PDP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\PDP.png").resize((60,60),Image.LANCZOS))
        butt_2= ctk.CTkButton(master=frame1, image= PDP_Vote,text="PDP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_governorship(butt_1,butt_2,butt_3,butt_4))
        butt_2.place(x=90, y=200)

        APC_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\APC.png").resize((60,60),Image.LANCZOS))
        butt_3= ctk.CTkButton(master=frame1, image= APC_Vote,text="APC", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_governorship(butt_1,butt_2,butt_3,butt_4))
        butt_3.place(x=90, y=260)
        
        NNPP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\nnpp.png").resize((60,60),Image.LANCZOS))
        butt_4= ctk.CTkButton(master=frame1, image= NNPP_Vote,text="NNP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_governorship(butt_1,butt_2,butt_3,butt_4))
        butt_4.place(x=90, y=320)

def component_widget_3():
        frame.place_forget()
        frame1= ctk.CTkFrame(master=label_1, width=280, height=460, bg_color="#000E0E",fg_color="#000E0E")
        frame1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        lbl_4 = ctk.CTkLabel(master=frame1, text="HOUSE OF\nREPRESENTATIVES", font=('Geometr415 Blk BT', 20))
        lbl_4.place(x=52, y=80)

# defining our image and creating of buttons
        LP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\LP.png").resize((60,60),Image.LANCZOS))
        butt_1= ctk.CTkButton(master=frame1, image= LP_Vote,text="LP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_representative(butt_1,butt_2,butt_3,butt_4))
        butt_1.place(x=90, y=140)

        PDP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\PDP.png").resize((60,60),Image.LANCZOS))
        butt_2= ctk.CTkButton(master=frame1, image= PDP_Vote,text="PDP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_representative(butt_1,butt_2,butt_3,butt_4))
        butt_2.place(x=90, y=200)

        APC_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\APC.png").resize((60,60),Image.LANCZOS))
        butt_3= ctk.CTkButton(master=frame1, image= APC_Vote,text="APC", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_representative(butt_1,butt_2,butt_3,butt_4))
        butt_3.place(x=90, y=260)
        
        NNPP_Vote= ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\nnpp.png").resize((60,60),Image.LANCZOS))
        butt_4= ctk.CTkButton(master=frame1, image= NNPP_Vote,text="NNP", width=90,height=40,font=('Geometr415 Blk BT',20),bg_color="#000E0E",fg_color="#00787E",command=lambda : initialize_representative(butt_1,butt_2,butt_3,butt_4))
        butt_4.place(x=90, y=320)


if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("300x500")
    root.iconbitmap(r'C:\Users\Suleiman\Desktop\Strings\voting-app\String_logo.ico')
    root.resizable(0,0)
    root.title("The Strings Voting App")
    root.config(background="#000E0E")
    img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\Suleiman\Desktop\Strings\voting-app\pattern.png"))
    label_1 = ctk.CTkLabel(master=root, image=img1)
    label_1.pack()
     
    label()

    root.mainloop()