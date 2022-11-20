from configparser import ConfigParser
import os
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
here = os.getcwd()
music_path = f"{here}{music_path}"
print(music_path)