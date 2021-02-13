import time

def projectdownload():
    # Data extraction
    print('What is the size file? (in M = MegaByte, G = GigaByte)')
    sizeFile = input('-> ')
    sizeFile = sizeFile.lower()
    print('What is the your internet speed? (in MegaBite)')
    netSpeed = input('-> ')

    # MegaBite for MegaByte
    biteByteSpeed = int(netSpeed) / 8
    if biteByteSpeed == 1.0:
        biteByteSpeed = 0.9
    else:
        print('Ocorreu um erro')

    # Gigabyte to Megabyte
    if 'g' in sizeFile:
        sizeFile = sizeFile.replace(' ','')
        sizeFile = sizeFile.replace('g','')
        sizeFile = sizeFile * 1000
        sizeFile = float(sizeFile)
        print(sizeFile)

    # Calc time of download
    timeSec = float(sizeFile) / float(biteByteSpeed)

    # Calc time (in sec) for hours and minutes
    timeMin = timeSec / 60
    timeHour = timeMin / 60
    timeSec = int(timeSec)
    timeMin = int(timeMin)
    timeHour = int(timeHour)

    # Show data
    print(f'The download time of {sizeFile} Megabyte is: \n {timeHour} horas; \n {timeMin} Minutos; \n {timeSec} Segundos.')

    time.sleep(5.0)

projectdownload()