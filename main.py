from pytube import YouTube
from os import fdopen
import pyttsx3
url=input("Enter the youtube URL/Link for Download :") 
link=url
yt1=YouTube(link)
print("--The Title of the vedio which you want to Download is --")
print(yt1.title)
answer=input("Do you want to download Thumnail with vedio(Y/N) ??")
if answer=='Y' or answer=='y':
    print(yt1.thumbnail_url)
    videos=yt1.streams.all()
    vid=list(enumerate(videos))
    for i in vid:
        print(i)
    st=int(input("Enter :"))
    videos[st].download()
    print("SuccessFully Downloaded")  
else:
    videos=yt1.streams.all()
    vid=list(enumerate(videos))
    for i in vid:
        print(i)
    st=int(input("Enter :"))
    videos[st].download()
    print("SuccessFully Downloaded")  
          
text_speech=pyttsx3.init()
value1="The Vedio is Successfully Downloaded,Thank you for Using Yutube Vedio Downloader Backend by Deb Kumar Das"

text_speech.say(value1)
text_speech.runAndWait()