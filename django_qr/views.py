from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
import uuid  # 👈 added for unique filename
from django.conf import settings


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Make sure MEDIA_ROOT exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # Generate unique filename using uuid
            # use first 8 chars for readability
            unique_id = uuid.uuid4().hex[:8]
            filename = f'{res_name}_{unique_id}_qr.png'
            path = os.path.join(settings.MEDIA_ROOT, filename)

            # Generate and save QR code
            qr = qrcode.make(url)
            qr.save(path)

            return render(request, 'generate_qr_code.html', {
                'form': form,
                'qr_image': filename
            })
    else:
        form = QRCodeForm()

    return render(request, 'generate_qr_code.html', {'form': form})
