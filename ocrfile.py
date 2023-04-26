import cv2
from PIL import Image
import pytesseract

def ocrgenerate(path):
    print("path===",path)
    image = cv2.imread(path)
    # print(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Store grayscale image as a temporary file to apply OCR
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

    # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))

    print("OCR Text is " + text.strip())
    # val=text.strip().split('D')
    # atte=val[0].split(',')
    # print(atte[0],atte[1])
    # # print(val[1])
    return  text.strip()

ocrgenerate("C:\\Users\\reshm\\OneDrive\\Pictures\\ss1.jpg")