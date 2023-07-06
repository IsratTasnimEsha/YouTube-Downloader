#BISMILLAHIR RAHMANIR RAHIM

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

FolderName= ''
Font='Copperplate Gothic Bold'
LightFont='Copperplate Gothic Light'

#File location
def openLocation():
    
    global FolderName
    FolderName=filedialog.askdirectory()

    if len(FolderName)>1:
        if len(FolderName)<=40:
            locationError1.config(text=FolderName[:41], fg='Snow', font=(LightFont, 9))
            locationError2.config(text='', fg='Snow', font=(LightFont, 1))
            locationError3.config(text='', fg='Snow', font=(LightFont, 1))
            locationError4.config(text='', fg='Snow', font=(LightFont, 1))

        elif len(FolderName)<=80:
            locationError1.config(text=FolderName[:41], fg='Snow', font=(LightFont, 9))
            locationError2.config(text=FolderName[41:], fg='Snow', font=(LightFont, 9))
            locationError3.config(text='', fg='Snow', font=(LightFont, 1))
            locationError4.config(text='', fg='Snow', font=(LightFont, 1))
            
        else:
            locationError1.config(text=FolderName[:41], fg='Snow', font=(LightFont, 9))
            locationError2.config(text=FolderName[41:81], fg='Snow', font=(LightFont, 9))
            locationError3.config(text=FolderName[81:], fg='Snow', font=(LightFont, 9))
            locationError4.config(text='', fg='Snow', font=(LightFont, 1))
    
    else:
        locationError1.config(text='Please Choose Folder', fg='Snow', font=(LightFont, 9))
        locationError2.config(text='', fg='Snow', font=(LightFont, 1))
        locationError3.config(text='', fg='Snow', font=(LightFont, 1))
        locationError4.config(text='', fg='Snow', font=(LightFont, 1))

#Download video
def downloadVideo():
    choice=videoChoice.get()
    videoURL=YouTubeEntryVar.get()
    qualityError.config(text='', fg='Snow', font=(LightFont, 10))

    if len(videoURL)>1:
        videoTitle=YouTube(videoURL).title
        
        if len(videoTitle)<=40:
            YouTubeError1.config(text=videoTitle[:41], fg='Snow', font=(LightFont, 9))
            YouTubeError2.config(text='', fg='Snow', font=(LightFont, 1))
            YouTubeError3.config(text='', fg='Snow', font=(LightFont, 1))
            YouTubeError4.config(text='', fg='Snow', font=(LightFont, 1))
            
        elif len(videoTitle)<=80:
            YouTubeError1.config(text=videoTitle[:41], fg='Snow', font=(LightFont, 9))
            YouTubeError2.config(text=videoTitle[41:91], fg='Snow', font=(LightFont, 9))
            YouTubeError3.config(text='', fg='Snow', font=(LightFont, 1))
            YouTubeError4.config(text='', fg='Snow', font=(LightFont, 1))
           
        else:
            YouTubeError1.config(text=videoTitle[:41], fg='Snow', font=(LightFont, 9))
            YouTubeError2.config(text=videoTitle[41:91], fg='Snow', font=(LightFont, 9))
            YouTubeError3.config(text=videoTitle[91:], fg='Snow', font=(LightFont, 9))
            YouTubeError4.config(text='', fg='Snow', font=(LightFont, 1))

        youtube=YouTube(videoURL)

        if choice==videoQualities[0]:
            select= youtube.streams.filter(progressive=True, file_extension='mp4').last()

        elif choice==videoQualities[1]:
            select= youtube.streams.filter(only_audio=True, file_extension='mp4').first()
            
        elif choice==videoQualities[2]:
            select= youtube.streams.filter(only_video=True, file_extension='mp4').first()
        
        else:
            qualityError.config(text='Please Select Quality', fg='Snow', font=(LightFont, 10))
    
    else:
        YouTubeError1.config(text='Please Give URL', fg='Snow', font=(LightFont, 9))
        YouTubeError2.config(text='', fg='Snow', font=(LightFont, 1))
        YouTubeError3.config(text='', fg='Snow', font=(LightFont, 1))
        YouTubeError4.config(text='', fg='Snow', font=(LightFont, 1))

    select.download(FolderName)
    qualityError.config(text='Download Completed!!!', fg='Snow', font=(Font, 12))

def Space():
    space=Label(app, bg='Teal', font=(Font, 20))
    space.grid()

app=Tk()
#Title of the app will be "StoreMe"
app.title("StoreMe")

#Icon of the app
app.iconbitmap('C:\\Users\\Asus\\Documents\\Downloads\\StoreMeIcon.ico')

#Height and width of screen
app.geometry('400x400')
app.configure(background='Teal')

#Content in the center of the screen
app.columnconfigure(0, weight=1)

Space()

#Youtube link label
YouTubeLabel= Label(app, text='URL Of The Video', fg='White', bg='Teal', font=(Font, 15))
YouTubeLabel.grid()

#Entry box
YouTubeEntryVar= StringVar()
YouTubeEntryVar= Entry(app, width=25, textvariable= YouTubeEntryVar, font=(LightFont, 10))
YouTubeEntryVar.grid()

#Error message for URL
YouTubeError1=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
YouTubeError2=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
YouTubeError3=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
YouTubeError4=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
YouTubeError1.grid()
YouTubeError2.grid()
YouTubeError3.grid()
YouTubeError4.grid()

#Asking path to save file
saveLabel= Label(app, text='Save The File', fg='White', bg='Teal', font=(Font, 15))
saveLabel.grid()

#Button to save file
saveEntry= Button(app, width=15, bg='DarkSlateGray', fg='White', text='Choose Path', font=(LightFont, 10), command=openLocation)
saveEntry.grid()

#Error message for location
locationError1=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
locationError2=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
locationError3=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
locationError4=  Label(app, text='', fg='White', bg='Teal', font=(Font, 1))
locationError1.grid()
locationError2.grid()
locationError3.grid()
locationError4.grid()

#Download quality
downloadQuality= Label(app, text='Select Quality', fg='White', bg='Teal', font= (Font, 15))
downloadQuality.grid()

#Select quality
videoQualities= ['Audio and Video', 'Only Audio', 'Only Video']
videoChoice= ttk.Combobox(app, values=videoQualities, font=(LightFont, 10)) 
videoChoice.grid()

#Download button
downloadButton= Button(app, width=15, bg='DarkSlateGray', fg='White', text='Download', font=(LightFont, 10), command= downloadVideo)
downloadButton.grid()

#Error message for URL
qualityError=  Label(app, text='', fg='White', bg='Teal', font=(Font, 9))
qualityError.grid()

Space()

#Screen until quit
app.mainloop()