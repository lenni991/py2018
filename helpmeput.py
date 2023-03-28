import matplotlib.pyplot as plt
import pytesseract
from gtts import gTTS
from requests import get
import cv2

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

download("https://github.com/lenni991/tessdata/blob/main/eng.traineddata","eng.traineddata")

filename="Image2.jpg" 
# img_cv = cv2.imread(filename)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'  # your path may be different
english_text=pytesseract.image_to_string(filename , lang='eng',config= ".")

print(english_text)