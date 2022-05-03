import cv2
import numpy as np
from pyzbar.pyzbar import decode
from tkinter import *
from GUI import scannerGUI

# Fuentes consultadas
# https://answers.opencv.org/question/137744/python-opencv-tkinter-playing-video-help/
# https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/

# Tkinter solo admite imagenes PIL y a su vez TK
from PIL import Image, ImageTk


class qrbarcode:
    def __init__(self, inputdata, inputype):
        self.__qrbarcodedata = inputdata
        self.__qrbarcodetype = inputype

    def getData(self):
        return self.__qrbarcodedata

    def getType(self):
        return self.__qrbarcodetype


class cameraScanner:
    def __init__(self):
        # Asignamos la camara - Private attribute of camera
        self.__cam = cv2.VideoCapture(0)

        # Control de excepcion para no abrir el escaner al no existir camara
        if not self.__cam.isOpened():
            raise Exception("No es posible abrir la camara", 0)
        # Ajuste del tamanio del frame de la camara
        self.__cam.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.__cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

        # Interfaz de escaneo
        gui = scannerGUI()

        # Ventana de Tkinter
        self.window = gui.getWindow()

        # Nombre de ventana de Tkinter
        self.window.title("EscaneadorQRBar")

        # Incializando el panel donde alojamos el video de la camara
        self.panel = Label(self.window)

        # Posicionamiento correcto de la camara
        self.panel.place(x=-140, y=200)

        # Llamamos al escaner
        self.scanner()

    def __del__(self):
        if self.__cam.isOpened():
            self.__cam.release()

    # Retorna un objeto del tipo qrbarcode
    def decoder(self, image):
        barcodeData = None
        barcodeType = None

        # Lo convierte en grayscale_ el FPS captado
        gray_img = cv2.cvtColor(image, 0)
        # Decidificador de codigo de barras
        barcode = decode(gray_img)

        # Obteniendo la informacion del objeto barcode
        for obj in barcode:
            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type

        data = qrbarcode(barcodeData, barcodeType)

        return data

    # Necesita un bucle de ventana en Tkinter para ir captando los Frames
    # Retorna un dato, hasta que no retorne algo distinto a
    # Retorna tambien el dato del tipo de qrbarcode
    def scanner(self):
        if self.__cam.isOpened():
            # Obtienen los frames de la camara desde OpenCV
            ret, frame = self.__cam.read()

            # Comprueba que ret sea distinto a vacio
            if ret:
                # BGR to RGBA
                cev2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

                # RGBA CV2 TO PIL
                frame_pil = Image.fromarray(cev2image)

                # PIL to Tkinter
                frame_imgtk = ImageTk.PhotoImage(image=frame_pil)

                # Fijamos la imagen al panel de Tk
                self.panel.imgtk = frame_imgtk
                self.panel.config(image=frame_imgtk)

            returnbarcodedata = self.decoder(frame)

            if returnbarcodedata.getData() != None:
                # DEBUG ZONE
                # print(returnbarcodedata.getData())
                # print(returnbarcodedata.getType())

                # Le manda al decodificador el Frame Per Second
                return returnbarcodedata
            else:
                self.window.after(1, self.scanner)
        else:
            raise Exception("No es posible abrir la camara", 0)


# Codigo a incluir donde se llamen los modulos
#myscanner = cameraScanner()

#myscanner.window.mainloop()
