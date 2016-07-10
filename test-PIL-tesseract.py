import pytesseract

from PIL import Image

image = Image.open('D:\\GIT\\test-spider\\index.png')

vcode = pytesseract.image_to_string(image)

print(vcode)