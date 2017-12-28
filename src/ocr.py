
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

# open image
image = Image.open('test.png')
# code = pytesseract.image_to_string(image, lang='chi_sim')
code = pytesseract.image_to_string(image)
print(code)