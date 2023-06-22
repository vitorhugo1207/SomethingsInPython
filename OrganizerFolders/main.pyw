import os
import time

path = "/your/path/"

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
         ".iso": "ISO/",
         ".img": "ISO/",
         ".torrent": "Torrent/",
         ".xlsx": "Documents/",
         ".xls": "Documents/",
         ".mkv": "Video/",
         ".mp4": "Video/",
         ".wav": "Audio/",
         ".mp3": "Audio/",
         ".java": "Script/",
         ".py": "Script/",
         ".pyw": "Script/",
         ".js": "Script/",
         ".c": "Script/",
         ".cpp": "Script/"}

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
            if file == folderFile:
                countDup += 1
        os.rename(f"{path}{file}", f"{path}{folderName}{os.path.splitext(file)[0]} ({countDup}){os.path.splitext(file)[1]}")

def verify():
    otherFiles = []
    for file in files:
        for type, folderName in types.items():
            if os.path.splitext(file)[1] == type: # File Known
                organize(folderName, file)
            else:
                count =+ 1
            
            if count - 1 == len(type) and os.path.isfile(f"{path}/{file}") and os.path.splitext(file)[1] == None and not os.path.splitext(file)[1] == ".tmp":
                otherFiles.append(file)
                print(otherFiles)
    
    for otherFile in otherFiles:
        organize("Others/", otherFile)

while(1):
    files = os.listdir(path)
    verify()
    time.sleep(2)
