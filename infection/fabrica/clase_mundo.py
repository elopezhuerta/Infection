import numpy as np
class Mundo:
    # Atributos que no puede cambiar
    color = "azul"
    def __init__(self, n_columnas, n_filas):
        self.numero_columnas = n_columnas
        self.numero_filas = n_filas

        self.mapa = np.zeros((n_filas,n_columnas), dtype=int)

    def ocupacion_inicial(self,ocupacion):

        numero_celdas_ocupadas = int(ocupacion * self.numero_columnas * self.numero_filas)
        
	aux_lista = []
	for ii in range(self.numero_filas):
	    for jj in range(self.numero_columns):
	    aux_lista.append([ii,jj])
	np.random.shuffle(aux_lista)

	for kk in range(self.numero_celdas_ocupadas):
	    self.mapa[aux_lista[kk]]=1

