import os
import json
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import ytstatus
from tkinter import messagebox
class lst:
		
	def uplst(o):
		if o.sav==False:
			messagebox.showwarning("Wait!", "To add songs to the list you have to save it first!\n\nClick on \"Save list\" and try again")
			return
		else:
			o.root.lx["text"]=o.cart
			o.root.L.delete(0, END)
			totsng=ytstatus.totsongs(o.savf)
			dones=ytstatus.listcheck(o.savf)
			for album in o.list[o.cart]:
				for song, d in o.list[o.cart][album]:
					o.root.L.insert(END, song)
			o.root.li["text"]=str(dones)+" / "+str(totsng)+" downloaded"
			o.root.update()
	
	def getinfo(o):
		ret={}
		ret["artist"]=o.root.ea.get()
		ret["song"]=o.root.es.get()
		ret["album"]=o.root.eb.get()
		return ret

	def openlist(o, e):
		print("Open list")
		f=filedialog.askopenfilename(parent=o.root)
		o.sav=True
		o.savf=f
		f=open(f, "r")
		j=f.read()
		o.list=json.loads(j)
		print(o.list)
		o.ats=sorted(o.list.keys())
		o.cart=o.ats[0]
		o.uplst()


	def savelist(o, e):
		print("Save list")
		f=filedialog.asksaveasfile(mode="w", defaultextension=".ytlist")
		f.write(json.dumps(o.list))
		o.sav=True
		o.savf=f.name
		f.close()
		print(f)


	def addsong(o, e):
		if o.sav==False:
			messagebox.showwarning("Wait!", "To add songs to the list you have to save it first!\n\nClick on \"Save list\" and try again")
			return 
		else:
			song=o.getinfo()
			print(song["artist"] in o.list)
			if song["artist"] not in o.list:
				o.list[song["artist"]]={}
			if song["album"] not in o.list[song["artist"]]:
				o.list[song["artist"]][song["album"]]=[]
			o.list[song["artist"]][song["album"]].append([song["song"], False])
			print(o.list)
			o.cart=song["artist"]
			o.ats=sorted(o.list.keys())
			o.uplst()
		

	def download(o, e):
		if o.sav == False:
			messagebox.showwarning("Wait!", "To download the songs you have to save the list.\n\nClick on \"Save list\" and try again")
			return
		else:
			print("Download")
			d=filedialog.askdirectory(parent=o.root, title="Where to save songs?")
			import ytsrc
			totsongs=0
			for a in o.list:
				for aa in o.list[a]:
					for s in o.list[a][aa]:
						totsongs=totsongs+1
			o.root.prg["maximum"]=totsongs
			print("Downloading...")
			o.root.update()
			sfa=0
			for artist in o.list:
				for album in o.list[artist]:
					for song, daun in o.list[artist][album]:
						if daun==False:
							print(song, "to download")
							fn=d+"/"+artist+" - "+song+".mp3"
							vids=ytsrc.src(artist+" "+song, 1)
							print("SEARCH: ",vids)
							ytsrc.dwd(artist, song, vids[0]["id"], fn)
							ytsrc.adj(fn, song, artist, album)
							if o.sav==True:
								o.root.prg["value"]=ytstatus.listcheck(o.savf)
							else:
								o.root.prg["value"]=o.root.prg["value"]+1
							o.uplst()
							o.list[artist][album][sfa]=[song, True]
							if o.sav==True:
								f=open(o.savf, "w")
								print("Updating", o.savf)
								f.write(json.dumps(o.list))
								f.close()
							o.root.update()
							sfa=sfa+1
					sfa=0
	def prevart(o, e):
		if o.ats.index(o.cart) != 0:
			o.cart=o.ats[o.ats.index(o.cart)-1]
			o.uplst()

	def nextart(o, e):
		if o.ats.index(o.cart) != len(o.ats)-1:
			o.cart=o.ats[o.ats.index(o.cart)+1]
			o.uplst()


	def rmsong(o, e):
		if o.root.L.curselection!=():
			seln=o.root.L.get(ANCHOR)
			a=""
			for album in o.list[o.cart]:
				print("look", seln, "in ", o.list[o.cart][album])
				if seln in o.list[o.cart][album]:
					print("FOUND")
					o.list[o.cart][album].remove(seln)
					break
			print(o.list)
			o.ats=sorted(o.list.keys())
			o.uplst()

	def lstres(o, e):
		ytstatus.listreset(o.savf)
		o.uplst()		

	def __init__(o):
		o.root=Tk()
		o.sav=False

		#GUI ELEMENTS
		o.root.bo	=Button(o.root, text="Open list")
		o.root.blf	=Button(o.root, text="Save list")
		o.root.ls	=Label(o.root, text="Song:")
		o.root.es	=Entry(o.root)
		o.root.la	=Label(o.root, text="Artist:")
		o.root.ea	=Entry(o.root)
		o.root.lb	=Label(o.root, text="Album:")
		o.root.eb	=Entry(o.root)
		o.root.li	=Label(o.root, text="info")
		o.root.ln	=Label(o.root)
		o.root.bs	=Button(o.root, text="Add song")
		o.root.lx	=Label(o.root, text="Artist")
		o.root.bd	=Button(o.root, text="Download songs!")
		o.root.bp	=Button(o.root, text="<")
		o.root.bn	=Button(o.root, text=">")
		o.root.L	=Listbox(o.root)
		o.root.br	=Button(o.root, text="Delete song")
		o.root.prg	=ttk.Progressbar(o.root, value=0)
		o.root.rlb	=Button(o.root, text="Reset list")
		o.root.il	=Label(o.root)
		
		#GUI PLACEMENT
		o.root.bo	.grid(column=0, row=0)
		o.root.blf	.grid(column=1, row=0)
		o.root.ls	.grid(column=0, row=1)
		o.root.es	.grid(column=1, row=1)
		o.root.la	.grid(column=0, row=2)
		o.root.ea	.grid(column=1, row=2)
		o.root.lb	.grid(column=0, row=3)
		o.root.eb	.grid(column=1, row=3)
		o.root.li	.grid(column=0, row=4)
		o.root.ln	.grid(column=1, row=4)
		o.root.bs	.grid(column=1, row=5)
		o.root.bd	.grid(column=1, row=8)
		o.root.rlb	.grid(column=2, row=8)
		o.root.lx	.grid(column=1, row=6)
		o.root.bp	.grid(column=0, row=7)
		o.root.bn	.grid(column=2, row=7)
		o.root.L	.grid(column=1, row=7)
		o.root.br	.grid(column=0, row=8)
		o.root.prg	.grid(column=1, row=9)

		#GUI EVENTS
		o.root.bo.bind("<Button-1>", o.openlist)
		o.root.blf.bind("<Button-1>", o.savelist)
		o.root.bs.bind("<Button-1>", o.addsong)
		o.root.bd.bind("<Button-1>", o.download)
		o.root.bp.bind("<Button-1>", o.prevart)
		o.root.bn.bind("<Button-1>", o.nextart)
		o.root.br.bind("<Button-1>", o.rmsong)
		o.root.rlb.bind("<Button-1>", o.lstres)
		
		o.cart=""
		o.list={}
				
		o.root.mainloop()


l=lst()
