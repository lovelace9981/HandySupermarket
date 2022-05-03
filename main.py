from modules import cameraScanner, qrbarcode
from GUI import carritoGUI, scannerGUI, pasilloGUI, productoGUI, mainMenuGUI

gui = scannerGUI()

myscanner = cameraScanner(gui)

myscanner.scanner

myscanner.window.mainloop()
