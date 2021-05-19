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

while True:
    fileList = os.listdir(DOWNLOADSPATH)

    if fileList:
        for file in fileList:
            pass
            # Check extension of file and sort accordingly.

    time.sleep(queryDelay)