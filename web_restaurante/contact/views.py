from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import JsonResponse

# Create your views here.
def ejecutaAJAX(req):
    respuesta = {}
    if req.method == "POST":

        opcion = req.POST.get('valor','')
        if opcion == '1' or opcion == '2':
            respuesta['estado'] == 'correcto'
            opciones = {}
            opciones['1'] = 'Opcion 1'
            opciones['2'] = 'Opcion 2'
            opciones['3'] = 'Opcion 3'
            opciones['4'] = 'Opcion 4'
            opciones['5'] = 'Opcion 5'
            respuesta['opciones'] = opciones
        else:
            respuesta['estado'] == 'incorrecto'
        
        return JsonResponse(respuesta)

def contact(req):
    contactForm = ContactForm()

    if req.method == "POST":
        contactForm = ContactForm(data=req.POST)
        if contactForm.is_valid():
            name = req.POST.get('name','')
            email = req.POST.get('email','')
            content = req.POST.get('content','')

            # Se envía email a usuario
            subject = 'Gracias por Contactarnos'
            message = f'Hi {name}, gracias por contactarnos, en un momento nos contactaremos contigo...'
            message += "\n\n\n--------------------------------------------\n\n\n" + content
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]


            try:
                send_mail(subject, message, email_from, recipient_list)
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
        

    return render(req, "contact/contact.html", {'form':contactForm})