import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import subprocess
import time



def say(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio=r.listen(source)
            query=r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return f"Some Error corrued. Sorry from Nazeem"
if __name__ == '__main__':
    print('PyCharm')
    say("Hello Nazeem Khan I'm Your Jarvis Project")
    while True:
        print("Listening...")
        query=takeCommand()
        # query=query.lower()
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])

        if "open music" in query:
            musicpath = "F:\\music"
            music_files = os.listdir(musicpath)
            music_files.sort()  # Sort the files to ensure consistent order

            current_index = 0  # Index to keep track of the currently playing music
            music_is_on = True
            if "close" in takeCommand().lower():
                say("Closing music, sir")
                media_player_process.kill()  # Kill the current song
                music_is_on = False
                break

            while current_index < len(music_files):
                say("Opening Music, sir")

                # Start playing the current song
                current_song_path = os.path.join(musicpath, music_files[current_index])
                media_player_process = subprocess.Popen(["start", current_song_path], shell=True)

                # Wait for the current song to finish or user command
                while media_player_process.poll() is None:
                    next_command = takeCommand()

                    if "next" in next_command.lower():
                        say("Playing next song, sir")
                        media_player_process.kill()  # Kill the current song
                        current_index = (current_index + 1) % len(music_files)
                        # break
                    elif "close" in next_command.lower():
                        say("Closing music, sir")
                        media_player_process.kill()  # Kill the current song
                        music_is_on = False
                        break
            if current_index == len(music_files):
                say("No more songs in the folder, sir")








    