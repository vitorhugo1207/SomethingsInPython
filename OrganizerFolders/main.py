import os
import time

path = "Your/Path"

types = {".txt": "Text/", 
         ".png": "Image/", 
         ".jpg": "Image/", 
         ".webp": "Image/",
         ".exe": "Executables/",
         ".doc": "Documents/",
         ".docx": "Documents/",
         ".pdf": "Documents/",
         ".zip": "Compacted/",
         ".rar": "Compacted/",
         ".7zip": "Compacted/",
         ".iso": "iso/",
         ".torrent": "Torrent/",
         ".xlsx": "Documents/",
         ".xls": "Documents/",}
         
def organize(folderName, file):
    countDup = 2
    try:
        os.rename(f"{path}{file}", f"{path}{folderName}{file}")

    except FileNotFoundError: # Create folder
        os.mkdir(f"{path}{folderName}")
        os.rename(f"{path}{file}", f"{path}{folderName}{file}")
        
    except FileExistsError: # If File is Duplicate
        folderFiles = os.listdir(f"{path}{folderName}")
        for folderFile in folderFiles:
            if file == os.path.splitext(folderFile):
                countDup += 1
        os.rename(f"{path}{file}", f"{path}{folderName}{os.path.splitext(file)[0]} ({countDup}){os.path.splitext(file)[1]}")

def verify(type, folderName, supposedFile):
    if type == None: # File not Known
        organize("Others/", supposedFile)
    for file in files:
        if os.path.splitext(file)[1] == type: # File Known
            organize(folderName, file)

while(1):
    files = os.listdir(path)
    for type, folderName in types.items():
        verify(type, folderName, supposedFile=None)

    files = os.listdir(path)
    for supposedFile in files:
        if os.path.isfile(f"{path}/{supposedFile}"):
            verify(None, "Others/", supposedFile)

    time.sleep(2)
