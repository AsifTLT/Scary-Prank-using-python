import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/User/Desktop/200 PYTHON PROJECT CHALLENGE/data/Day13/Halloween Prank using python/ratsasan.mp3')
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('C:/Users/User/Desktop/200 PYTHON PROJECT CHALLENGE/data/Day13/Halloween Prank using python/scary.mp3')
pygame.mixer.music.play()
sleep(1)
image = pygame.image.load('C:/Users/User/Desktop/200 PYTHON PROJECT CHALLENGE/data/Day13/Halloween Prank using python/scr.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(3)