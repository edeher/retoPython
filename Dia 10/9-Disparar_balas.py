import pygame
import random

# Inicializar Pygame
pygame.init()

# Crear la Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invacion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# Variable Jugador
img_jugador = pygame.image.load("astronave.png")
jugador_x = 370
jugador_y = 520
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variable enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 150)
enemigo_x_cambio = 1
enemigo_y_cambio = 50

# Variable bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False


# Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion Enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


# Funcion Disparar Bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Loop del Juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    # pantalla.fill((205, 144, 228))

    # imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # Iterar Eventos
    for evento in pygame.event.get():

        # Evento cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                print("Izquierda")
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                print("Derecha")
                jugador_x_cambio = 1
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                print("Arriba")
                jugador_y_cambio = -1
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                print("Abajo")
                jugador_y_cambio = 1
            if evento.key == pygame.K_SPACE:
                print("Disparar Bala")
                disparar_bala(jugador_x, bala_y)

        # Evento soltar tecla
        if evento.type == pygame.KEYUP:
            # if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or
            #    evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP,
                              pygame.K_DOWN, pygame.K_a, pygame.K_d,
                              pygame.K_w, pygame.K_s):
                print("Tecla soltada")
                jugador_x_cambio = 0
                jugador_y_cambio = 0
    # Modificar posicion jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de los limites horizontales
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    jugador_y += jugador_y_cambio

    # Mantener dentro de los limites verticales
    if jugador_y <= 0:
        jugador_y = 0
    elif jugador_y >= 536:
        jugador_y = 536

    # Modificar posicion del enemigo
    enemigo_x += enemigo_x_cambio

    # Mantener dentro de los limites horizontales
    if enemigo_x <= 0:
        enemigo_x_cambio = 1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -1
        enemigo_y += enemigo_y_cambio

    # Movimiento de la bala
    if bala_visible:
        disparar_bala(jugador_x, bala_y)
        bala_y -= bala_y_cambio
    if bala_y <= 0:
        bala_y = 500
        bala_visible = False

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actuaslizar
    pygame.display.update()