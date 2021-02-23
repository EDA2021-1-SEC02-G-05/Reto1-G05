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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newdicc():
    """
    Inicializa el catálogo de los videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorias ,
    Retorna el catalogo inicializado.
    """
    dicci = {'videos': None,
               'categorias': None,
              }

    dicci['videos'] = lt.newList()
    dicci['categorias'] = lt.newList('SINGLE-LINKED')

    return dicci


# Funciones para agregar informacion al catalogo


def addVideo(dicci, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(dicci['videos'], video)



def addCategoria(dicci, categoria):
    # Se adiciona la categoria a la lista de categorias
    lt.addLast(catalog['categorias'], categoria)









# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento