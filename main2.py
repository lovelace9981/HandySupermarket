import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decoder(image):
    # Lo convierte en grayscale_
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        print("Barcode: "+ barcodeData + " | Type: " + barcodeType)

# Inicio de la camara
cap = cv2.VideoCapture(0)

#Bucle de ventana
while True:
    # Va llamando al frame
    ret, frame = cap.read()
    # Le manda al decodificador el Frame Per Second
    decoder(frame)

    #Imprime la imagen
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
