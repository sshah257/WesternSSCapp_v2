from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import paramiko
import os

def callback():
	filename = askopenfilename(initialdir = "/temp")
	print ("Changing Slider Picture 1")
	sftp.put(filename,"/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic1.jpg")
	print("done")
	
def callback2():
	filename = askopenfilename(initialdir = "/temp")
	print ("Changing Slider Picture 2")
	sftp.put(filename,"/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic2.jpg")
	print("done")
def callback3():
	filename = askopenfilename(initialdir = "/temp")
	print ("Changing Slider Picture 3")
	sftp.put(filename,"/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic3.jpg")
	print("done")
password= "~Samveg95"
username="chris"

s= paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect("westernssc.ca",22,username=username,password=password,timeout=4)
print("conn")
sftp = s.open_sftp()
currentPath= os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(currentPath+ "\\temp"):
	os.makedirs(currentPath+"\\temp")

for i in range (1,4):
	print("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg")
	sftp.get("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg",currentPath+"\\temp\\SliderPic"+str(i)+".jpg");


master = Tk()
master.wm_title('Slider Pictures')
canvas = Canvas(master, width=300, height=400)
# canvas2 = Canvas(master, width=300, height=400)
# canvas3 = Canvas(master, width=300, height=400)
canvas.pack()
# canvas2.pack()
# canvas3.pack()
icon = Image.open(currentPath+"\\temp\\SliderPic1.jpg")
icon = icon.resize((375,150))
icon2 = Image.open(currentPath+"\\temp\\SliderPic2.jpg")
icon2 = icon2.resize((375,150))
icon3 = Image.open(currentPath+"\\temp\\SliderPic3.jpg")
icon3 = icon3.resize((375,150))

image1 = ImageTk.PhotoImage(icon)
image2 =ImageTk.PhotoImage(icon2)
image3 =ImageTk.PhotoImage(icon3)

# icon2 = Image.open(currentPath+"\\temp\\SliderPic2.jpg")
# icon2 = icon2.resize((30,40))
# canvas.image = ImageTk.PhotoImage(icon2)

# icon3 = Image.open(currentPath+"\\temp\\SliderPic3.jpg")
# icon3 = icon3.resize((30,40))
# canvas.image = ImageTk.PhotoImage(icon3)
b = Button(canvas, text="CHANGE THIS SLIDER IMAGE",height= 250, width=375,command=callback, image = image1, compound = TOP)
b.pack(side=LEFT)
b2 = Button(canvas, text="CHANGE THIS SLIDER IMAGE",height= 250, width=375,command=callback2, image = image2, compound = TOP)
b2.pack(side=LEFT)
b3 = Button(canvas, text="CHANGE THIS SLIDER IMAGE",height= 250, width=375,command=callback3, image = image3, compound = TOP)
b3.pack(side=LEFT)


mainloop();

