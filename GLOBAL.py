class Detector:
    def __init__(self,ADN,detector):
        self.ADN = ADN
        self.detector = detector
        self.base = []
        self.posicion_mutador = ""

    def detectar_mutante(self):
        mutacion_horizontal = self.detector_horizontal()
        mutacion_vertical = self.detector_vertical()
        mutacion_diagonal = self.detector_diagonal()

        if mutacion_horizontal and mutacion_vertical and mutacion_diagonal:
            print("Hemos encontrado mutaciones tanto horizontales, verticales y Diagonales!")
        elif mutacion_horizontal:
            print("Se detecto una mutacion Horizontal! \nNo se encontraron mutaciones verticales ni diagonales")
        elif mutacion_vertical:
            print("Se detecto una mutacion vertical! \nNo se encontraron mutacion Horizontales ni diagonales")
        elif mutacion_diagonal:
            print("Se encontro una mutacion Diagonal! \nNo se encontraron mutaciones horizontales ni verticales")
        else:
            print("No se encontro ningun tipo de Mutacion")
        


    def detector_horizontal(self):

        for fila in self.ADN:
            contador_consecutivo = 1 #El contador empiezaen uno por la primer letra
            for i in range(1, len(fila)):
                if fila[i] == fila[i-1]: #Vemos si lo numeros son iguales para sumarle 1 a contador_consecutivo, si llega a 4 automaticamente lanza un aviso de que se encontro una mutacion
                    contador_consecutivo += 1
                    if contador_consecutivo == self.detector:
                        self.base = [fila[i],fila[i],fila[i],fila[i]]
                        self.posicion_mutador = "Horizontal"
                        return True
                else:
                    contador_consecutivo = 1 #En caso de que no sean iguales las letras se reinicia contador a 0

        return False
    
    def detector_vertical(self):
        num_columnas = len(self.ADN[0])
        for columnas in range(num_columnas):
            contador_consecutivo = 1
            for fila in range(1, len(self.ADN)):
                if self.ADN[fila][columnas] == self.ADN[fila-1][columnas]:
                    contador_consecutivo += 1
                    if contador_consecutivo == self.detector:
                        self.base = [self.ADN[fila][columnas]] * self.detector
                        self.posicion_mutador = "Vertical"
                        return True
                else:
                    contador_consecutivo = 0
        return 
    
    def detector_diagonal(self):
        numero_filas = len(self.ADN)
        numero_columnas = len(self.ADN[0])

        for fila in range(numero_filas - 3): 
            for columna in range(numero_columnas - 3):
                contador = 1 
                for numerito in range(1, 4):
                    if self.ADN[fila + numerito][columna + numerito] == self.ADN[fila + numerito - 1][columna + numerito - 1]:
                        contador += 1
                        if contador == self.detector:
                            self.base = [self.ADN[fila + numerito][columna + numerito]] * self.detector 
                            self.posicion_mutador = "Diagonal"
                            return True
                    else:
                        contador = 0



class Mutador:
    def __init__(self, base_nitrogenada):
        self.base_nitrogenada = base_nitrogenada


    def crear_mutante(self):
        pass


ADN = Detector(["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"], 4)
ADN.detectar_mutante()
base_nitrogenada =  []
posicion_de_mutacion = ""
posicion_de_mutacion = ADN.posicion_mutador
if ADN.base:
    base_nitrogenada.append(ADN.base)
print(base_nitrogenada)
print(posicion_de_mutacion)

coso = Mutador(base_nitrogenada,)