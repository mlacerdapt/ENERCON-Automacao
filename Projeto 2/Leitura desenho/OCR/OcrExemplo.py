import cv2
import pytesseract

img = cv2.imread(r"C:\Users\00082300\Downloads\Projeto 2\Leitura desenho\OCR\imagem2.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\00082300\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
config = r'--oem 3 --psm 6'
resultado = pytesseract.image_to_string(img, config=config)

print(resultado)