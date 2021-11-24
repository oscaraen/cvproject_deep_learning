"""
Script para la exploración inicial de los archivos en el dataset

Version 1 creado el 23 nnoviembre de 2021

autor: Oscar Andrés Martínez S.

"""
from utilidades_dataset import *

# funciones para la lectura del dataset
import os
from pathlib import Path

# recorrido de las imágenes por una carpeta

class ExploradorCarpetas:
    def __init__(self, ruta):
        self.rutabase = ruta
        self.leer_carpetas_directorio(ruta)

    def leer_carpetas_directorio(self, directorio_base):
        self.resultado = os.walk(directorio_base)
        self.subcarpetas = [x[0] for x in self.resultado]
        self.resultado = os.walk(directorio_base)


    def calcular_archivos_carpeta(self):
        # 1. tomar el generador y leer uno a uno los registros
        lista_archivos_subcarpetas = []
        next(self.resultado) # tomar una entrada de un generador
        for registro in self.resultado:
            lista_archivos_subcarpetas.append(len(registro[2]))
        print(lista_archivos_subcarpetas)
        print("el promedio de imgs por carpeta es {}".format(sum(lista_archivos_subcarpetas)/len(lista_archivos_subcarpetas)))
        # el registro trae, la carpeta y una lista con los ficheros en la carpeta

    def crear_diccionario_rutas(self):
        """
        tome la carpeta base y a partir de los ficheros encontrados
        cree un diccionario con un número de clase de 0 a 315
        y como valor una lista con las rutas de las imágenes que pertenecen
        a esa clase
        """
        self.resultado = os.walk(self.rutabase)
        llaves = next(self.resultado)[1] # lista de carpetas
        llaves_enumeradas = enumerate(llaves) # enumeración de carpetas
        lista_rutas_clase = []
        for registro in self.resultado:
            lista_rutas_clase.append(registro[2])

        diccionario_etiquetas_archivos = {}
        for llave, valor in zip(llaves, lista_rutas_clase):
            diccionario_etiquetas_archivos[llave] = valor

        return diccionario_etiquetas_archivos

    def visualizar_img(self, ruta_img):
        # todo: terminar este método
        pass

    def obtener_ruta_completa_imgs(self):
        # leer la lista de archivos y construir la ruta completa
        # para su acceso
        # todo: terminar este método
        pass

if __name__=="__main__":
    # Pruebas de funcionamiento durante el desarrollo
    explorador = ExploradorCarpetas(RUTA_CARPETA_TRAIN)
    #explorador.calcular_archivos_carpeta()
    explorador.crear_diccionario_rutas()





