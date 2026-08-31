import pdfplumber
import pytesseract

## Tesseract installation
pytesseract.pytesseract.tesseract_cmd = (
    r"D:\Tools\Tesseract-OCR\tesseract.exe"
)
PDF_PATH = "data/raw/apollo_propulsion.pdf"

def is_text_usable(text):
    """
    Basic heuristic to determine whether extracted text
    looks usable.
    """

    if not text:
        return False

    text = text.strip()

    if len(text) < 100:
        return False

    # Too many unusual characters can indicate
    # a broken PDF text layer.
    suspicious_chars = sum(
        text.count(char)
        for char in ["�", "!", "@", "#", "$", "%", "^", "&"]
    )

    if suspicious_chars > 10:
        return False

    # Check whether the text contains a reasonable
    # proportion of alphabetic characters.
    letters = sum(char.isalpha() for char in text)

    if letters / len(text) < 0.5:
        return False

    return True

def extract_page(page):
    """
    Try normal PDF text extraction first.
    If no usable text is found, fall back to OCR.
    """
    
    ## Try extracting ttext layer
    text = page.extract_text()
    
    if is_text_usable(text):
        print("Using PDF text extraction.")
        return text
    
    ## If no text was found, fall back to OCR
    print("No text found. Falling back to OCR.")
    
    image = page.to_image(resolution=300).original
    
    text = pytesseract.image_to_string(image)
    
    return text

with pdfplumber.open(PDF_PATH) as pdf:
    
    ## Page -> idx 5
    page = pdf.pages[5]
    text = extract_page(page)
    
    print("\n" + "=" * 70)
    print("Extracted Text:")
    print("=" * 70)
    print(text)