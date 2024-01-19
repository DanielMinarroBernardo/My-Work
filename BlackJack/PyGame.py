import pygame, sys
pygame.init()

#Definir los colores para el juego
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Definir tamaño de la pantalla
size = (800,500)

#Crear ventana
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    

    #Cambiar  color fondo
    screen.fill(WHITE)
    #ZONA DE DIBUJO----------
    #pygame.draw.line(screen,GREEN,[0,100],[200,300],5)
    #pygame.draw.rect(screen, BLACK, (100,100,80,80))
    #pygame.draw.circle(screen,BLACK,(200,200), 30)

    for x in range(100,700,100):
        pygame.draw.rect(screen, BLACK,(x,230,50,50))
        pygame.draw.line(screen, GREEN,(x,0),(x,100),5)

    #ZONA DE DIBUJO----------
    #Actualizar la pantalla
    pygame.display.flip()