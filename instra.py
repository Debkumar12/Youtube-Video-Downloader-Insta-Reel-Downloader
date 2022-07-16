#To Download any reel from intragram you must first login to your instagram from your device browser!!!!!
from instascrape import Reel 
import os
import time
URL=input("Enter thr Reel URL/Link to Download :")
sample_reel = Reel(URL)
sample_reel.scrape()
reeldir = os.getcwd()
sample_reel.download(fp=f"{reeldir}\\reel{int(time.time())}.mp4")
print(dir)
print(f"This reel has {sample_reel.video_view_count:,} views.")