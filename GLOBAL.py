class Detector:
    def __init__(self,ADN,detector):
        self.ADN = ADN
        self.detector = detector


    def detectar_mutante(self):
        mutacion_horizontal = self.detector_horizontal()
        mutacion_vertical = self.detector_vertical()

        if mutacion_horizontal and mutacion_vertical:
            print("Hemos encontrado mutaciones tanto horizontales y verticales!")
        elif mutacion_horizontal:
            print("Se detecto una mutacion Horizontal! \nNo se encontraron mutaciones verticales")
        elif mutacion_vertical:
            print("Se detecto una mutacion vertical! \nNo se encontraron mutacion Horizontales")
        else:
            print("No se encontro ningun tipo de Mutacion")
        


    def detector_horizontal(self):
        for fila in self.ADN:
            contador_consecutivo = 1 #El contador empiezaen uno por la primer letra
            for i in range(1, len(fila)):
                if fila[i] == fila[i-1]: #Vemos si lo numeros son iguales para sumarle 1 a contador_consecutivo, si llega a 4 automaticamente lanza un aviso de que se encontro una mutacion
                    contador_consecutivo += 1
                    if contador_consecutivo == self.detector:
                        print(f"Se detectaron 4 '{fila[i]}' consecutivos en la fila: {fila}")
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
                        print(f"Se Encontraron {self.detector} {self.ADN[fila][columnas]} consecutivas en la columna: {columnas+1}")
                        return True
                else:
                    contador_consecutivo = 0
        return False

ADN = Detector(["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"], 4)
ADN.detectar_mutante()