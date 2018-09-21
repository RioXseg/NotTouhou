#modulos
import pygame
import settings
import os

#clases
import background
import button
import cursor
import bgm

#funciones
pygame.init()

#funcion principal
def main():

    #creacion de objetos para el programa
    bg = background.background(settings.pantalla,'01.png',alpha = True)
    mouse = cursor.cursor()
    bgmusic = bgm.bgm("003.mp3")
    running = True
    directorio = os.getcwd()


    #acciones de uso unico
    bgmusic.play(inicio = 2.0)

    #bucle principal
    while running:
        #variables que se comprueban cada bucle


        #lista de los eventos que se ejecutaron
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        #actualizacion de objetos en pantalla
        bg.update()
        mouse.update()
        if not(running): bgmusic.stop()
    
        #actualizamos la pantalla
        pygame.display.flip()
        settings.reloj.tick(60)

