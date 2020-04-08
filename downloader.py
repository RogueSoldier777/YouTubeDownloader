from pytube import YouTube
import tkinter, sys, subprocess

root = tkinter.Tk()

root.title('YouTube Video Downloader by @RogueSoldier777.')
root.geometry('960x540')

title = tkinter.Label(root, text='YouTube Video Downloader.', font=('Sen', 22))
title.pack()

videoLinkEntry = tkinter.Entry(root)
videoLinkEntry.pack()

def confirm():
    global yt
    global videoLink
    global videoTitle
    videoLink = videoLinkEntry.get()

    yt = YouTube(videoLink)

    videoTitle = yt.title
    videoTitleLabel = tkinter.Label(root, text=videoTitle)
    videoTitleLabel.pack()

    videoLength = round(yt.length / 60, 1)
    videoLengthMinutes = f'{videoLength} minutes.'
    videoLengthLabel = tkinter.Label(root, text=f'Length: {videoLengthMinutes}')
    videoLengthLabel.pack()

    videoAuthor = yt.author 
    videoAuthorLabel = tkinter.Label(root, text=f'By: {videoAuthor}')
    videoAuthorLabel.pack()

    videoViews = yt.views 
    videoViewsLabel = tkinter.Label(root, text=f'{videoViews} views')
    videoViewsLabel.pack()

confirmButton = tkinter.Button(root, text='Confirm', command=confirm)
confirmButton.pack()

def download():
    yt = YouTube(videoLink)

    stream = yt.streams.first()
    stream.download()

    sys.exit(0)

downloadButton = tkinter.Button(root, text='Download as MP4.', command=download)
downloadButton.pack()

def downloadasmp3():
    yt = YouTube(videoLink)

    stream = yt.streams.get_by_itag('140')
    stream.download()



downloadmp3 = tkinter.Button(root, text='Download as MP3.', command=downloadasmp3)
downloadmp3.pack()

if __name__ == "__main__":
    root.mainloop()
