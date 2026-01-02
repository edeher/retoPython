import pygame

# Inicializar Pygame
pygame.init()

# Crear la Pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invacion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load("astronave.png")
jugador_x = 370
jugador_y = 530
jugador_x_cambio = 0
jugador_y_cambio = 0


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop del Juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((205, 144, 228))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                print("Izquierda")
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                print("Derecha")
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                print("Arriba")
                jugador_y_cambio = -0.3
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                print("Abajo")
                jugador_y_cambio = 0.3
        if evento.type == pygame.KEYUP:
            # if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or
            #    evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP,
                              pygame.K_DOWN, pygame.K_a, pygame.K_d,
                              pygame.K_w, pygame.K_s):
                print("Tecla soltada")
                jugador_x_cambio = 0
                jugador_y_cambio = 0
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio
    jugador(jugador_x, jugador_y)
    pygame.display.update()