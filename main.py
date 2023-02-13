from tkinter import *
from tkinter import messagebox
import sqlite3
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import time
import winsound

while True:
    url = "http://hasanadiguzel.com.tr/api/sondepremler"

    response = requests.get(url)
    data = response.json()

    veri = data["data"][0]
    yer=veri["yer"]
    tarih=veri["tarih"],veri["saat"]
    siddet=veri["ml"]
    if ("kadirli" in yer.lower() or "Kadirli" in yer or "KADIRLI" in yer or "kadirli" in yer) and siddet > 4:
        frequency = 1000  
        duration = 3000  
        print("Şiddet",siddet)

        winsound.Beep(frequency, duration)
    else:
        print("Şiddet",siddet,"bölge",yer)
    time.sleep(5)