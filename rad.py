#!/usr/bin/python
#coding: utf8
import requests
import json
def main ():
    url='http://playlist.rr.ru/cur_playing/mc/cur_playing.json'
    a=requests.get(url)
    h=a.content
    dj=json.loads(h) 
    art=dj['Current']['Artist']
    song=dj['Current']['Song']
    print "Исполнитель:",art
    print "Название песни:",song   
if __name__ == "__main__":
    main()

