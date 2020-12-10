import pyqrcode

link = 'https://zoom.us/j/98776845524?pwd=MlR1K3AyLzd6MjBNM2FldkU5Y3dHUT09'
qrcode = pyqrcode.create(link)

qrcode.png('Mom exercise link QR Code.png', scale=6)
