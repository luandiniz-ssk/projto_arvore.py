import turtle
# turtle.tracer(False)
import math
import time

# --------- Parâmetros principais ----------
DEPTH = 15          # profundidade (7–10 dá um visual legal)
ANGLE = 22         # ângulo de ramificação (20–30)
SHRINK = 0.72      # quanto o galho diminui a cada nível (0.68–0.75)
TRUNK = 140        # tamanho do tronco
SPEED = 0         # 0 = mais rápido; 1..10 mais devagar
PAUSE = 0          # segundinhos entre segmentos (ex.: 0.001)
# -----------------------------------------

t = turtle.Turtle(visible=False)
turtle.colormode(255)
t.speed(0)
# t  = turtle.Turtle(visible=False)
# t.hideturtle()
# turtle.tracer(False)
# t.speed(0)
turtle.update()
t.screen.bgcolor("black")
t.pensize(12)

# posiciona tronco
t.penup()
t.setheading(90)              # apontando para cima
t.goto(0, -250)
t.pendown()

def lerp(a, b, t):
    return a + (b - a) * t

def set_color(depth, max_depth):
    # transição marrom -> verde conforme sobe a árvore
    k = 1 - depth / max_depth
    r = int(lerp(139, 34, k))   # marrom escuro -> verde
    g = int(lerp(69, 139, k))
    b = int(lerp(19, 34, k))
    t.pencolor(r, g, b)

def set_width(depth):
    t.pensize(max(1, int(12 * (0.75 ** (DEPTH - depth)))))

def draw_branch(length, depth):
    set_color(depth, DEPTH)
    set_width(depth)

    # desenha o segmento principal
    t.forward(length)
    if PAUSE: time.sleep(PAUSE)

    if depth <= 0:
        # pontinhas com “folhas” miúdas
        return

    # ramos esquerdo e direito
    for turn in (-ANGLE, ANGLE):
        t.left(turn)
        draw_branch(length * SHRINK, depth - 1)
        t.right(turn)  # volta o heading

    # um ramo “central” leve, para coroar como um guarda-chuva
    t.left(0)
    t.right(0)  # mantém heading

    # volta para base do galho (para continuar animando o resto)
    t.backward(length)
    if PAUSE: time.sleep(PAUSE)

# desenha o tronco com marrom
t.pencolor(139, 69, 19)
t.forward(TRUNK)
draw_branch(TRUNK * SHRINK, DEPTH)
t.hideturtle()
turtle.done()
