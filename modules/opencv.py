import cv2
import numpy as np
from pyzbar.pyzbar import decode

class qrbarcode:
    __qrbarcodedata
    __qrbarcodetype

    def __init__(self, inputdata, inputype):
        self.__qrbarcodedata = inputdata
        self.__qrbarcodetype = inputype

    def getData(self):
        return self.__qrbarcodedata

    def getType(self):
        return self.__qrbarcodetype


class camera:
    # Private attribute of camera
    __cap
    # Singleton instaciation
    __instance = None

    # https://es.stackoverflow.com/questions/79446/cu%C3%A1l-es-la-diferencia-entre-staticmethod-y-classmethod-en-python
    @staticmethod
    def getInstance():
        # Camara
        if camera.__instance == None:
            camera()

        return camera.__instance

    def __init__(self):
            if camera.__instance != None
                raise Exception("This class camera is a Singleton Class")
            else:
                # Asignamos la camara
                self.__cap = cv2.VideoCapture(0)
                camera.__instance = self

    # Retorna un objeto del tipo qrbarcode
    def decoder(self, image):
        # Lo convierte en grayscale_ el FPS captado
        gray_img = cv2.cvtColor(image,0)
        # Decidificador de codigo de barras
        barcode = decode(gray_img)

        # Obteniendo la informacion del objeto barcode
        for obj in barcode:
            barcodeData = obj.datadecode("utf-8")
            barcodeType = obj.type

        return qrbarcode(barcodeData, barcodeType)

    # Necesita un bucle de ventana en Tkinter para ir captando los Frames
    # Necesita un boton de parada automatico en el caso de que no lea datos nulos
    # Retorna tambien el dato del tipo de qrbarcode
    def scanner(self):
        # Va llamando al frame
        ret, frame = cap.read()

        #Imprime la imagen
        cv2.imshow('Image', frame)

        returnbarcodedata = decoder(frame)

        # DEBUG ZONE
        print(returnbarcodedata.getData + " " + returnbarcodedata.getType)

        # Le manda al decodificador el Frame Per Second
        return returnbarcodedata
