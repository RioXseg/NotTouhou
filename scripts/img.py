import pygame

#imagen_actual -> surface
#sprarray -> list(surface)
#posicion -> tupla
#rectangulo -> Rect
#pantalla -> surface (principal)
#directorio -> str
class img(pygame.sprite.Sprite):
    def __init__(self,pantalla = None,directorio = '../img/', posicion=(0,0)):
        pygame.sprite.Sprite.__init__(self)

        self.sprarray = []
        self.imagen_actual = None
        self.rectangulo = None
        self.posicion = posicion
        self.pantalla = pantalla
        self.directorio = directorio

    #agregar_sup: self surface -> None
    #agrega una superficie a la lista de sprites del boton
    def agregar_sup(self,superficie):
        self.sprarray.append(superficie)

    #screen: self surface -> None
    #modifica el parametro self.pantalla, sin el cual no se podra hacer update
    def screen(self,pantalla):
        self.pantalla = pantalla

    #agregar_img: self, str bool str -> None
    #lo mismo que la anterior solo que pedimos parametros distintos
    def agregar_img(self,nombre,alpha = True, directorio = '../img/'):
        if alpha:
            self.sprarray.append(pygame.image.load(directorio + nombre).convert_alpha())
        else:
            self.sprarray.append(pygame.image.load(directorio + nombre).convert())

    #cambiar_actual: self int -> None
    #cambia la imagen actual del objeto por otra que este en la lista de sprites del objeto
    def actual(self,indice = 0):
        assert type(indice)==int and indice > -1
        self.imagen_actual = self.sprarray[indice]
        self.rectangulo = self.imagen_actual.get_rect()
        (self.rectangulo.left,self.rectangulo.top) = self.posicion

    #move: self int int -> None
    #mueve el boton tantas posiciones en x como en y (simialr a move_ip de rectangulos)
    def move(self,x,y):
        assert type(x)==type(y)==int
        self.posicion[0] += x
        self.posicion[1] += y
        (self.rectangulo.left,self.rectangulo.top) = self.posicion
        
    #move_to: self int int -> None
    #mueve la imagen hacia la posicion indicada
    def move_to(self,x,y):
        assert type(x)==type(y)==int
        self.posicion = (x,y)
        (self.rectangulo.left,self.rectangulo.top) = self.posicion

    #update: self -> None
    #actualiza la imagen del boton en la pantalla principal
    def update(self):
        self.pantalla.blit(self.imagen_actual,self.posicion)          #la posicion del boton se configura con el rectangulo
        
 
