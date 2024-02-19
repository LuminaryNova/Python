from tkinter import *
from tkinter.font import Font
from tkinterhtml import *
from PIL import Image, ImageTk
import psutil
import GPUtil
import requests
import time


cpu = 0
ram = 0
gpu_usage = 0
gpu_temp = 0
gpus = 0


def readings():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    gpus = GPUtil.getGPUs()
    gpu_temp = gpus[0].temperature
    gpu_usage = gpus[0].load
    bgcanvas.itemconfig(gpu_text, text = f'GPU Usage: {gpu_usage}',fill = "white", font = gen_font)
    bgcanvas.itemconfig(cpu_text, text=f'CPU Usage: {cpu}%', fill="white", font=gen_font)
    bgcanvas.itemconfig(ram_text, text=f'RAM Usage: {ram}%', fill="white", font=gen_font)
    bgcanvas.itemconfig(gpu_temp_text, text = f"GPU Temp: {gpu_temp}", fill = "white", font = gen_font)
    bgcanvas.after(1000, readings)

root = Tk()

root.attributes('-fullscreen', True)
root.title("Launcher by Shyam")

gen_font = Font(family = "Segoe Print", size = 20)

#background image 
bg = Image.open("My Stuff\Tkbackground.jpg")
bg = ImageTk.PhotoImage(bg)
bgcanvas = Canvas(root, width=1920, height=1050, bd=0, highlightthickness=0)
bgcanvas.pack(fill="both", expand=True)
bgcanvas.create_image(0, 0, image=bg, anchor=NW)

#button close
cl_original_image = Image.open("My Stuff\Tkbutton_close.jpg")
cl_resized_image = cl_original_image.resize((50, 50))
close_button = ImageTk.PhotoImage(cl_resized_image)
button_close = Button(root, command=root.quit, width=50, height=50, image=close_button, borderwidth=0, highlightthickness=0)
button_close.place(x = 1870, y = 2)

#button minimize
mn_original_image = Image.open("My Stuff\Tkminimize.jpg")
mn_resized_image = mn_original_image.resize((60,60))
min_button = ImageTk.PhotoImage(mn_resized_image)
button_min = Button(root, command = root.iconify, image=min_button, width = 60, height = 60, borderwidth=0, highlightthickness=0)
button_min.place(x = 1805, y = 0)

#readings
cpu_text = bgcanvas.create_text(30, 930, text=f'CPU Usage: {cpu}%', fill="white", font=gen_font, anchor="w")
ram_text = bgcanvas.create_text(30, 960, text=f'RAM Usage: {ram}%', fill="white", font=gen_font, anchor="w")
gpu_text = bgcanvas.create_text(30, 990, text=f"GPU Usage: {gpu_usage}%", fill="white", font=gen_font, anchor="w")
gpu_temp_text = bgcanvas.create_text(30, 1020, text=f"GPU Temp: {gpu_temp}", fill="white", font=gen_font, anchor="w")
readings()

#ip address
def ipaddress():
    global url, response, ip
    url = "https://api.ipify.org?format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
            ip = response.json()
            return ip["ip"]
public_ip = ipaddress()
location_text = bgcanvas.create_text(1780, 1050, text=f"IP:{public_ip}", font=gen_font, fill="white")

#hide ip
def hide_ip():
    global hide_again
    ip_hide.destroy()
    hide_again = Button(root, text = "Click to hide ip", bg = "black", fg = "white", borderwidth=0, highlightthickness= 0, font = ("helvetica", 12), command = hideip)
    hide_again.place(x = 1800, y = 1000 )

def hideip():
    global ip_hide
    hide_again.destroy()
    ip_hide = Button(root, text = "Click to reveal",bg = "grey", fg = "white", width = "24", font = ("helvetica", 14), command = hide_ip, highlightthickness= 0, borderwidth= 0)
    ip_hide.place(x=1688, y = 1035)
    
ip_hide = Button(root, text = "Click to reveal", bg = "grey", fg = "white", width = "24", font = ("helvetica", 14), command = hide_ip, highlightthickness= 0, borderwidth= 0)
ip_hide.place(x=1688, y = 1035)
    
#location and weather
api_key = "5980e2cabcee9aac4e610030246c1129"
geolocation_url = f"http://ip-api.com/json/{public_ip}"
geolocation_response = requests.get(geolocation_url)
geolocation_data = geolocation_response.json()
country_code = geolocation_data.get("countryCode")

weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={geolocation_data["city"]},{country_code}&appid={api_key}'
weather_response = requests.get(weather_url)
weather_data = weather_response.json()

location = bgcanvas.create_text(1760, 800, text = f"{geolocation_data['city']}, {geolocation_data['region']}\n{weather_data['weather'][0]['main']}, {int(weather_data['main']['temp'] - 273.15)}°C\nHumidity : {weather_data['main']['humidity']}%", fill = "white", font = gen_font)

#clock
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    bgcanvas.itemconfig(time_display, text = current_time)
    bgcanvas.after(1000, update_clock)
    
time_display = bgcanvas.create_text(960, 1030, font = ("Segoe Print", 30, "bold"), fill = "white")   
update_clock()

root.mainloop()