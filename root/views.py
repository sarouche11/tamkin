from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Commune,Compagnion,Registered
from .forms import CaptchaForm, RegisteredForm
from . import data as data_register
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render (request,'index.html')



def register(request):

    if request.method == "POST":
        register_form = RegisteredForm(request.POST)
        captcha_form = CaptchaForm(request.POST)

        if register_form.is_valid() and captcha_form.is_valid():

            register = register_form.save(commit=False)
            register.miclat = False
            register.status = data_register.registration.CHECK_NIN

            register.save()

            return redirect("success", code=register.code)  

            return redirect("register")  # ou autre page

    else:
        register_form = RegisteredForm()
        captcha_form = CaptchaForm()

    context = {
        "register_form": register_form,
        "captcha_form": captcha_form
    }

    return render(request, "register.html", context)




def register_id(request,code):
     
    compagnon = Compagnion.objects.filter(code=code).first()

    # 🔥 si code n'existe pas → redirection
    if not compagnon:
        return redirect(reverse('forbidden', kwargs={'code': 401}))

    if request.method == "POST":
        register_form = RegisteredForm(request.POST)
        captcha_form = CaptchaForm(request.POST)

        if register_form.is_valid() and captcha_form.is_valid():

            register = register_form.save(commit=False)
            register.miclat = False
            register.status = data_register.registration.CHECK_NIN
            register.compagnion = compagnon

            register.save()

           

            
            return redirect("success", code=register.code)  

    else:
        register_form = RegisteredForm()
        captcha_form = CaptchaForm()

    context = {
        "register_form": register_form,
        "captcha_form": captcha_form,
        "compagnon": compagnon
    }

    return render(request, "register.html", context)






def load_communes(request):
    wilaya_id = request.GET.get('wilaya')
    communes = Commune.objects.filter(wilaya_id=wilaya_id).values('id', 'name_fr')
    return JsonResponse(list(communes), safe=False)






def forbidden(request, code):
    code = str(code)

    if code == '403':
        err = "Accès non autorisé"
        detail = "Vous n'avez pas les permissions nécessaires pour accéder à cette page."
    elif code == '404':
        err = "Page non trouvée"
        detail = "La page que vous recherchez est introuvable."
    elif code == '500':
        err = "Erreur serveur"
        detail = "Une erreur interne s'est produite. Veuillez réessayer plus tard."
    elif code == '400':
        err = "Requête invalide"
        detail = "La requête ne peut pas être traitée. Vérifiez les informations envoyées."
    elif code == '401':
        err = "Non authentifié"
        detail = "Vous devez être connecté pour accéder à cette page."
    else:
        err = f"Erreur {code}"
        detail = "Une erreur inattendue s'est produite."

    context = {
        'code': code,
        'err': err,
        'detail': detail,

    }    

    return render(request, 'includes/error.html', context)


def success(request, code):


    register = get_object_or_404(Registered, code=code)

    return render(request, 'success.html', {
        'register': register
    })
