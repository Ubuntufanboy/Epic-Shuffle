# Planning

### Welcome screen

gives the user a welcome and asks if the
user wants a tour or if the user just wants
to continue onto the program

### User folder

2 options:

designated folder for this program and user
can add mp3 files into the proram

or

program asks for a file path if not provided
in the conf file.

### Playing music

Might use Silver or playsound as the driver
It depends on how the program is structured

### Skipping songs

Have a thread constantly check for a keybind
if pressed kill the song and play the next

### Exit keybinds

Have a thread listen for the a keybind and
exit the program if that key is pressed 

### Conf
 
Use ini for config and ask for some simple
values to use the program. Do not let the
user use the program without editing the ini