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




# Advanced
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decoder(image):
    # Lo convierte en grayscale_
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)

        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)

# Inicio de la camara
cap = cv2.VideoCapture(0)

#Bucle de ventana
while True:
    # Va llamando al frame
    ret, frame = cap.read()
    decoder(frame)

    #Imprime la imagen
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
