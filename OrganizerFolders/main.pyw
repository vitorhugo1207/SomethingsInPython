import os
import time
from windows_toasts import WindowsToaster, ToastText1

path = "C:/Users/vitor/Downloads/"

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
         ".cpp": "Script/",
         ".gif":"Image/",
         ".appinstaller":"Executables/",
         ".msi": "Executables/"}

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

    except PermissionError: # When another program is using the file
        return

def notification(file, folderName):
    newToast = ToastText1()
    newToast.SetBody(f'Arquivo {file} moved to {folderName.replace("/", "")}. \nClick to open folder.')
    pathReplaced = path.replace("/", "\\")
    folderNameReplaced = folderName.replace("/", "\\")
    newToast.on_activated = lambda _: os.system(f'explorer "{pathReplaced}{folderNameReplaced}"')
    wintoaster.show_toast(newToast)

def verify():
    otherFiles = []
    for file in files:
        for type, folderName in types.items():
            if os.path.splitext(file)[1] == type: # File Known
                organize(folderName, file)
                notification(file, folderName)
            else:
                count =+ 1
            
            if count - 1 == len(type) and os.path.isfile(f"{path}/{file}") and os.path.splitext(file)[1] == None and not os.path.splitext(file)[1] == ".tmp":
                otherFiles.append(file)
                notification(file, folderName)
    
    for otherFile in otherFiles:
        organize("Others/", otherFile)

if __name__ == '__main__':
    wintoaster = WindowsToaster('Organizer Folder')
    while(1):
        files = os.listdir(path)
        verify()
        time.sleep(2)
