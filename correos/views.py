from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
def formularioContacto(request):
    return render(request, "correos/formularioContacto.html")


def contactenos(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + \
            " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["salvadorexamplemail@gmail.com"]
        send_mail(asunto, mensaje, email_desde,
                  email_para, fail_silently=False)
        return render(request, "correos/contactoExitoso.html")

    return render(request, "correos/formularioContacto.html")
