import pygame

text = input('Nome da musica: ')

pygame.init()
pygame.mixer.music.load(text)
pygame.mixer.music.play()

print('S para parar.')
text2 = input('-> ')

if text2 == 'S':
    pygame.mixer.stop()
else:
    pygame.event.wait()
