import pyqrcode
import png
from pyqrcode import QRCode

l = str(input("Enter the link:\n"))

url = pyqrcode.create(l)

url.svg("myqr.svg", scale=8)

url.png('myqr.png', scale = 6)
