from tkinter import *
from tkinter.filedialog import askopenfilename
from pygame import *
from PIL import ImageTk, Image
import paramiko
import os

def callback():
	filename = askopenfilename(initialdir = "/temp")
	print ("Changing The Constitution")
	sftp.put(filename,"/home/ssc/www/public/docs/Currently_Used_docs/doc_the_constitution.pdf")
	print("done")
	
def callback2():
	filename = askopenfilename(initialdir = "/temp")
	print ("Changing The Student Group Grant")
	sftp.put(filename,"/home/ssc/www/public/docs/Currently_Used_docs/application_student_group_grant.pdf")
	print("done")
def callback3():
	filename = askopenfilename(initialdir = "/temp")
	print ("Changing The First Year Guide")
	sftp.put(filename,"/home/ssc/www/public/docs/Currently_Used_docs/first_year_guide_2014.pdf")
	print("done")
def deleteFile():
	sftp.remove("/home/ssc/www/public/docs/Currently_Used_docs/doc_the_constitution.pdf")
	print("done removing the constitution")
def deleteFile2():
	sftp.remove("/home/ssc/www/public/docs/Currently_Used_docs/application_student_group_grant.pdf")
	print("done removing the student group grant")
def deleteFile3():
	sftp.remove("/home/ssc/www/public/docs/Currently_Used_docs/first_year_guide_2014.pdf")
	print("done removing the first year guide")
def submit():
	global username, password,sftp
	username = username_e.get()
	password = password_e.get()
	try:

		s.connect("westernssc.ca",22,username=username,password=password,timeout=4)
		sftp = s.open_sftp()
		print ("conn")
		try :
			sftp.get("/home/ssc/www/public/docs/Currently_Used_docs/doc_the_constitution.pdf",currentPath+"\\temp\\doc_the_constitution.pdf")
		except:
			print("File Probably Doesn't Exists")
		try :
			sftp.get("/home/ssc/www/public/docs/Currently_Used_docs/application_student_group_grant.pdf",currentPath+"\\temp\\application_student_group_grant.pdf")
		except:
			print("File Probably Doesn't Exists")
		try :
			sftp.get("/home/ssc/www/public/docs/Currently_Used_docs/first_year_guide_2014.pdf",currentPath+"\\temp\\first_year_guide_2014.pdf")
		except:
			print("File Probably Doesn't Exists")
		print("docs all loaded")

		submit.destroy()
		b = Button(canvas, text="CHANGE THE CONSTITUTION",height= 5, width=30,command=callback)
		b.grid(row = 0, column=0)
		bd= Button(canvas, text="REMOVE THIS FILE",height= 5, width=30, command = deleteFile)
		bd.grid(row = 1, column=0)
		b2 = Button(canvas, text="CHANGE THE STUDENT GROUP GRANT",height= 5, width=30,command=callback2)
		b2.grid(row = 0, column=1)
		b2d= Button(canvas, text="REMOVE THIS FILE",height= 5, width=30, command = deleteFile2)
		b2d.grid(row = 1, column=1)
		b3 = Button(canvas, text="CHANGE THE FIRST YEAR GUIDE",height= 5, width=30,command=callback3)
		b3.grid(row = 0, column=2)
		b2d= Button(canvas, text="REMOVE THIS FILE",height= 5, width=30, command = deleteFile3)
		b2d.grid(row = 1, column=2)
	except:
		print("Wrong Username/Password")

s= paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

currentPath= os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(currentPath+ "\\temp"):
	os.makedirs(currentPath+"\\temp")

master = Tk()
master.wm_title('Document Changer')
master.resizable(width=False, height=False)
canvas = Canvas(master, width=150, height=10)
canvas.pack()

Label(canvas, text="Username: ").grid(row=0, sticky=W)
Label(canvas, text="Password: ").grid(row=1, sticky=W)

username_e = Entry(canvas)
password_e = Entry(canvas, show = "*")

username_e.grid(row=0, column=1)
password_e.grid(row=1, column=1)

submit = Button(canvas, text="LOGIN",command=submit)
submit.grid(row= 2, column = 1)

mainloop();


