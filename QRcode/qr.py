import pyqrcode
from png import *
qr=pyqrcode.create('https://ak-tech27.000webhostapp.com')
qr.png("myqr.png",scale=8)

