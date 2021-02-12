import time

# Data extraction
print('What is the size file? (in MegaByte)')
sizeFile = int(input('-> '))
print('What is the your internet speed? (in MegaBite)')
netSpeed = int(input('-> '))

# MegaBite for MegaByte
biteByteSpeed = (netSpeed) / 8
if biteByteSpeed == 1.0:
    biteByteSpeed = 0.9
else:
    pass

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