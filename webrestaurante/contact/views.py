from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

from django.conf import settings
from django.core.mail import send_mail

from django.http import JsonResponse
import time


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            subject = 'Gracias por contactarnos'
            message = f'Hi {name}, gracias por contactarnos, en un momento nos contactaremos contigo..'
            message += "\n\n\n----------------------------\n\n\n" + content
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)

            # reverse - resuelve la url
            return redirect(reverse('contact')+'?ok')

    return render(request, 'contact/contact.html', {'form': contact_form})


def ejecutaAJAX(request):
    if request.method == "POST":
        # Validamos los campos.
        opcion = request.POST.get('valor', '')
        respuesta = {}
        if opcion == '1' or opcion == '2':
            respuesta['estado'] = 'correcto'
        else:
            respuesta['estado'] = 'No válido'

        opciones = {}
        opciones['1'] = 'Opcion1'
        opciones['2'] = 'Opcion2'
        opciones['3'] = 'Opcion3'
        opciones['4'] = 'Opcion4'
        opciones['5'] = 'Opcion5'

        respuesta['opciones'] = opciones
        time.sleep(5)

        return JsonResponse(respuesta)
