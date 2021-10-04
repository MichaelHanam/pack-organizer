# pack-organizer
organizes samples in sample packs with emojis based on the sample type.

usage:
    python main.py path action extensions

for example:

    this script would run over every folder in the sample packs folder and edit all of the mp3, 
                                                 wav and rx2 files to have an appropriate emoji
                                                 
    python main.py "C:\Users\username\Desktop\Sample Packs" edit "mp3 wav rx2"


    this script would run over every folder in the sample packs folder and remove all of the
                                                 emojis from the mp3, wav and rx2 files's names

    python main.py "C:\Users\username\Desktop\Sample Packs" remove "mp3 wav rx2"