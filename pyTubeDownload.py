# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:43:00 2020
@author: MrtAlt
https://twitter.com/DrMuratAltun
https://altunmurat.wordpress.com/"
"""

# python 3.6 sürümü üzerinde oluşturlmuştur
# pytube ve tkinter kütüphanelerini kurmanız gerekir
import pytube
import tkinter as tk
#Youtube video URL
field = 'ytbUrl'
#forum oluşturma fonksiyonu bu proje için çok gerekli değil
#Ama genelde bu şeekilde kullanıyorum
def makeform(root, field):
    entries = {}
    row = tk.Frame(root)
    lab = tk.Label(row, width=22, text=field, anchor='w')
    ent = tk.Entry(row)
    ent.insert(0,'youtube linklerini araya virgül koyarak giriniz')
    row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        
    entries[field] = ent
    return entries

#youtube video indirme programı
def VideoDownload(entries):
    myVideos=str(entries['ytbUrl'].get()).split(',')
    print (myVideos)
    msg=""
    for video in myVideos:
        yt = pytube.YouTube(video)
        msg+=video
        msg+=" indiriliyor"
        msg+="\n"
        lab.config(text=msg)
        stream = yt.streams.filter(progressive=True).first()
        stream.download()
        msg+= video
        msg+=" indirildi"
        msg+="\n"
        lab.config(text=msg)
               
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Video İndirmece")
    ents = makeform(root, field)
    b1 = tk.Button(root, text='Video İndir', command=(lambda e=ents: VideoDownload(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    lab = tk.Label(width=50, height=20, text='Açıklamalar', anchor='w')
    lab.pack(side=tk.LEFT)
    root.mainloop()