import pygame
import sys
import random
import time  # Importa el módulo time para medir el tiempo

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Esquiva los Objetos")

# Colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)

# Jugador (más pequeño)
jugador = pygame.Rect(175, 550, 30, 30)

# Velocidad del jugador (reducida)
velocidad_jugador = 1

# Lista de objetos
objetos = []

# Velocidad de los objetos (lenta, dividida por 5)
velocidad_objetos = 1.5

# Temporizador para agregar objetos (cada 2 segundos)
temporizador_objetos = 0

# Puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Tiempo inicial
tiempo_inicial = time.time()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jugador.left > 0:
        jugador.move_ip(-velocidad_jugador, 0)
    if keys[pygame.K_RIGHT] and jugador.right < 400:
        jugador.move_ip(velocidad_jugador, 0)

    # Crear objetos aleatorios
    temporizador_objetos += 1
    if temporizador_objetos == 240:  # Agregar un objeto cada 4 segundos (240 cuadros)
        objeto = pygame.Rect(random.randint(0, 350), 0, 20, 20)  # Objetos más pequeños
        objetos.append(objeto)
        temporizador_objetos = 0

    # Mover y eliminar objetos
    for objeto in objetos:
        objeto.move_ip(0, velocidad_objetos)
        if objeto.top > 600:
            objetos.remove(objeto)

    # Verificar colisiones entre el jugador y los objetos
    for objeto in objetos:
        if jugador.colliderect(objeto):
            pygame.quit()
            sys.exit()

    # Calcular el tiempo transcurrido
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial

    # Aumentar la puntuación en 1.3 puntos por cada segundo transcurrido
    puntuacion = int(tiempo_transcurrido * 1.3)

    # Dibuja todo en la ventana
    ventana.fill((0, 0, 0))
    pygame.draw.rect(ventana, blanco, jugador)

    for objeto in objetos:
        pygame.draw.rect(ventana, rojo, objeto)

    # Mostrar la puntuación en la pantalla
    texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, blanco)
    ventana.blit(texto_puntuacion, (10, 10))

    pygame.display.update()
