import pygame

#posicion -> (int, int)
#movimiento -> (int, int)
#visible -> bool
#estado -> (bool,bool,bool)
#isImage -> bool
#sprarray -> list[surface]
#pantalla -> surface (principal)
#imagen_actual -> surface
#rectangulo -> Rect
class cursor():
    #inicializa un objeto del tipo cursor
    def __init__(self):
        self.posicion = (0,0)
        self.movimiento = (0,0)
        self.visible = True
        self.estado = (False,False,False)
        self.isImage = False
        self.sprarray = []
        self.pantalla = None
        self.imagen_actual = None
        self.rectangulo = None

    #selecciona si la imagen del cursor es visible o no
    def visible(self,visible):
        self.visible = visible
        if self.visible: pygame.mouse.set_visible(True)
        else: pygame.mouse.set_visible(False)

    #en caso de haber imagenes, esta funcion sirve para seleccionar la pantalla sobre a cual
    #se mostraran las imagenes
    def screen(self,pantalla):
        self.pantalla = pantalla

    #agrega superficie a la lista de imagenes del cursor
    def agregar_sup(self,superficie):
        if self.isImage == False: self.isImage = True
        self.sprarray.append(superficie)

    #agrega imagen a la lista de imagenes del cursor
    def agregar_img(self,nombre,alpha = True, directorio = '../sprites/'):
        if self.isImage == False: self.isImage = True
        
        if alpha: self.sprarray.append(pygame.image.load(directorio + nombre).convert_alpha())
        else:     self.sprarray.append(pygame.image.load(directorio + nombre).convert())

    #modifica la imagen actual con la que se mostrara el cursor (en caso de haber)
    def actual(self,indice = 0):
        assert type(indice)==int and indice > -1 and self.sprarray != []
        self.imagen_actual = self.sprarray[indice]
        self.rectangulo = self.imagen_actual.get_rect()
        (self.rectangulo.left,self.rectangulo.top) = self.posicion

    #recarga los datos del cursor
    def update(self):
        self.posicion = pygame.mouse.get_pos()
        self.movimiento = pygame.mouse.get_rel()
        self.estado = pygame.mouse.get_pressed()
        
        pygame.mouse.set_visible(self.visible)

        if self.isImage:
            (self.rectangulo.left,self.rectangulo.top) = self.posicion
            if self.visible:
                self.pantalla.blit(self.imagen_actual,self.posicion)
            
            
            
            
