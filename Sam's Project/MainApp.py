import tkinter as tk   # python3
#import Tkinter as tk   # python
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import paramiko
import sys
import os
from DropTarget import *
import six
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements
import time
TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):
	s= None
	sftp = None
	frames= {}
	container=None
	submit = None
	pass_label=None
	username_e=None
	password_e=None
	def __init__(self):
		tk.Tk.__init__(self)
		self.wm_title('WesternSSC Website editor')
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
		self.container = tk.Frame(self)
		self.container.pack(side="top", fill="both", expand=False)
		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		tk.Label(self.container, text="Username: ").grid(row=0,sticky="W")
		self.pass_label = tk.Label(self.container, text="Password: ")
		self.pass_label.grid(row=1, sticky="W")

		self.username_e = tk.Entry(self.container)
		self.password_e = tk.Entry(self.container, show = "*")

		self.username_e.grid(row=0, column=1)
		self.password_e.grid(row=1, column=1)

		self.submit = tk.Button(self.container, text="LOGIN",command =lambda: self.checkLogin(self.username_e.get(), self.password_e.get()))
		self.submit.grid(row= 2, column = 1)
	def checkLogin(self, username, password):

		# try:
		self.s= paramiko.SSHClient()
		self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.s.connect("westernssc.ca",22,username=username,password=password,timeout=4)
		self.sftp = self.s.open_sftp()
		print("conn")
		self.username_e.destroy()
		self.password_e.destroy()
		self.pass_label.destroy()
		self.submit.destroy()
		for F in ( PageOne, PageTwo, MainPage):
			page_name = F.__name__
			if page_name =="PageOne" or page_name =="PageTwo":
				self.frame = F(parent = self.container, controller= self,s=self.s, sftp= self.sftp)
			else:
				self.frame = F(parent=self.container, controller=self)
				

			self.frames[page_name] = self.frame
			self.frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame("MainPage")
		return True

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		# if page_name == "PageOne":
		# 		try:
		# 			currentPath= os.path.dirname(os.path.abspath(__file__))
		# 		except:
		# 			currentPath = os.path.dirname(os.path.abspath(sys.argv[0]))
		# 		if not os.path.exists(currentPath+ "\\temp"):
		# 			os.makedirs(currentPath+"\\temp")
		# 		for i in range (1,4):
		# 			print("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg")
		# 			try:
		# 				self.sftp.get("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg",currentPath+"\\temp\\SliderPic"+str(i)+".jpg");
		# 			except:
		# 				print("SliderPic"+str(i)+".jpg does not exsist")
		# elif page_name=="PageTwo":
		# 		try:
		# 			currentPath= os.path.dirname(os.path.abspath(__file__))
		# 		except:
		# 			currentPath= os.path.dirname(os.path.abspath(sys.argv[0]))
		# 		if not os.path.exists(currentPath+ "\\temp"):
		# 			os.makedirs(currentPath+"\\temp")
		# 		file = ["doc_the_constitution.pdf","application_student_group_grant.pdf","first_year_guide_2014.pdf","Committee_Charity.pdf","Committee_EventsAtLarge.pdf","Committee_Finance.pdf","Committee_Sciwiki.pdf","Committee_StudentSupport.pdf","Committee_StudentSupport.pdf"]
		# 		for i in range(len(file)):
		# 			try:
		# 				self.sftp.get("/home/ssc/www/public/docs/Currently_Used_docs/"+file[i],currentPath+"\\temp\\"+file[i])
		# 			except:
		# 				print("File "+file[i]+" Probably Doesn't Exists")
		frame.tkraise()
class MainPage (tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		button1 = tk.Button(self, text="Go to the Photo Uploads",width=163,height=5,
		                   command=lambda: controller.show_frame("PageOne"))
		button2 = tk.Button(self, text="Go to the File Uploads",width=163,height=5,
		                   command=lambda: controller.show_frame("PageTwo"))
		button1.pack()
		button2.pack()		


class PageOne(tk.Frame):
	icon = None
	icon2= None
	icon3= None
	image1 =None
	image2=None
	image3=None
	filename=""
	currImage = None
	def __init__(self, parent, controller,s,sftp):

		tk.Frame.__init__(self, parent)
		self.hwnd = self.winfo_id()
		pythoncom.OleInitialize()
		self.controller = controller
		try:
			currentPath= os.path.dirname(os.path.abspath("__file__"))
		except:
			currentPath = os.path.dirname(os.path.abspath(sys.argv[0]))
		if not os.path.exists(currentPath+ "\\temp"):
			os.makedirs(currentPath+"\\temp")
		for i in range (1,4):
			print("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg")
			try:
				sftp.get("/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(i)+".jpg",currentPath+"\\temp\\SliderPic"+str(i)+".jpg");
			except:
				print("SliderPic"+str(i)+".jpg does not exsist")
		self.after(100, lambda: update_list(self))
		self.after(100, self.updateCurrentPath)
		self.after(200, DropTarget, self.hwnd)
		label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
		# label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page",
		                   command=lambda: controller.show_frame("StartPage"))
		# button.pack()
		currentPath= os.path.dirname(os.path.abspath("__file__"))
		print(currentPath)
		self.icon = Image.open(currentPath+"\\temp\\SliderPic1.jpg")
		self.icon = self.icon.resize((375,150))
		self.icon2 = Image.open(currentPath+"\\temp\\SliderPic2.jpg")
		self.icon2 = self.icon2.resize((375,150))
		self.icon3 = Image.open(currentPath+"\\temp\\SliderPic3.jpg")
		self.icon3 = self.icon3.resize((375,150))
		self.image1 = ImageTk.PhotoImage(self.icon)
		self.image2 =ImageTk.PhotoImage(self.icon2)
		self.image3 =ImageTk.PhotoImage(self.icon3)


		self.b = tk.Button(self, text="CHANGE THIS SLIDER IMAGE",command=lambda: self.callback(0,sftp,controller),image = self.image1, compound = "top")
		self.b.grid(row =0 , column =1 )
		self.b2 = tk.Button(self, text="CHANGE THIS SLIDER IMAGE", command=lambda: self.callback(1,sftp,controller),image = self.image2, compound = "top")
		self.b2.grid(row = 0, column =2 )
		self.b3 = tk.Button(self, text="CHANGE THIS SLIDER IMAGE", command=lambda: self.callback(2,sftp,controller),image = self.image3, compound = "top")
		self.b3.grid(row = 0, column =3 )
		mainPage = tk.Button(self, text= "MainPage", command =lambda: controller.show_frame("MainPage"))
		mainPage.grid(row = 1, column =2 )
	def updateCurrentPath (self):
		files = getTextList()
		if len(files)>1:
			print("multiple files dropped, selecting last in the list")
		if self.checkProperFile(files[-1]):
			self.filename = files[-1]
			self.currImage =  Image.open(self.filename)
			self.currImage = self.currImage.resize((375,150))
			self.currentImage = ImageTk.PhotoImage(self.currImage)
			imagelbl= tk.Label(self, image= self.currentImage)
			imagelbl.grid(row=2, column =2)
		self.after(100, self.updateCurrentPath)
	def checkProperFile(self,n):
		lst= n.split(".")
		if lst[1]=="png" or lst[1]=="jpg":
			return True
		else:
			return False  
	def callback(self,num,sftp,controller):
		print(self.filename)
		if self.filename=="":
			self.filename = askopenfilename(initialdir = "/temp")
		print ("Changing Slider Picture"+str(num+1))
		sftp.put(self.filename,"/var/www/ssc/public/images/slider_pics/Currently_Used/SliderPic"+str(num+1)+".jpg")
		controller.show_frame("MainPage")
		print("done")

class PageTwo(tk.Frame):

	def __init__(self, parent, controller,s,sftp):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		try:
			currentPath= os.path.dirname(os.path.abspath("__file__"))
		except:
			currentPath= os.path.dirname(os.path.abspath(sys.argv[0]))
		if not os.path.exists(currentPath+ "\\temp"):
			os.makedirs(currentPath+"\\temp")
		file = ["doc_the_constitution.pdf","application_student_group_grant.pdf","first_year_guide_2014.pdf","Committee_Charity.pdf","Committee_EventsAtLarge.pdf","Committee_Finance.pdf","Committee_Sciwiki.pdf","Committee_StudentSupport.pdf","Committee_StudentSupport.pdf"]
		for i in range(len(file)):
			try:
				sftp.get("/home/ssc/www/public/docs/Currently_Used_docs/"+file[i],currentPath+"\\temp\\"+file[i])
			except:
				print("File "+file[i]+" Probably Doesn't Exists")

		print("docs all loaded")
		h=2
		w=30
		b = tk.Button(self, text="CHANGE THE CONSTITUTION",height= h, width=w,command=lambda: self.callback(0,sftp,controller))
		b.grid(row = 0, column=0)
		bd= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(0,sftp,controller))
		bd.grid(row = 1, column=0)
		b2 = tk.Button(self, text="CHANGE THE STUDENT GROUP GRANT",height= h, width=w,command=lambda: self.callback(1,sftp,controller))
		b2.grid(row = 0, column=1)
		b2d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(1,sftp,controller))
		b2d.grid(row = 1, column=1)
		b3 = tk.Button(self, text="CHANGE THE FIRST YEAR GUIDE",height= h, width=w,command=lambda: self.callback(2,sftp,controller))
		b3.grid(row = 0, column=2)
		b3d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(2,sftp,controller))
		b3d.grid(row = 1, column=2)

		b4 = tk.Button(self, text="CHANGE CHARITY FILE",height= h, width=w,command=lambda: self.callback(3,sftp,controller))
		b4.grid(row = 2, column=0)
		b4d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(3,sftp,controller))
		b4d.grid(row = 3, column=0)

		b5 = tk.Button(self, text="CHANGE EVENTS FILE",height= h, width=w,command=lambda: self.callback(4,sftp,controller))
		b5.grid(row = 2, column=1)
		b5d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(4,sftp,controller))
		b5d.grid(row = 3, column=1)		

		b6 = tk.Button(self, text="CHANGE FINANCE FILE",height= h, width=w,command=lambda: self.callback(5,sftp,controller))
		b6.grid(row = 2, column=2)
		b6d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(5,sftp,controller))
		b6d.grid(row = 3, column=2)		

		b7 = tk.Button(self, text="CHANGE SCIWIKI/INTERNE",height= h, width=w,command=lambda: self.callback(6,sftp,controller))
		b7.grid(row = 4, column=0)
		b7d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(6,sftp,controller))
		b7d.grid(row = 5, column=0)	

		b8 = tk.Button(self, text="CHANGE STUDENT SUPPORT",height= h, width=w,command=lambda: self.callback(7,sftp,controller))
		b8.grid(row = 4, column=1)
		b8d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(7,sftp,controller))
		b8d.grid(row = 5, column=1)	

		b5 = tk.Button(self, text="CHANGE CURRENT",height= h, width=w,command=lambda: self.callback(8,sftp,controller))
		b5.grid(row = 4, column=2)
		b5d= tk.Button(self, text="REMOVE THIS FILE",height= h, width=w, command = lambda: self.deleteFile(8,sftp,controller))
		b5d.grid(row = 5, column=2)		

		mainPage = tk.Button(self, text= "MainPage", command =lambda: controller.show_frame("MainPage"))
		mainPage.grid(row=6,column=1)
		# label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		# label.pack(side="top", fill="x", pady=10)
		# button = tk.Button(self, text="Go to the start page",
		#                    command=lambda: controller.show_frame("PageOne"))
		# button.pack()
	def callback(self,num,sftp,controller):
		filename = askopenfilename(initialdir = "/temp")

		file = ["doc_the_constitution.pdf","application_student_group_grant.pdf","first_year_guide_2014.pdf","Committee_Charity.pdf","Committee_EventsAtLarge.pdf","Committee_Finance.pdf","Committee_Sciwiki.pdf","Committee_StudentSupport.pdf","Committee_StudentSupport.pdf"]
		print ("changing "+file[num])
		sftp.put(filename,"/home/ssc/www/public/docs/Currently_Used_docs/"+file[num])
		controller.show_frame("MainPage")
		print("done")
	def deleteFile(self,num,sftp,controller):
		file = ["doc_the_constitution.pdf","application_student_group_grant.pdf","first_year_guide_2014.pdf","Committee_Charity.pdf","Committee_EventsAtLarge.pdf","Committee_Finance.pdf","Committee_Sciwiki.pdf","Committee_StudentSupport.pdf","Committee_StudentSupport.pdf"]
		print("removing "+file[num])
		sftp.remove("/home/ssc/www/public/docs/Currently_Used_docs/"+file[num])
		controller.show_frame("MainPage")
		print("done removing"+file[num])
def patch_crypto_be_discovery():

    """
    Monkey patches cryptography's backend detection.
    Objective: support pyinstaller freezing.
    """

    from cryptography.hazmat import backends

    try:
        from cryptography.hazmat.backends.commoncrypto.backend import backend as be_cc
    except ImportError:
        be_cc = None

    try:
        from cryptography.hazmat.backends.openssl.backend import backend as be_ossl
    except ImportError:
        be_ossl = None

    backends._available_backends_list = [be for be in (be_cc, be_ossl) if be is not None]

if __name__ == "__main__":
	patch_crypto_be_discovery()
	app = SampleApp()
	app.mainloop()