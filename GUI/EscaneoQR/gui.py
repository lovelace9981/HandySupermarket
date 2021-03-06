
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from modules import cameraScanner, qrbarcode, dmlContainer, databaseSQL
import re

# CREADOR DE QR: https://es.qr-code-generator.com/

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class scannerGUI:
    def __init__(self, window):

        self.window = window

        self.window.geometry("360x800")
        self.window.configure(bg="#000000")

        # Nombre de ventana de Tkinter
        self.window.title("EscaneadorQRBar")

        self.canvas = Canvas(
            self.window,
            bg="#000000",
            height=800,
            width=360,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_texto = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_texto = self.canvas.create_image(
            180.0,
            89.0,
            image=self.image_image_texto
        )

        self.button_image_atras = PhotoImage(
            file=relative_to_assets("button_atras.png"))
        self.button_atras = Button(
            self.window,
            image=self.button_image_atras,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.finMainloop(),
            relief="flat"
        )
        self.button_atras.place(
            x=12.0,
            y=18.0,
            width=45.0,
            height=45.0
        )

        # Incializando el panel donde alojamos el video de la camara
        self.panel = Label(self.window)

        # Posicionamiento correcto de la camara
        self.panel.place(x=0, y=200)
        self.window.resizable(False, False)

        self.mycamera = cameraScanner(self.window)
        self.mycamera.update_image()
        self.window.mainloop()

        # debug
        #print(self.mycamera.data.getType())
        database = databaseSQL()

        if self.mycamera.data.getType() == "QRCODE":
            # Verificamos que sea un codigo de barras
            if bool(re.search("[0-9]{11}", self.mycamera.data.getData())):
                print("BARCODE")

                query = "SELECT *"
                table = "FROM PRODUCTOS"
                clause = "WHERE COD_BARRAS_EAN_13 = '" + self.mycamera.data.getData() + "'"

                dmlContainer = database.queryConsultas(query, table, clause)

                print(dmlContainer.getHeaderTable())
                print(dmlContainer.getBodyTable())

                # Aqui deberia ir la GUI de producto

            else: # No es codigo de barras, es un QR de pasillos estante
                print("QR PASILLOS ESTANTES")

                # sample of Join or Cartesian producto on two SQL tables
                #SELECT  PASILLOS_ESTANTES.COD_QR_PASILLO_ESTANTE, COD_BARRAS_EAN_13, DESCRIPCION, NOMBRE, PRECIO, STOCK
                #FROM PASILLOS_ESTANTES, PRODUCTOS WHERE PASILLOS_ESTANTES.COD_QR_PASILLO_ESTANTE = "CARNICERIA01" AND PASILLOS_ESTANTES.COD_QR_PASILLO_ESTANTE = PRODUCTOS.COD_QR_PASILLO_ESTANTE;

                query = "SELECT PASILLOS_ESTANTES.COD_QR_PASILLO_ESTANTE, COD_BARRAS_EAN_13, DESCRIPCION, NOMBRE, PRECIO, STOCK"
                table = "FROM PASILLOS_ESTANTES, PRODUCTOS"
                clause = "WHERE PASILLOS_ESTANTES.COD_QR_PASILLO_ESTANTE = '" + self.mycamera.data.getData() + "' AND PASILLOS_ESTANTES.COD_QR_PASILLO_ESTANTE = PRODUCTOS.COD_QR_PASILLO_ESTANTE"

                dmlContainer = database.queryConsultas(query, table, clause)

                print(dmlContainer.getHeaderTable())
                print(dmlContainer.getBodyTable())

                # Aqui deberia ir la GUI de pasillo


            # Disenio de REGEX
            # CARNICERIA01
            # PAS = Pasillo
            # 01 = Estante
            # 01234567891
            # 11111111111
