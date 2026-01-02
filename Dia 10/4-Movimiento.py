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


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Loop del Juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((205, 144, 228))
    jugador_x += 0.1  # No hay movimiento aún
    jugador_y += 0.1  # No hay movimiento aún
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador(jugador_x, jugador_y)
    pygame.display.update()