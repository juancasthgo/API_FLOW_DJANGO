from django.urls import path
from . import views

urlpatterns = [
    path('crear-pago/', views.create_payment, name='crear_pago'),
    path('confirmacion/', views.payment_confirmation, name='confirmacion'),
]