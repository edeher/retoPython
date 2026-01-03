import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crear la Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invacion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# Agregar Sonido de Fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Variable Jugador
img_jugador = pygame.image.load("astronave.png")
jugador_x = 370
jugador_y = 520
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variable enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for i in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)


# Variable bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

# Puntaje
puntaje = 0
fuente = pygame.font.Font('OCRAEXT.TTF', 32)
texto_x = 10
texto_y = 10


# Funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion Jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion Enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Funcion Disparar Bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Detectar Colision
def hay_colision(x_1, y_1, x_2, y_2):
    operacion1 = (x_1 - x_2) ** 2
    operacion2 = (y_1 - y_2) ** 2
    distancia = math.sqrt(operacion1 + operacion2)
    if distancia < 27:
        return True
    else:
        return False


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
                # Velocidad a la Izquierda
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                print("Derecha")
                # Velocidad a la Derecha
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                print("Arriba")
                jugador_y_cambio = -1
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                print("Abajo")
                jugador_y_cambio = 1
            if evento.key == pygame.K_SPACE:
                print("Disparar Bala")
                mixer.Sound("disparo.mp3").play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

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
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final = fuente.render("GAME OVER", True, (255, 255, 255))
            pantalla.blit(texto_final, (300, 250))
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    # Mantener dentro de los limites horizontales
        if enemigo_x[e] <= 0:
            # Velocidad positiva
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            # Velocidad negativa
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]
    # DETECTAR COLISION
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            mixer.Sound("golpe.mp3").play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(f"Puntaje: {puntaje}")
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 150)
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    # Actuaslizar
    pygame.display.update()
