
import argparse
# 1. cargar los dataloaders (importando la biblioteca previamente creada)

parser = argparse.ArgumentParser()
parser.add_argument("-i")
argumentos = parser.parse_args()
print(argumentos)
# 2. cargar los modelos DL previamente creados en la biblioteca

# 3. si es para entrenar, efectuar el entrenamiento

# 4. si es solo para inferencias recibir datos de entrada y generar las salidas
