import pytesseract

from PIL import Image

image = Image.open(r'D:\devtool\PycharmProjects\test-spider\index.png')

vcode = pytesseract.image_to_string(image)

print(vcode)