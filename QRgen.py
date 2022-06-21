import pyqrcode
import png
from pyqrcode import QRCode

QRlink = 'youtube.com'

url = pyqrcode.create(QRlink)

url.png(r'qr.png', scale=8)
