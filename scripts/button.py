import pygame
import img


class button(img.img):
    #__init__: self surface str str str str tupla -> boton
    #crea objeto del tipo boton para luego ser usado
    def __init__(self,pantalla = None,posicion = (0,0)):
        img.img.__init__(self)
        self.pantalla = pantalla
        self.posicion = posicion
        
