from selenium import webdriver
import urllib
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import urllib.request
from download import downloadImage
from threading import Thread

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import re
import os

root = Tk()
root.geometry("600x300")
root.configure(background='#f6f6f6')
frame = Frame(root, background="#0168ff", width=20,
              height=200, padx=20, pady=20)
infoLabel = Label(frame, text="Please paste the desired URL in the box ↑",
      fg="white", background="#0168ff", wraplength=500, justify=CENTER)

entry = Entry(root, width=30, font=("Calibre", 18))


def getText():
    url = entry.get()
    imageScrapper(url)


def messagePop():
   messagebox.showinfo("Download report", "All the pictures have been downloaded sucessfully")


def informationDisplay(text):
    Label(frame, text="Images to be downloaded",
      fg="white", background="#0168ff", wraplength=500, justify=CENTER).pack()


def infoUpdater(textUpdate):
    infoLabel.config(text = textUpdate)

def imageScrapper(url):
    infoUpdater("Going to the website: ")
    options = Options()
    options.add_argument('--headless')
    # url = "https://ww6.readblackclover.com/chapter/black-clover-colored-chapter-258/"


    driver = webdriver.Firefox(options=options)

    
    
    infoUpdater("Getting tools ready ")
    driver.get(url)
    

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    imageLinkArrays = []

    

    SCROLL_PAUSE_TIME = 5

    # Get scroll height

    last_height = driver.execute_script("return document.body.scrollHeight")
    
    infoUpdater("Scrolling the webpage....")

    while True:

        images = driver.find_elements_by_tag_name('img')
        try:

            for image in images:
                if (link := image.get_attribute("src")) :#make sure to install python3.8 to use the walrus
                    imageLinkArrays.append(link)
        except StaleElementReferenceException as e:
            raise e

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        
        print("last height = " + str(last_height))
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        # Calculate new scroll height and compare with last scroll height
    
        print("new height = "+ str(new_height))

        if new_height == last_height:
            infoUpdater("Scrolling complete")  
            break
        last_height = new_height

    

    uniqueSets = set(imageLinkArrays)

    
    time.sleep(.5)
    infoUpdater("Unique images: " + str(len(uniqueSets)))

    

    print(len(imageLinkArrays))
    print(len(uniqueSets))
    driver.close()

    counter = 0
    for i in uniqueSets:
        print(i)
        try:
            #urllib.request.urlretrieve(i, str(counter)+".jpg")
            if '.png' in i:
                downloadImage(i, str(counter)+".png")
                infoUpdater("Downloading "+ str(counter+1)+ " of "+ str(len(uniqueSets)))
                
            elif '.jpg' in i:
                downloadImage(i, str(counter)+".jpg")
                infoUpdater("Downloading "+ str(counter+1)+ " of "+ str(len(uniqueSets)))
            
            
        except:
            print("Error downloading......  " + str(counter))
            infoUpdater("Error downloading .... ")

        
        counter = counter + 1
    
    entry.delete(0, 'end')
    infoUpdater("Please paste the desired URL in the box ↑")
    messagePop()
        

label = Label(root, text="Image Downloader", pady=30,
              background="#f6f6f6", fg="#0168ff", font=("Open Sans", 16, 'bold'))


infoLabel.pack()
label.pack()


button = Button(root, text="Download the images", width=25, height = 2, command=lambda: Thread(target = getText).start())


label.pack()
entry.pack(fill=NONE)


frameSpace = Frame(root, height=35)
frameSpace1 = Frame(root, height=35)
frameSpace1.pack()
button.pack()

frameSpace.pack()

frame.pack(fill=BOTH)
root.title('Image Downloader')
root.mainloop()


