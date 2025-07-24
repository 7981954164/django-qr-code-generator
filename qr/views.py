from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
import uuid
from django.conf import settings


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Ensure media directory exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # Unique filename for QR code image
            unique_id = uuid.uuid4().hex[:8]
            filename = f"{res_name}_{unique_id}_qr.png"
            filepath = os.path.join(settings.MEDIA_ROOT, filename)

            # Generate and save QR code
            qr_img = qrcode.make(url)
            qr_img.save(filepath)

            return render(request, 'generate_qr_code.html', {
                'form': form,
                'qr_code_url': settings.MEDIA_URL + filename,
            })
    else:
        form = QRCodeForm()

    return render(request, 'generate_qr_code.html', {'form': form})
