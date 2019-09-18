from tkinter import *
from tkinter import filedialog
import os

class yt:
	
	def savein(o, e):
		fd=filedialog.askdirectory(parent=o.root, title="Select folder to save your songs")
		o.root.ef.delete(0, END)
		o.root.ef.insert(0, fd)
	
	def dld(o, e):
		art=o.root.ea.get()
		sng=o.root.es.get()
		alb=o.root.eb.get()
		fld=o.root.ef.get()
		s="python3 ytcls.py --artist '"+art+"' --song '"+sng+"' --album '"+alb+"' --folder '"+fld+"'"
		print(s)
		os.system(s)
	
	def __init__(o):
		o.root=Tk()
		o.root.minsize(width=400, height=100)
		o.root.title("YouTube Downloader")

		o.root.ls=Label(o.root, text="Song:")
		o.root.la=Label(o.root, text="Artist:")
		o.root.lb=Label(o.root, text="Album:")
		o.root.lf=Label(o.root, text="Save in:")
		
		o.root.es=Entry(o.root)
		o.root.ea=Entry(o.root)
		o.root.eb=Entry(o.root)
		o.root.ef=Entry(o.root)

		o.root.dld=Button(text="Download")
		
		o.root.ls.grid(column=0, row=0)
		o.root.la.grid(column=0, row=1)
		o.root.lb.grid(column=0, row=2)
		o.root.lf.grid(column=0, row=3)
		
		o.root.es.grid(column=1, row=0)
		o.root.ea.grid(column=1, row=1)
		o.root.eb.grid(column=1, row=2)
		o.root.ef.grid(column=1, row=3)

		o.root.dld.grid(column=1, row=4)

		o.root.ef.bind("<Button-1>", o.savein)
		o.root.dld.bind("<Button-1>", o.dld)

		o.root.mainloop()

yto=yt()
