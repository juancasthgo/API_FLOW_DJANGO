import requests
import hashlib
import hmac
from django.conf import settings
from django.shortcuts import redirect, render

# Utility function to generate HMAC signature
def generate_signature(params):
    sorted_params = ''.join(f"{key}{value}" for key, value in sorted(params.items()))
    signature = hmac.new(settings.FLOW_SECRET_KEY.encode('utf-8'), sorted_params.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature

# View to create a payment
def create_payment(request):
    if request.method == 'POST':
        commerce_order = request.POST.get('commerceOrder')
        subject = request.POST.get('subject')
        currency = request.POST.get('currency')
        amount = request.POST.get('amount')
        email = request.POST.get('email')

        params = {
            'apiKey': settings.FLOW_API_KEY,
            'commerceOrder': commerce_order,
            'subject': subject,
            'currency': currency,
            'amount': amount,
            'email': email,
            'urlConfirmation': 'https://tu-dominio.com/confirmacion/',
            'urlReturn': 'https://tu-dominio.com/retorno/',
        }

        params['s'] = generate_signature(params)

        url = 'https://www.flow.cl/api/payment/create'
        # url de pruebas: 'https://sandbox.flow.cl/api/payment

        response = requests.post(url, data=params)

        if response.status_code == 200:
            data = response.json()
            payment_url = data['url'] + '?token=' + data['token']
            return redirect(payment_url)
        else:
            return render(request, 'inicio.html', {'error': response.text})

    return render(request, 'crear_pago.html')

# View to handle payment confirmation
def payment_confirmation(request):
    if request.method == 'POST':
        token = request.POST.get('token')

        params = {
            'apiKey': settings.FLOW_API_KEY,
            'token': token,
        }
        params['s'] = generate_signature(params)

        url = 'https://www.flow.cl/api/payment/create'
        # url de pruebas: 'https://sandbox.flow.cl/api/payment

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return render(request, 'confirmacion.html', {'status': data})
        else:
            return render(request, 'error.html', {'error': response.text})
