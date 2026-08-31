import re

def clean_text(text):
    ## Remove hyphenation caused by line breaks
    ## e.g. "cor-\nrection" -> "correction"
    text =  re.sub(r"-\s*\n\s*", "" ,text)
    
    ## Replace remaining line breaks with spaces
    text = re.sub(r"\s*\n\s*", " ", text)
    
    ## Collapse repeated whitespaces
    text = re.sub(r"s\s+", " ", text)
    
    return text.strip()

if __name__ == "__main__":
    sample = """
    The Apollo spacecraft uses a primary propul-
    sion system.

    The system provides     thrust for orbital
    maneuvers.
    """

    print("BEFORE:")
    print(sample)

    print("\nAFTER:")
    print(clean_text(sample))