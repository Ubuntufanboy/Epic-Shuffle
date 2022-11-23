from configparser import ConfigParser
import os, time, random, playsound
from os import listdir

try:
    import playsound
except:
    print("Please install playsound")


try:
    from plyer import notification
except:
    print("Please install plyer")
# Welcome the user

print("Welcome to Epic-Shuffle!")
print("This code is still in Alpha! Feel free to contribute")

# Ask for tour

while 1:
    answer = input("Would you like a tour? (y/n) ")
    answer = answer.lower()
    if answer == "y":
        print("add tour here later")
    elif answer == "n":
        break
    else:
        print("Invalid answer")

# Tell user to config the ini file or use default values
config = ConfigParser()

# Get to config dir
os.chdir("..")
os.chdir("config")
try:
    config.read("config.ini")
except:
    print("Something went wrong with the config file")
    exit(1)
music_path = config.get("main", "path") # This gets the value of path in the ini file
os.chdir("..") # back to root dir
if music_path.startswith("!"): # We use ! to signify it belongs in the code's source code
    listed = list(music_path)
    listed.pop(0)
    music_path = "".join(listed)
    here = os.getcwd()
    music_path = f"{here}{music_path}"
print(music_path)
# Time to find all mp3 files
def find_music(directory, extension):
    print(directory)
    music = listdir(directory)
    for song in music:
        if not song.endswith(f".{extension}"):
            music.remove(song)
    return f"{directory}{random.choice(music)}"

def play(song):
    playsound.playsound(song)
while 1:
    try: # We check if _next is defined
        song = _next # if it is, then the current song is the old next
    except: # If not
        song = find_music(music_path,"mp3") # find a song and play it
    _next = find_music(music_path,"mp3") # And load up our next song on deck

    title = 'Epic Shuffle'

    message = f'Now playing: {song}!'

    #Notify 
    notification.notify(title= title,
                        message= message,
                        app_icon = "/home/apollo/example.png",
                        timeout= 10,
                        toast=False)
    
    message = f"NEXT: {_next}"

    notification.notify(title= title,
                        message= message,
                        app_icon = "/home/apollo/example.png",
                        timeout= 10,
                        toast=False)
    play(song)