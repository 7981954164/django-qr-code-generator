# Django QR Code Generator 📱

A simple Django web app that generates QR codes for restaurant menus or any given URL.

## 🚀 Features

- Generate QR codes from any link
- Automatically saves and displays the QR image
- Form to enter restaurant name and menu URL
- Saves generated images to the `/media/` directory

## 🛠 Tech Stack

- Python 3
- Django
- qrcode (Python library)
- HTML5

## 📸 Demo

![QR Generator Screenshot](./test_qr.png)

## 🧪 How to Run Locally

```bash
git clone https://github.com/7981954164/django-qr-code-generator.git
cd django-qr-code-generator
python -m venv env
env\Scripts\activate   # On Windows
pip install -r requirements.txt
python manage.py runserver
