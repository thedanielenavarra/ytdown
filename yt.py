import os
from tkinter import *


class yt:
	def b1(o, e):
		os.system("python3 ytgui.py")

	def b2(o, e):
		os.system("python3 ytlst.py")

	def b3(o, e):
		os.system("python3 mssrc.py")

	def __init__(o):
		o.root=Tk()
		o.root.title("YouTube Downloader")
		o.root.b1=Button(o.root, text="Download a song")
		o.root.b2=Button(o.root, text="Create list of songs")
		o.root.b3=Button(o.root, text="Search a song")
		
		o.root.b1.grid(column=0, row=0)
		o.root.b2.grid(column=0, row=1)
		o.root.b3.grid(column=0, row=2)
		
		o.root.b1.bind("<Button-1>", o.b1)
		o.root.b2.bind("<Button-1>", o.b2)
		o.root.b3.bind("<Button-1>", o.b3)
		
		o.root.mainloop()
y=yt()
