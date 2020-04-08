from pytube import YouTube
import tkinter, sys

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

downloadButton = tkinter.Button(root, text='Download as MP4.', command=download)
downloadButton.pack()

if __name__ == "__main__":
    root.mainloop()
