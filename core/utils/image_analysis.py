from PIL import Image
import pytesseract
from collections import Counter
import numpy as np
import os

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_and_colors(image_path, num_colors=5):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # 1. Open image
    image = Image.open(image_path)

    # 2. Extract text using OCR
    extracted_text = pytesseract.image_to_string(image)

    # 3. Resize and extract dominant colors
    small_image = image.resize((150, 150)).convert('RGB')
    pixels = np.array(small_image).reshape((-1, 3))

    color_counts = Counter(map(tuple, pixels))
    most_common_colors = color_counts.most_common(num_colors)

    # Convert RGB to HEX
    dominant_colors = ['#%02x%02x%02x' % color for color, _ in most_common_colors]

    return {
        'text': extracted_text.strip(),
        'colors': dominant_colors
    }
