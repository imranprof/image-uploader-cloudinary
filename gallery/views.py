from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm


def image_upload(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('image_list')
  else:
    form = ImageForm()
  return render(request, 'gallery/upload.html', {'form': form})

def image_list(request):
  images = Image.objects.all()
  return render(request, 'gallery/list.html', {'images': images})
