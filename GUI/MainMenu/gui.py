
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from modules import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class mainMenuGUI:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("360x800")
        self.window.configure(bg="#000000")

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
        self.button_image_1 = PhotoImage(
          file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
          image=self.button_image_1,
          borderwidth=0,
          highlightthickness=0,
          # Ejecución de comandos al hacer click
          command=lambda: print("button 1 clicked"),
          relief="flat"
        )
        self.button_1.place(
          x=34.0,
          y=613.0,
          width=290.0,
          height=64.0
        )

        self.button_image_2 = PhotoImage(
          file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
          image=self.button_image_2,
          borderwidth=0,
          highlightthickness=0,
          # Ejecución de comandos al hacer click
          command=lambda: print("button_2 clicked"),
          relief="flat"
        )
        self.button_2.place(
          x=34.0,
          y=544.0,
          width=290.0,
          height=61.0
        )

        self.button_image_3 = PhotoImage(
          file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
          image=self.button_image_3,
          borderwidth=0,
          highlightthickness=0,
          # Ejecución de comandos al hacer click
          command=lambda: self.callScanner(),
          relief="flat"
        )
        self.button_3.place(
          x=34.0,
          y=470.0,
          width=290.0,
          height=66.0
        )

        self.image_image_1 = PhotoImage(
          file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
          181.0,
          255.0,
          image=self.image_image_1
        )
        self.window.resizable(False, False)

    def callScanner(self):
        scanner = cameraScanner()
        scanner.gui.window.mainloop()
