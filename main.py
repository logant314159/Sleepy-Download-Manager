import time

# nohup <name> &
# This will allow you to close the console window.

queryDelay = 1

documentsExt = []
musicExt = []
picturesExt = []
videosExt = []

while True:
    time.sleep(queryDelay)
    # Check for files in Downloads dir
        # If files, sort them based off of the Ext lists.