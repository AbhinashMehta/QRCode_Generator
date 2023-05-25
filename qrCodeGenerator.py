import pyqrcode
from pyqrcode import QRCode
s = "https://www.linkedin.com/in/abhinashkumar-mehta-76064a21b"
url = pyqrcode.create(s)
url.svg("myQRforLinkedIn", scale=10)
