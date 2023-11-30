import tkinter
import customtkinter
from pytube import YouTube
import os
import threading


# Add a global variable to track the download thread
download_thread = None
def StartDownload():
    global download_thread
    try:
        ytlink= link.get()
        ytObject=YouTube(ytlink, on_progress_callback=on_progress)
        # Specify the folder name
        folder_name = "MyYouTubeDownloads"
        # Get the user's Downloads directory
        download_folder = os.path.expanduser("~/Downloads")
        # Create the full path to the folder
        full_download_path = os.path.join(download_folder, folder_name)
        # Check if the folder exists, and if not, create it
        if not os.path.exists(full_download_path):
            os.makedirs(full_download_path)

        title.configure(text=ytObject.title,text_color='white')
        video=ytObject.streams.get_highest_resolution()
        
        finishLabel.configure(text="")
        video.download(output_path=full_download_path)
        finishLabel.configure(text="Downloaded!")
    except:
        # print('Error downloading video')
        finishLabel.configure(text='Download Error!',text_color='red')
    

def on_progress(stream,chunk,bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded= total_size-bytes_remaining
    percentage_of_completion=bytes_downloaded/total_size * 100
    # print(percentage_of_completion)
    per=str(int(percentage_of_completion))
    progressLabel.configure(text=per + '%')
    progressLabel.update()
    # Update progress
    progressBar.set(float(percentage_of_completion) / 100)
    progressBar.update()


# System settings
customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")

# Our Frame
app=customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Videos Downloader")

# Adding UI Elements
title=customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#link input
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350, height=40,textvariable=url_var)
link.pack()

# Progress Percentage

progressLabel= customtkinter.CTkLabel(app, text="0%")
progressLabel.pack()

progressBar=customtkinter.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Finished Dowloading.
finishLabel= customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download Button
download=customtkinter.CTkButton(app,text="Download",command=StartDownload)
download.pack(padx=10, pady=10)

# # Create a Cancel button
# cancel_button = customtkinter.CTkButton(app, text="Cancel", command=CancelDownload)
# cancel_button.pack(padx=10, pady=10)

# Run App
app.mainloop()
