import os
import time

# nohup <name> &
# This will allow you to close the console window.

USER = os.getenv("USER")
DOWNLOADSPATH = f"/home/{USER}/Downloads"

queryDelay = 1

extensions = {
    "Documents": ['.txt', '.odt', '.docx'],
    "Music":     ['.mp3', '.wav', '.flak', '.ogg'],
    "Pictures":  ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.tiff'],
    "Videos":    ['.mp4', '.mov', '.avi']
}

locations = extensions.keys()

while True:
    fileList = os.listdir(DOWNLOADSPATH)

    if fileList:
        for file in fileList:
            ext = file[file.rfind('.'):]

            for location in locations:
                if ext in extensions[location]:
                    os.replace(f"{DOWNLOADSPATH}/{file}", f"/home/{USER}/{location}/{file}")
                else:
                    pass

    time.sleep(queryDelay)