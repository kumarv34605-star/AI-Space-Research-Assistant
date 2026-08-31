import json


with open("data/ocr_pages.json", "r", encoding="utf-8") as f:
    original_pages = json.load(f)

with open("data/filtered_ocr_pages.json", "r", encoding="utf-8") as f:
    filtered_pages = json.load(f)


original_numbers = {
    page["page"]
    for page in original_pages
}

filtered_numbers = {
    page["page"]
    for page in filtered_pages
}


removed_pages = sorted(original_numbers - filtered_numbers)

print("Removed pages:", removed_pages)