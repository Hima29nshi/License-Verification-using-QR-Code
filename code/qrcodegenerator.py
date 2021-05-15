import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "Random Person"
# Generate QR code
u = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
u.png('Random.png', scale=6)
