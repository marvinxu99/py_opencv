"""
https://www.makeuseof.com/how-to-create-and-decode-a-qr-code-using-python/

pip install opencv-python pillow

You can customize: 
    - the fill color, 
    - background color, 
    - image size, 
    - box size, and 
    - border thickness of the QR code
"""


import qrcode
# Data for which you want to make QR code
# Here we are using the URL of the MakeUseOf website
data = "Jane Xu: 604-889-2908, jianpingjin@hotmail.com, WeChat ID: Turbotobin"

# File name of the QR code Image
QRCodefile = "jane_xu.png"

# Generating the QR code
QRimage = qrcode.make(data)
# Saving image into a file
QRimage.save(QRCodefile)