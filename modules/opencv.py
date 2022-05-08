import tkinter as tk
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

import cv2

class qrbarcode:
    def __init__(self, inputdata = None, inputype = None):
        self.__qrbarcodedata = inputdata
        self.__qrbarcodetype = inputype

    def getData(self):
        return self.__qrbarcodedata

    def getType(self):
        return self.__qrbarcodetype

class cameraScanner:
    def __init__(self, window):
        # Obtenemos ventana
        self.window = window

        # Camara
        self.cam = cv2.VideoCapture(0)

        # Control de excepcion para no abrir el escaner al no existir camara
        if not self.cam.isOpened():
            raise Exception("No es posible abrir la camara", 0)
        # Resolucion de camara
        #self.width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        #self.height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width_height = 360

        #self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.width_height)
        #self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.width_height)

        # Intervalo de actualizacion
        self.interval = 10 # Interval in ms to get the latest frame

        # Create canvas for image frame
        #self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas = tk.Canvas(self.window, width=self.width_height, height=self.width_height)
        self.canvas.grid(row=0, column=0)
        # Update image on canvas
#        self.update_image()

    def decoder(self):
        barcodeData = None
        barcodeType = None

        # Lo convierte en grayscale_ el FPS captado
        gray_img = cv2.cvtColor(self.frame, 0)
        # Decidificador de codigo de barras
        barcode = decode(gray_img)

        # Obteniendo la informacion del objeto barcode
        for obj in barcode:
            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type

        data = qrbarcode(barcodeData, barcodeType)

        return data

    def update_image(self):
        if self.cam.isOpened():
            self.frame = self.cam.read()[1]
            # Get the latest frame and convert image format
            self.image = cv2.cvtColor(self.cam.read()[1], cv2.COLOR_BGR2RGB) # to RGB
            self.image = Image.fromarray(self.image) # to PIL format
            self.image = ImageTk.PhotoImage(self.image) # to ImageTk format

            # Update image
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

            self.data = self.decoder()


            if self.data.getType() == None:
                # Repeat every 'interval' ms
                self.window.after(self.interval, self.update_image)
            else:
                if self.cam.isOpened():
                    print("Cam Released")
                    self.cam.release()

                print("Exit window")
                self.window.quit()

        else:
            raise Exception("No es posible abrir la camara", 0)


#root = tk.Tk()
#mycamera = camera(root, cv2.VideoCapture(0))
#mycamera.update_image()
#root.mainloop()

#print(mycamera.data.getType())
