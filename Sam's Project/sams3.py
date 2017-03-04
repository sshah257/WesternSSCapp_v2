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
def submit():
	global username, password,sftp, currentPath, icon, icon2, icon3, image1, image2, image3
	username = username_e.get()
	password = password_e.get()
	try:
		s.connect("westernssc.ca",22,username=username,password=password,timeout=4)
		sftp = s.open_sftp()
		print("conn")

		for i in range (1,4):
			print("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg")
			try:
				sftp.get("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg",currentPath+"\\temp\\SliderPic"+str(i)+".jpg");
			except:
				print("SliderPic"+str(i)+".jpg does not exsist")

		username_e.destroy()
		password_e.destroy()
		submit.destroy()
		pass_label.destroy()

		icon = Image.open(currentPath+"\\temp\\SliderPic1.jpg")
		icon = icon.resize((375,150))
		icon2 = Image.open(currentPath+"\\temp\\SliderPic2.jpg")
		icon2 = icon2.resize((375,150))
		icon3 = Image.open(currentPath+"\\temp\\SliderPic3.jpg")
		icon3 = icon3.resize((375,150))
		image1 = ImageTk.PhotoImage(icon)
		image2 =ImageTk.PhotoImage(icon2)
		image3 =ImageTk.PhotoImage(icon3)



		b = Button(canvas, text="CHANGE THIS SLIDER IMAGE",height= 250, width=375,command=callback, image = image1, compound = TOP)
		b.grid(row = 0, column=0)
		b2 = Button(canvas, text="CHANGE THIS SLIDER IMAGE",height= 250, width=375,command=callback2, image = image2, compound = TOP)
		b2.grid(row = 0, column=1)
		b3 = Button(canvas, text="CHANGE THIS SLIDER IMAGE",height= 250, width=375,command=callback3, image = image3, compound = TOP)
		b3.grid(row = 0, column=2)
	except:
		print("Wrong Username/Password")
s= paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

currentPath= os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(currentPath+ "\\temp"):
	os.makedirs(currentPath+"\\temp")

master = Tk()
master.wm_title('Slider Pictures')
master.resizable(width=False, height=False)
canvas = Canvas(master, width=375, height=400)
canvas.pack()

Label(canvas, text="Username: ").grid(row=0, sticky=W)
pass_label = Label(canvas, text="Password: ")
pass_label.grid(row=1, sticky=W)

username_e = Entry(canvas)
password_e = Entry(canvas, show = "*")

username_e.grid(row=0, column=1)
password_e.grid(row=1, column=1)

submit = Button(canvas, text="LOGIN",command=submit)
submit.grid(row= 2, column = 1)

mainloop();

# password= "~Samveg95"
# username="chris"

# s.connect("westernssc.ca",22,username=username,password=password,timeout=4)
# print("conn")
# sftp = s.open_sftp()




# mainloop();

