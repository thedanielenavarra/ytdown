import requests
import os
import json
import argparse
import ytapikey
def src(q, n):
    pld={"type": "video", "part": "snippet", "maxResults": n, "q": q, "key": ytapikey.getkey()} #"AIzaSyC89Pcgcts9ZRY4QCGWLq_3RGkjF-Hihdk"}
    url="https://www.googleapis.com/youtube/v3/search"
    r=requests.get(url, params=pld)
    resp=[]
    if r.status_code==requests.codes.ok:
        j=json.loads(r.text)
        #print("SEARCH OK: ", r.text)
        for items in j["items"]:
            resp.append({"order": "relevance", "title": items["snippet"]["title"], "id": items["id"]["videoId"], "channel": items["snippet"]["channelTitle"]})	
    else:
        print("ERROR SEARCHING: ", r.status_code, r.content)
    return resp

def getserverip():
	return open("SERVER_IP").read().strip()

def dwd(art, sng, vid, fn):
    url="http://"+getserverip()+"/youtubemp3/ytmp3/PRJ/convert.php"
    pld={"youtubelink": "https://wwww.youtube.com/watch?v="+vid}
    print("Link: ", vid)
    r=requests.get(url, params=pld, allow_redirects=True)
    r=json.loads(r.text)
    if r['error']:
        print(r)
    else:
        print("http://54.93.104.165/youtubemp3/ytmp3/PRJ/"+r["file"])
        rq=requests.get("http://"+getserverip()+"/youtubemp3/ytmp3/PRJ/"+r["file"])
        f=open(fn, "wb")
        f.write(rq.content)
        f.close()
        print("Saved in \""+fn+"\"")
        return fn

def adj(fn, t, r, a):
    s="id3tool -t '"+t+"' -a '"+a+"' -r '"+r+"' '"+fn+"'"
    os.system(s)

def main():
    ap=argparse.ArgumentParser(prog="YouTube downloader")
    ap.add_argument("--artist", metavar="ART", help="Artist", dest="art")
    ap.add_argument("--song", metavar="SONG", help="Song", dest="sng")
    ap.add_argument("--album", metavar="ALBUM", help="Album", dest="alb")
    ap.add_argument("--folder", metavar="FLD", help="Folder", dest="fld")
    args=ap.parse_args()
    print(args)
    art=args.art
    sng=args.sng
    fld=args.fld
    alb=args.alb
    if fld==None:
        fld="."
    if alb==None:
        alb=""
    if sng==None:
        print("Error: no song name provided")
    if art==None:
        art=""
    vids=src(art+" "+sng, 1)
    fn=dwd(art, sng, vids[0]["id"], fld+"/"+art+" - "+sng+".mp3")
    adj(fn, sng, art, alb)

