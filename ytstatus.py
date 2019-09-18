import json
import argparse

def listreset(fn):
	f=open(fn, "r")
	s=f.read()
	j=json.loads(s)
	s=0
	for art in j:
		for alb in j[art]:
			for song, d in j[art][alb]:
				j[art][alb][s][1]=False
				s=s+1
			s=0
	f.close()
	f=open(fn, "w")
	f.write(json.dumps(j))
	f.close()
                                        
def totsongs(fn):
	f=open(fn, "r")
	s=f.read()
	j=json.loads(s)
	DONES=0
	TOT=0
	for art in j:
		for alb in j[art]:
			for song, d in j[art][alb]:
				if d==True:
					DONES=DONES+1
				TOT=TOT+1
	return TOT

def listcheck(fn):
	f=open(fn, "r")
	s=f.read()
	j=json.loads(s)
	DONES=0
	TOT=0
	for art in j:
		for alb in j[art]:
			for song, d in j[art][alb]:
				if d==True:
					DONES=DONES+1
				TOT=TOT+1
	return DONES
