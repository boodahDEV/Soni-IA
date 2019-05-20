import retro
import pygame
import os
from pygame.locals import *


video_size = 1, 1
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
screen = pygame.display.set_mode(video_size)

env.reset()

done = False
def key_action():
    keys=pygame.key.get_pressed()
    key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    if keys[K_LEFT]:
        key[6] = 1
    if keys[K_UP]:
        key[0] = 1
    if keys[K_RIGHT]:
        key[7] = 1
    if keys[K_DOWN]:
        key[5] = 1
    return key


archivo = open("data_game.csv", "a")
while not done:
    img = env.render()
    screen = pygame.display.set_mode(video_size)
    pygame.display.set_caption(str(img))
    #pygame.display.update()
    action = key_action()
    ob, rew, done, info = env.step(action)
    archivo.write(str(info))
    archivo.write(";")
    archivo.write(str(action))
    archivo.write(";")
    archivo.write(str(rew))
    archivo.write(";") #columnas
    archivo.write("\n")
    #print("Action ", action, "Reward ", rew)
