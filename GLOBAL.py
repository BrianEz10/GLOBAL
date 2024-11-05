class Detector:
    def __init__(self,ADN,detector):
        self.ADN = ADN
        self.detector = detector


    def detectar_mutante(self):
        if self.detector_horizontal():
            return print("Se detecto una mutacion ")
        else: print("No se detectaron mutaciones horizontales")

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


ADN = Detector(["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"], 4)
ADN.detectar_mutante()