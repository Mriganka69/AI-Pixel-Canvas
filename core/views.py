from django.shortcuts import render
from .forms import ImageUploadForm

def upload_image(request):
    uploaded_file_url = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uploaded_file_url = form.instance.image.url
    else:
        form = ImageUploadForm()

    return render(request, 'image_upload.html', {
        'form': form,
        'uploaded_file_url': uploaded_file_url
    })

from django.shortcuts import render

def upload_view(request):
    return render(request, 'image_upload.html')