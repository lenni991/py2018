import matplotlib.pyplot as plt
import pytesseract
from requests import get  # to make GET request
import sys, os

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

download("https://github.com/tesseract-ocr/tessdata/blob/main/eng.traineddata","eng.traineddata")

import cv2

filename="gg.png"
img_cv = cv2.imread(filename)
plt.figure(figsize=(20, 20))
plt.imshow(img_cv,cmap = 'gray')
plt.title('template'), plt.xticks([]), plt.yticks([])


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 
english_text=pytesseract.image_to_string(img_cv , lang='eng',config= ".")

print(english_text)