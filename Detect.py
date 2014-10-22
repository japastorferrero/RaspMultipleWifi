__author__ = 'Ja'

# Captar los datos de los dispositivos cercanos en las tres frecuencias: 1, 6, 11
# Utilizando un thread para que esten activos simultaneamente
# Utilizando una lista FIFO para gestionar la informacion
# Escribiendo en la base de datos SQL con un tratamiento de la informacion

# Importaciones

import threading
from datetime import date, datetime, timedelta
# import MySQLdb
import subprocess
# import StringIO
import time



# Variables
Sensor = "0100RB"
MAC = ""
Fecha = ""
Hora = ""
Power = ""
Type = ""
DateSlot = ""
TimeSlot = ""
ListadoDetecciones = []
# Para tratamiento de la presencia
ListadoDeteccionesImp = []
# Para escribir directamente en la tabla
PresenciaMovil = []
# Control de bloqueos
lock1 = threading.Lock()
lock2 = threading.Lock()
# Fin control de bloqueos
PeriodoEscritura = 10
tiempoProceso = 2
contador = 3
# contador para mantener presencia de dispositivo


# Funciones

def Canal1():
    global ListadoDetecciones, ListadoDeteccionesImp
    while True:
        Deteccion = []
        #Ejecucicion deteccion
        #Codigo deteccion con canal 1
        with lock2:
            ListadoDetecciones.append(Deteccion)
        with lock1:
            ListadoDeteccionesImp.append(Deteccion)
        print("Tarea canal 1")
        time.sleep(1)


def Canal6():
    global ListadoDetecciones, ListadoDeteccionesImp
    while True:
        Deteccion = []
        #Ejecucicion deteccion
        #Codigo deteccion con canal 6
        with lock2:
            ListadoDetecciones.append(Deteccion)
        with lock1:
            ListadoDeteccionesImp.append(Deteccion)
        print("Tarea canal 6")
        time.sleep(1)



def Canal11():
    global ListadoDetecciones, ListadoDeteccionesImp
    while True:
        Deteccion = []
        #Ejecucicion deteccion
        #Codigo deteccion con canal 1
        with lock2:
            ListadoDetecciones.append(Deteccion)
        with lock1:
            ListadoDeteccionesImp.append(Deteccion)
        print("Tarea canal 11")
        time.sleep(1)


def EscribirMySQL():
    global PresenciaMovil, ListadoDeteccionesImp
    global DateSlot, TimeSlot
    print("Ejecutando función para escribir SQL:   ")
    with lock1:
        pass
        # Escribir todas las detecciones en una tabla
    with lock2:
        for x in PresenciaMovil:
            x[4] = x[4] + PeriodoEscritura

        # Codigo funcion utiliza PresenciaMovil
        # Codigo funcion

    # Se llama de nuevo la funcion para volverse a ejecutar

def Controlador():
    while True:
        t100 = threading.Timer(PeriodoEscritura, EscribirMySQL)
        t100.start()
        t100.join()
        print("He salido")


# Lanzar timer
t0 = threading.Thread(target=Controlador)
# Lanzar threads
t1 = threading.Thread(target=Canal1)
t2 = threading.Thread(target=Canal6)
t3 = threading.Thread(target=Canal11)
t1.start()
t2.start()
t3.start()
t0.start()
# Bucle principal


def BuclePrincipal():
    global PresenciaMovil, ListadoDetecciones
    global contador


    # Trabajo presencia y creacion de tabla


    with lock2:
        if (len(ListadoDetecciones) != 0):
            for x in ListadoDetecciones:
                if x in PresenciaMovil:
                    PresenciaMovil[PresenciaMovil.index(x)][5] = contador
                    # contador para mantener presencia
                else:
                    lista = [x[0], x[1], DateSlot, TimeSlot, 0, contador]
                    # Comprobar datos que integran esta lista
                    PresenciaMovil.append(lista)
            for y in PresenciaMovil:
                if not(y in ListadoDetecciones):
                    if y[5] > 0:
                        y[5] = y[5] -1
                    else:
                        PresenciaMovil.remove(y)
            ListadoDetecciones = []




    print("Ejecuto el proceso de tratar leer detectados ...")




    # Codigo tratamiento de presencia
    # Trabajo presencia



    # Bucle principal


while True:
    BuclePrincipal()
    time.sleep(tiempoProceso)

    # Comprobar que la pila no esta vacia

    


