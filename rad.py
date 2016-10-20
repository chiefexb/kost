#!/usr/bin/python
#coding: utf8
import requests
import json
import sys
def main ():
    url='http://playlist.rr.ru/cur_playing/mc/cur_playing.json'
    a=requests.get(url)
    h=a.content
    dj=json.loads(h) 
    art=dj['Current']['Artist']
    song=dj['Current']['Song']
    sys.stdout.write(art+';'+song)
    #nt u"Исполнитель:",unicode(art)
    #print u"Название песни:",unicode(song )
if __name__ == "__main__":
    main()

