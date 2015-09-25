"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from Registro.models import Persona, Factura, TIPO_PETICION
from django.contrib.auth.models import User

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'EMPRESA DE SERVICIOS PUBLICOS ESP',
            'year':datetime.now().year,
        }))

def peticion(request):
    assert isinstance(request, HttpRequest)
    u = request.GET.get('username', ' ')
    p = User.objects.get(username=u)
    if (len(u)):
        return render(request,'app/peticion.html',
        context_instance = RequestContext(request,
            {
            'title':'Peticiones',
            'message':'Peticiones para la Empresa',
            'year':datetime.now().year,
            'Persona': p,
            },))
    else:
        return render(request, 'app/error.html')


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }))


def consulta(request):
    assert isinstance(request, HttpRequest)
    u = request.GET.get('username', ' ')
    p = User.objects.get(username=u)
    f = Factura.objects.filter(usuario = p)
    if (len(u)):
        return render(request,'app/consulta.html',
        context_instance = RequestContext(request,
            {
            'title':'Consultar',
            'message':'Facturas',
            'year':datetime.now().year,
            'Persona': p,
            'Factura': f,
            },))
    else:
        return render(request, 'app/error.html')

def savePeticion(request):
    assert isinstance(request, HttpRequest)
    u = request.GET.get('username', ' ')
    p = User.objects.get(username=u)
    f = Factura.objects.filter(usuario = p)
    if (len(u)):
        return render(request,'app/index.html')
    else:
        return render(request, 'app/error.html')
