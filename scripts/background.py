import pygame
import settings

#imagen -> surface
#pantalla -> surface (principal)
#posicion -> tupla
#directorio -> str
#nombre -> str
class background:
    #__init__: self surface str str bool tupla -> background
    #crea objeto del tipo background, se recomienda tener solo uno de estos por pantalla
    def __init__(self,pantalla,nombre,directorio = '../bg/',alpha = False, posicion=(0,0)):
        #imagen para ser utilizada
        if alpha:
            self.imagen = pygame.image.load(directorio + nombre).convert_alpha()
        else:
            self.imagen = pygame.image.load(directorio + nombre).convert()
        self.pantalla = pantalla
        self.posicion = posicion
        
        #nombre y directorio del archivo para ser identificada
        self.directorio = directorio
        self.nombre = nombre

    #move: self int int -> None
    #mueve el background tantas posiciones en x como en y (simialr a move_ip de rectangulos)
    def move(self,x,y):
        assert type(x)==type(y)==int
        self.posicion[0] += x
        self.posicion[1] += y
        
    #move_to: self int int -> None
    #mueve la imagen hacia la posicion indicada
    def move_to(self,x,y):
        assert type(x)==type(y)==int
        self.posicion = (x,y)

    #update: self -> None
    #funcion que recarga la imagen en la pantalla asiganada al objeto
    def update(self):
        self.pantalla.blit(self.imagen,self.posicion)
