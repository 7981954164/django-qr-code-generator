from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=100, label='Restaurant Name')
    url = forms.URLField(label='Menu URL')
