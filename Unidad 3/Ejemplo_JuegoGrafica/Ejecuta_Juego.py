import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QTime
import random as rnd
import Plantilla_Juego as grafica

import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_action.clicked.connect(self.action)

        self.btn_arriba.clicked.connect(self.arriba)
        self.btn_izquierda.clicked.connect(self.izquierda)
        self.btn_centro.clicked.connect(self.centro)
        self.btn_derecha.clicked.connect(self.derecha)
        self.btn_abajo.clicked.connect(self.abajo)

        ################################################################################

        self.xMax = 5
        self.xMin = -5
        self.yMax = 5
        self.yMin = -5


        #################################################################################
        #                Jugador  Computadora   computadora2 computadora3 computadora4
        self.personajes = [[0, 0], [0, 0],      [0,0],        [0, 0],       [0, 0], ]

        ##############################################

        self.limpiar()

        #inicializamos el cronometro


    # Área de los Slots
    def action(self):
        if self.btn_action.text() == "INICIAR":
            self.btn_action.setText("DETENER")

            #jugador
            self.personajes[0] = [0, 0] #vuelve al jugar al centro

            import random as rnd
            #computadora
            self.personajes[1] = [rnd.randrange(self.xMin, self.xMax), rnd.randrange(self.yMin, self.yMax)]
            self.personajes[2] = [rnd.randrange(self.xMin, self.xMax), rnd.randrange(self.yMin, self.yMax)]
            self.personajes[3] = [rnd.randrange(self.xMin, self.xMax), rnd.randrange(self.yMin, self.yMax)]
            self.personajes[4] = [rnd.randrange(self.xMin, self.xMax), rnd.randrange(self.yMin, self.yMax)]
            self.graficar()



        else:
            self.btn_action.setText("INICIAR")
            self.limpiar()
            #se detendra el timepo al terminar el juego




    def arriba(self):#     v  => valor de y
        self.personajes[0][1] = self.personajes[0][1] + 1
        self.limpiar()
        self.graficar()

    def izquierda(self):#  v  => valor de x
        self.personajes[0][0] -= 1
        self.limpiar()
        self.graficar()

    def centro(self):
        self.personajes[0][0] = 0
        self.personajes[0][1] = 0
        self.limpiar()
        self.graficar()

    def derecha(self):#    v  => valor de x
        self.personajes[0][0] += 1
        self.limpiar()
        self.graficar()

    def abajo(self):#      v  => valor de y
        self.personajes[0][1] -= 1
        self.limpiar()
        self.graficar()

    def limpiar(self):
        plt.cla() #BORRA_TODO EL GRAFICO

        x = [i for i in range(self.xMin, self.xMax + 1)] #GENERA LOS TICKS
        y = [i for i in range(self.yMin, self.yMax + 1)] #GENERA LOS TICKS

        # Generar coordenadas aleatorias para la computadora 1
        x_computadora1 = rnd.randrange(self.xMin, self.xMax)
        y_computadora1 = rnd.randrange(self.yMin, self.yMax)

        # Asegurarse de que las coordenadas estén dentro de los límites
        x_computadora1 = max(self.xMin, min(x_computadora1, self.xMax))
        y_computadora1 = max(self.yMin, min(y_computadora1, self.yMax))

        # Asignar las coordenadas corregidas a la computadora 1
        self.personajes[1] = [x_computadora1, y_computadora1]

        # Generar coordenadas aleatorias para la computadora 2
        x_computadora2 = rnd.randrange(self.xMin, self.xMax)
        y_computadora2 = rnd.randrange(self.yMin, self.yMax)

        # Asegurarse de que las coordenadas estén dentro de los límites
        x_computadora2 = max(self.xMin, min(x_computadora2, self.xMax))
        y_computadora2 = max(self.yMin, min(y_computadora2, self.yMax))

        # Asignar las coordenadas corregidas a la computadora 2
        self.personajes[2] = [x_computadora2, y_computadora2]

        # Generar coordenadas aleatorias para la computadora 3
        x_computadora1 = rnd.randrange(self.xMin, self.xMax)
        y_computadora1 = rnd.randrange(self.yMin, self.yMax)

        # Asegurarse de que las coordenadas estén dentro de los límites
        x_computadora1 = max(self.xMin, min(x_computadora1, self.xMax))
        y_computadora1 = max(self.yMin, min(y_computadora1, self.yMax))

        # Asignar las coordenadas corregidas a la computadora 3
        self.personajes[3] = [x_computadora1, y_computadora1]

        # Generar coordenadas aleatorias para la computadora 4
        x_computadora1 = rnd.randrange(self.xMin, self.xMax)
        y_computadora1 = rnd.randrange(self.yMin, self.yMax)

        # Asegurarse de que las coordenadas estén dentro de los límites
        x_computadora1 = max(self.xMin, min(x_computadora1, self.xMax))
        y_computadora1 = max(self.yMin, min(y_computadora1, self.yMax))

        # Asignar las coordenadas corregidas a la computadora 4
        self.personajes[4] = [x_computadora1, y_computadora1]

        self.ax.set_xticks(y)
        self.ax.set_yticks(y)

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)

        plt.grid(True)  #CUADRICULA

        self.canvas.draw() #DIBUJAR EL GRAFICO


    def graficar(self):

        #POSICIONA AL USUARIO EN LA GRAFICA
        self.ax.plot(self.personajes[0][0], self.personajes[0][1],
                     marker="o",  # o . *  x   1
                     markersize=15,
                     markerfacecolor="black",  # color interno del marcador
                     markeredgewidth=6,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        #POSICIONA A LA COMPUTADORA EN EL GRAFICO
        self.ax.plot(self.personajes[1][0], self.personajes[1][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="red",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        # POSICIONA A LA COMPUTADORA2 EN EL GRAFICO
        self.ax.plot(self.personajes[2][0], self.personajes[2][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="red",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )
        # POSICIONA A LA COMPUTADORA3 EN EL GRAFICO
        self.ax.plot(self.personajes[3][0], self.personajes[3][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="red",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )
        # POSICIONA A LA COMPUTADORA4 EN EL GRAFICO
        self.ax.plot(self.personajes[4][0], self.personajes[4][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="red",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )
        # Mover la computadora 1 lejos del jugador
        self.mover_computadora(self.personajes[1])

        # Mover la computadora 2 lejos del jugador
        self.mover_computadora(self.personajes[2])

        # Mover la computadora 3 lejos del jugador
        self.mover_computadora(self.personajes[3])

        # Mover la computadora 4 lejos del jugador
        self.mover_computadora(self.personajes[4])

        self.canvas.draw() #DIBUJA EL GRAFICO

    def mover_computadora(self, computadora):
            jugador_x, jugador_y = self.personajes[0]
            computadora_x, computadora_y = computadora

            # Calcular la dirección del jugador desde la computadora
            dx = jugador_x - computadora_x
            dy = jugador_y - computadora_y

            # Mover la computadora en la dirección opuesta al jugador
            computadora[0] -= dx
            computadora[1] -= dy

        #COMPRUEBA CADA QUE SE GRAFICA SI EL USUARIO ALCANZO A LA COMPUTADORA
        #SI LAS COORDENADAS DE AMBOS ESTAN EN LA MISMA POSICION, ENTONCES EL USUARIO ALCANZO
        # A LA COMPUTADORA.. 
            if  self.personajes[0][0] == self.personajes[1][0] and self.personajes[0][1] == self.personajes[1][1] or\
                self.personajes[0][0] == self.personajes[2][0] and self.personajes[0][1] == self.personajes[2][1]or\
                self.personajes[0][0] == self.personajes[3][0] and self.personajes[0][1] == self.personajes[3][1]or\
                self.personajes[0][0] == self.personajes[4][0] and self.personajes[0][1] == self.personajes[4][1]:
                self.limpiar()
                m = QtWidgets.QMessageBox()
                m.setText("Has Ganado")
                m.exec_()
                self.btn_action.setText("INICIAR")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
