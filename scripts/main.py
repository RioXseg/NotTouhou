# Modulos
import pygame
import settings
import os
import s1

#clases
import background
import button
import cursor
import bgm

#funciones

#funcion principal
def main():

    #creacion de objetos para el programa
    bg = background.background(settings.pantalla,'00.jpg')

    #configuramos boton principal
    boton = button.button(settings.pantalla,posicion=(40,450))
    boton.agregar_img('00.png')
    boton.agregar_img('01.png')
    boton.agregar_img('02.png')
    boton.actual(0)
    
    mouse = cursor.cursor()
    bgmusic = bgm.bgm("001.mp3")
    running = True
    directorio = os.getcwd()

    #acciones de uso unico
    bgmusic.play()

    #bucle principal
    while running:
        #variables que se comprueban cada bucle
            

        #lista que contiene todos los eventos que se ejecutaron
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    if boton.rectangulo.left < mouse.posicion[0] < boton.rectangulo.right and boton.rectangulo.top < mouse.posicion[1] < boton.rectangulo.bottom:
                        s1.main()
                        running = False
                        
                        
            if evento.type == pygame.QUIT:
                running = False


        #opciones de posicion del mouse
        if mouse.posicion[0] > boton.rectangulo.right or \
           mouse.posicion[0] < boton.rectangulo.left or \
           mouse.posicion[1] > boton.rectangulo.bottom or \
           mouse.posicion[1] < boton.rectangulo.top:
            boton.actual(0)
        else:
            if mouse.estado[0]:
                boton.actual(2)
            if not(mouse.estado[0]):
                boton.actual(1)

        #Actualizamos posicion de las cosas
        bg.update()
        boton.update()
        mouse.update()
        if not(running): bgmusic.stop()
        
        #actualizamos la pantalla
        pygame.display.flip()
        settings.reloj.tick(60)                     #60 frames por segundo
    

#esto es lo que pasa cuando se abre el programa, sirve para definir cosas generales.
pygame.init()
main()
pygame.display.quit()
