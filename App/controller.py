﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def initdicci():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    dicci = model.newdicc()
    return dicci

# Funciones para la carga de datos

def loadData(dicci):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(dicci)
    loadCategorias(dicci)

def loadVideos(dicci):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videofile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videofile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(dicci, video)


def loadCategorias(dicci):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    Categoryfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(Categoryfile, encoding='utf-8'))
    for category in input_file:
        model.addCategoria(dicci, category )
   
   
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo