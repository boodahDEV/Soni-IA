import pygame
from pygame.locals import *

def terminar():
  pygame.quit()
  sys.exit()
def esperarTeclaJugador():
  while True:
    for evento in pygame.event.get():
      if evento.type == QUIT:
        terminar()
      if evento.type == KEYDOWN:
        if evento.key == K_ESCAPE: # Quita al presionar ESCAPE
          terminar()
        return
while True:
  while True: # el ciclo del juego se mantiene mientras se este jugando
    for evento in pygame.event.get():
      if evento.type == QUIT:
        terminar()
      if evento.type == KEYDOWN:
        if evento.key == ord('z'):
          trucoReversa = True
        if evento.key == ord('x'):
          trucoLento = True
        if evento.key == K_LEFT or evento.key == ord('a'):
          moverDerecha = False
          moverIzquierda = True
        if evento.key == K_RIGHT or evento.key == ord('d'):
          moverIzquierda = False
          moverDerecha = True
        if evento.key == K_UP or evento.key == ord('w'):
          moverAbajo = False
          moverArriba = True
        if evento.key == K_DOWN or evento.key == ord('s'):
          moverArriba = False
          moverAbajo = True
      if evento.type == KEYUP:
       if evento.key == ord('z'):
          trucoReversa = False
          puntaje = 0
       if evento.key == ord('x'):
          trucoLento = False
          puntaje = 0
       if evento.key == K_ESCAPE:
          terminar()
       if evento.key == K_LEFT or evento.key == ord('a'):
         moverIzquierda = False
       if evento.key == K_RIGHT or evento.key == ord('d'):
         moverDerecha = False
       if evento.key == K_UP or evento.key == ord('w'):
         moverArriba = False
       if evento.key == K_DOWN or evento.key == ord('s'):
         moverAbajo = False
    # Mueve el jugador.
    if moverIzquierda > 0:
      ap = [0,0,0,0,0,0,1,0,0,0,0,0]
    if moverDerecha > 0 and moverIzquierda == 0:
      ap = [0,0,0,0,0,0,0,1,0,0,0,0]
pygame.display.update()