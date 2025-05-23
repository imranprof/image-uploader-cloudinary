from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm
import cloudinary.uploader

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save()
            print("Image URL:", image_obj.image.url)
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'gallery/list.html', {'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        # Delete from Cloudinary
        if image.image:
            public_id = image.image.name.split('.')[0]  # remove extension
            cloudinary.uploader.destroy(public_id)

        image.delete()
        return redirect('image_list')
    return redirect('image_list')
