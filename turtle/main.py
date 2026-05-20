import turtle  # Importa la librería turtle para crear gráficos y dibujos

# Lista de colores que se usarán para cambiar el color del lápiz
colores = ['cyan', 'pink', 'green', 'purple']

# Crea un objeto Turtle (la "tortuga" que dibuja)
t = turtle.Turtle()

# Ajusta la velocidad de dibujo al máximo (0 = velocidad más rápida)
t.speed(0)

# Cambia el color del fondo de la ventana a negro
turtle.bgcolor('black')

# Bucle que se ejecuta 360 veces
for x in range(360):

    # Cambia el color del lápiz usando los colores de la lista
    # x % 4 devuelve valores entre 0 y 3 para recorrer los 4 colores repetidamente
    t.pencolor(colores[x % 4])

    # Cambia el grosor del lápiz gradualmente
    # x // 100 realiza división entera:
    # de 0–99 -> ancho 1
    # de 100–199 -> ancho 2
    # de 200–299 -> ancho 3
    # de 300–359 -> ancho 4
    t.width(x // 100 + 1)

    # La tortuga avanza una distancia igual al valor actual de x
    # La distancia aumenta en cada iteración
    t.forward(x)

    # Gira la tortuga 45 grados hacia la izquierda
    t.left(45)

# Mantiene abierta la ventana hasta que el usuario la cierre
turtle.done()