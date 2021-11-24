"""
Utilidad para obtener las particiones xtrain, xtest, ytrain, ytest

"""

from utilidades_dataset import *

train_set = ExploradorCarpetas( RUTA_CARPETA_TRAIN)
test_set =  ExploradorCarpetas( RUTA_CARPETA_TEST)
valid_set = ExploradorCarpetas( RUTA_CARPETA_VALID)


