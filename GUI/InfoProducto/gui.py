
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class productoGUI:
    def __init__(self, window):
        self.window = window

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
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            179.0,
            321.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            45.0,
            102.0,
            320.0,
            377.0,
            fill="#000000",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            95.0,
            495.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=29.0,
            y=470.0,
            width=132.0,
            height=48.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            180.0,
            422.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=29.0,
            y=397.0,
            width=302.0,
            height=48.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            180.0,
            657.5,
            image=self.entry_image_3
        )
        self.entry_3 = Text(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_3.place(
            x=29.0,
            y=612.0,
            width=302.0,
            height=89.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            67.5,
            567.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_4.place(
            x=29.0,
            y=542.0,
            width=77.0,
            height=48.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            179.5,
            567.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_5.place(
            x=141.0,
            y=542.0,
            width=77.0,
            height=48.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            292.5,
            567.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_6.place(
            x=254.0,
            y=542.0,
            width=77.0,
            height=48.0
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
            264.0,
            495.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_7.place(
            x=198.0,
            y=470.0,
            width=132.0,
            height=48.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=20.0,
            y=720.0,
            width=120.0,
            height=50.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=220.0,
            y=720.0,
            width=120.0,
            height=50.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=12.0,
            y=18.0,
            width=45.0,
            height=45.0
        )
        self.window.resizable(False, False)

    def getWindow(self):
        return self.window
