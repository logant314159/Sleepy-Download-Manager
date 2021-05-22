import os
import time
import json

# nohup <name> &
# This will allow you to close the console window.

USER = os.getenv("USER")
DOWNLOADSPATH = f"/home/{USER}/Downloads"

queryDelay = 1

with open("extensions.json") as f:
    extensions = json.load(f)

locations = extensions.keys()

while True:
    fileList = os.listdir(DOWNLOADSPATH)

    if fileList:
        for file in fileList:
            ext = file[file.rfind('.'):]

            for location in locations:
                if ext in extensions[location]:
                    os.replace(f"{DOWNLOADSPATH}/{file}", f"/home/{USER}/{location}/{file}") # Might overwrite files ? Will have to check this.
                else:
                    pass

    time.sleep(queryDelay)