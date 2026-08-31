import pdfplumber
import pytesseract

## Tell pytesseract where the tesseract executable is located
pytesseract.pytesseract.tesseract_cmd = (
    r"D:\Tools\Tesseract-OCR\tesseract.exe"
)

PDF_PATH = "data/raw/apollo_propulsion.pdf"
PAGE_NUMBER = 30

with pdfplumber.open(PDF_PATH) as pdf:
    
    page = pdf.pages[PAGE_NUMBER - 1]
    
    ## Render the PDF page as an image
    image = page.to_image(resolution=300).original
    
    ## Run OCR on the image using pytesseract
    text = pytesseract.image_to_string(image)
    
    print(text)