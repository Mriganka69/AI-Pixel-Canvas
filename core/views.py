from django.shortcuts import render, redirect
from .forms import PosterForm
from .models import Poster
from .utils.image_analysis import extract_text_and_colors


import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def home(request):
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            poster = form.save()
            return render(request, 'home.html', {'form': PosterForm(), 'poster': poster})
    else:
        form = PosterForm()
    return render(request, 'home.html', {'form': form})
