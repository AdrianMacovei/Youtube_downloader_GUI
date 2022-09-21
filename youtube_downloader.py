import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox
import os


def createwidgets():

    link_label = Label(root, text="Youtube URL: ", bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destination: ", bg="#E8D579")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=45, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but = Button(root, text="Browse", command=browse, width=10, bg="#05E8E0")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but = Button(root, text="Download Video", command=download_video, width=25, bg="#05E8E0")
    download_but.grid(row=3, column=1, pady=3, padx=3)

    download_mp3_but = Button(root, text="Download MP3", command=download_mp3, width=25, bg="#05E8E0")
    download_mp3_but.grid(row=4, column=1, pady=3, padx=3)


def browse():

    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")

    download_path.set(download_dir)


def download_video():
    url = video_link.get()
    folder = download_path.get()
    get_video = YouTube(url)
    messagebox.showinfo("Downloading.........", f"Video:{get_video.title} will be downloaded in few seconds. Please wait!")
    get_stream = get_video.streams.get_by_resolution("720p")
    get_stream.download(folder)
    messagebox.showinfo("Finishing downloading",
                        f"Dogwnload successfully! You will find the video at {folder}.")

def download_mp3():
    url = video_link.get()
    folder = download_path.get()
    video = YouTube(url)
    messagebox.showinfo("Downloading.........",
                        f"Mp3: {video.title} will be downloaded in few seconds. Please wait!")
    mp3 = video.streams.filter(only_audio=True).first().download(folder)
    new_name = os.path.splitext(mp3)
    os.rename(mp3, new_name[0] + '.mp3')
    messagebox.showinfo("Finishing downloading", f"Download successfully! You will find the mp3 at {folder}.")

root = tk.Tk()

root.geometry("600x120")
root.resizable(False, False)
root.title("Pytube")
root.config(background="#000000")

video_link = StringVar()
download_path = StringVar()
createwidgets()

root.mainloop()

