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


# Importing libraries
import qrcode
import numpy as np

# Data which for you want to make QR code
# Here we are using URL of MakeUseOf website
data = "https://www.makeuseof.com/"

# Name of the QR code Image file
QRCodefile = "CustomisedImgBoxQRCode.png"

# instantiate QRCode object
# version - an integer between 1 and 40 where 1 is equivalent to 21x21 matrix and 40 is equivalent to 185x185 matrix
#  box_size - the pixels of each box in the QR code
qrObject = qrcode.QRCode(version=1, box_size=12, border=10)

# add data to the QR code
qrObject.add_data(data)

# compile the data into a QR code array
qrObject.make()
image = qrObject.make_image(fill_color="red", back_color="blue")
#image = qrObject.make_image(fill_color="red")

image.save(QRCodefile)

# print the image size (version)
print("Size of the QR image(Version):")
print(np.array(qrObject.get_matrix()).shape)
