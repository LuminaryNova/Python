from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

root = Tk()

root.state('zoomed')
root.title("Dayanand's bike mods and spares")
gen_font = Font(family='Comic Sans MS', size=30)
bg = Image.open("E:/Python/Dayanand/daynand.jpg")
bg = ImageTk.PhotoImage(bg)
bgcanvas = Canvas(root, width=1920, height=1080, bd=0, highlightthickness=0)
bgcanvas.pack(fill="both", expand=True)
bgcanvas.create_image(0, 0, image=bg, anchor=NW)

title = bgcanvas.create_text(530, 100, text="Welcome to Dayanand Bike Mods and Spares", fill="white", font=gen_font, anchor="w")


def main_scn():

    global yamaha_button, RE_button, kaw_button, bmw_button

    # yamaha
    yamaha_img = Image.open("E:/Python/Dayanand/yamaha.jpg")
    yamaha_img = ImageTk.PhotoImage(yamaha_img)
    yamaha_button = Button(root, width=600, height=336, image=yamaha_img, borderwidth=0, highlightthickness=0,command=yama_click)
    yamaha_button.image = yamaha_img
    yamaha_button.place(x=250, y=220)

    # re
    RE_img = Image.open("E:/Python/Dayanand/Re.jpg")
    RE_img = ImageTk.PhotoImage(RE_img)
    RE_button = Button(root, width=600, height=338, image=RE_img, borderwidth=0, highlightthickness=0, command=re_click)
    RE_button.image = RE_img
    RE_button.place(x=1100, y=220)

    # bmw
    bmw_img = Image.open("E:/Python/Dayanand/bmw-4753868_1280.jpg")
    bmw_img = ImageTk.PhotoImage(bmw_img)
    bmw_button = Button(root, width=600, height=338, image=bmw_img, borderwidth=0, highlightthickness=0, command=bmw_click)
    bmw_button.image = bmw_img
    bmw_button.place(x=250, y=650)

    # kaw
    kaw_img = Image.open("E:/Python/Dayanand/kawasaki-logo-2021.jpg")
    kaw_img = ImageTk.PhotoImage(kaw_img)
    kaw_button = Button(root, width=600, height=338, image=kaw_img, borderwidth=0, highlightthickness=0, command=kaw_click)
    kaw_button.image = kaw_img
    kaw_button.place(x=1100, y=650)
    


def destroy_main():
    kaw_button.destroy()
    bmw_button.destroy()
    yamaha_button.destroy()
    RE_button.destroy()
    bgcanvas.itemconfig(title, text='')



def choosebike():
    choose_bike = bgcanvas.create_text(820, 100, text="Choose a model", fill="white", font=gen_font, anchor="w")
    

def yamaha_bikes():
    rx100 = Image.open("E:\Python\Dayanand\\new-yamaha-rx-100.jpg")
    rx100 = ImageTk.PhotoImage(rx100)
    rx100btn = Button(root, width = 735, height = 393, borderwidth=0, image = rx100, highlightthickness=0)
    rx100btn.image = rx100
    rx100btn.place(x = 200, y = 400)
    
    r15 = Image.open("E:\Python\Dayanand\\New-Yamaha-R15-V3-17.jpg")
    r15.resize((735,393))
    r15 = ImageTk.PhotoImage(r15)
    r15btn = Button(root, image = r15, width = 735, height = 393, borderwidth=0, highlightthickness= 0)
    r15btn.image = r15
    r15btn.place(x = 1000, y = 400)

def bmw_bikes():
    S1000 = Image.open("E:\Python\Dayanand\k2yhofv.jpg")
    S1000 = ImageTk.PhotoImage(S1000)
    S1000btn = Button(root, width = 735, height = 450, borderwidth=0, image = S1000, highlightthickness=0)
    S1000btn.image = S1000
    S1000btn.place(x = 200, y = 400)
    
    R1250 = Image.open("E:\Python\Dayanand\Recall-BMW-R1250GSA-adventure-motorcycle-768x512.jpg")
    R1250 = ImageTk.PhotoImage(R1250)
    R1250btn = Button(root, image = R1250, width = 745, height = 450, borderwidth=0, highlightthickness= 0)
    R1250btn.image = R1250
    R1250btn.place(x = 1000, y = 400)

def kaw_bikes():
    Z900 = Image.open("E:\Python\Dayanand\MY22-Kawasaki-Z900-priced-at-INR-8.5-lakh-new-colour-launched_2.jpg")
    Z900 = ImageTk.PhotoImage(Z900)
    Z900btn = Button(root, width = 735, height = 393, borderwidth=0, image = Z900, highlightthickness=0)
    Z900btn.image = Z900
    Z900btn.place(x = 200, y = 400)
    
    ninja = Image.open("E:\Python\Dayanand\c11e049863cade39.jpg")
    ninja = ImageTk.PhotoImage(ninja)
    ninjabtn = Button(root, image = ninja, width = 735, height = 393, borderwidth=0, highlightthickness= 0)
    ninjabtn.image = ninja
    ninjabtn.place(x = 1000, y = 400)

def RE_bikes():
    gt650 = Image.open("E:\Python\Dayanand\side-view.jpg")
    gt650 = ImageTk.PhotoImage(gt650)
    gt650btn = Button(root, width = 735, height = 393, borderwidth=0, image = gt650, highlightthickness=0)
    gt650btn.image = gt650
    gt650btn.place(x = 200, y = 400)
    
    classic = Image.open("E:\Python\Dayanand\specifications-tribute-black.jpg")
    classic = ImageTk.PhotoImage(classic)
    classicbtn = Button(root, image = classic, width = 735, height = 393, borderwidth=0, highlightthickness= 0)
    classicbtn.image = classic
    classicbtn.place(x = 1000, y = 400) 

    
def yama_click():
    destroy_main()
    choosebike()
   
    yamaha_bikes()
    
    
def re_click():
    destroy_main()
    choosebike()
    RE_bikes()


def bmw_click():
    destroy_main()
    choosebike()
    bmw_bikes()
   

def kaw_click():
    destroy_main()
    choosebike()
    kaw_bikes()
   
def repair_screen():
    
    
main_scn()

root.mainloop()
